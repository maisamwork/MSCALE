let CATALOG = [];

function copyText(text, btn) {
  navigator.clipboard.writeText(text).then(() => {
    const old = btn.textContent;
    btn.textContent = "Copied!";
    setTimeout(() => (btn.textContent = old), 1200);
  });
}

function el(id) {
  return document.getElementById(id);
}

async function loadCatalog() {
  const list = el("tool-list");
  if (!list) return;
  try {
    const res = await fetch("data/catalog.json");
    CATALOG = await res.json();
  } catch {
    try {
      const res = await fetch("../data/catalog.json");
      CATALOG = await res.json();
    } catch {}
  }
  const live = (window.LIVE_TOOLS || []).map((t) => ({ ...t, live: true }));
  renderList(live);
}

function renderList(items) {
  const list = el("tool-list");
  if (!list) return;
  list.innerHTML = items
    .map(
      (t) => `<a class="card ${t.live ? "" : "soon"}" href="${t.url}">
        <div class="card-head">${(window.ICONS && window.ICONS[t.catSlug]) || ""}<h3>${t.name}</h3></div>
        <p>${t.desc || ""}</p>
        <span class="tag">${t.live ? "LIVE" : (t.cat || "") + (t.live ? "" : " — coming soon")}</span>
      </a>`
    )
    .join("");
  const count = el("count-note");
  if (count) count.textContent = `Showing ${items.length} of ${(window.LIVE_TOOLS || []).length + CATALOG.length} tools`;
}

function setupSearch() {
  const input = el("search");
  if (!input) return;
  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    const live = (window.LIVE_TOOLS || []).filter((t) => t.name.toLowerCase().includes(q));
    const soon = CATALOG.filter((t) => t.n.toLowerCase().includes(q)).slice(0, 60)
      .map((t) => ({ name: t.n, cat: t.c, desc: t.s || "", url: t.c ? t.c + "/" : "#" }));
    renderList([...live, ...soon]);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  loadCatalog();
  setupSearch();
});
