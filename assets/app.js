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

(function () {
  var t = document.getElementById("nav-toggle");
  var n = document.getElementById("main-nav");
  if (t && n) {
    t.addEventListener("click", function () {
      var open = n.classList.toggle("open");
      t.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
})();

(function () {
  var b = document.getElementById("theme-toggle");
  if (b) b.addEventListener("click", function () {
    var cur = document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", cur);
    try { localStorage.setItem("mscale-theme", cur); } catch (e) {}
  });
})();

function escHtml2(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

var HOT_TOOLS = { "word-counter": 1, "password-generator": 1, "json-formatter": 1, "qr-code-generator": 1,
  "image-compressor": 1, "pdf-merge": 1, "unit-converter": 1, "loan-emi-calculator": 1,
  "percentage-calculator": 1, "case-converter": 1, "compound-interest-pro": 1, "image-resizer": 1 };

function toolCardHtml(t, catName, hue) {
  var ic = (window.ICONS || {})[t.catSlug || t.cat] || "";
  var head = '<div class="card-head">' + ic.replace("<svg ", '<svg class="card-ic" style="color:' + hue + '" ') + "<h3>" + escHtml2(t.name) + "</h3>" + (t.live && HOT_TOOLS[t.slug] ? '<span class="hot-tag hot">HOT</span>' : "") + "</div>";
  var desc = "<p>" + escHtml2(t.desc || "") + "</p>";
  var badge = '<span class="badge" style="color:' + hue + ';background:' + hue + '22">' + escHtml2(catName) + "</span>";
  var status = t.live
    ? '<span class="status live"><span class="dot"></span>Online</span>'
    : '<span class="status soon"><span class="dot"></span>Coming soon</span>';
  var meta = '<div class="card-meta">' + badge + status + "</div>";
  var cta = '<span class="card-cta">Details &rarr;</span>';
  if (t.live) {
    return '<a class="card tool-card" href="' + t.url + '">' + head + desc + meta + cta + "</a>";
  }
  return '<div class="card soon tool-card">' + head + desc + meta + "</div>";
}

function initToolsPage() {
  var grid = document.getElementById("tools-grid");
  if (!grid) return;
  var state = { cat: "all", q: "", sort: "pop", shown: 1e9 };
  try {
    var qp = new URLSearchParams(location.search).get("q");
    if (qp) { state.q = qp.toLowerCase(); var si = document.getElementById("tools-search"); if (si) si.value = qp; }
  } catch (e) {}
  var ALL = [];
  var catName = {};
  var hueOf = function (cs) {
    var hues = { "calculators": "#ff9a3c", "text-tools": "#4cc3ff", "developer-tools": "#a78bfa", "converters": "#2dd4bf", "security": "#34d399", "color-tools": "#f472b6", "random-generators": "#fbbf24", "pdf-tools": "#f87171", "image-tools": "#e879f9", "seo-web-tools": "#22d3ee", "date-time-tools": "#60a5fa", "finance-tools": "#10b981" };
    return hues[cs] || "#ff7000";
  };
  var SLUG_NAMES = { "calculators": "Calculators", "text-tools": "Text Tools", "developer-tools": "Developer Tools", "converters": "Converters", "security": "Security", "color-tools": "Color Tools", "random-generators": "Random Generators", "pdf-tools": "PDF Tools", "image-tools": "Image Tools", "seo-web-tools": "SEO & Web Tools", "date-time-tools": "Date & Time Tools", "finance-tools": "Finance Tools" };
  (window.LIVE_TOOLS || []).forEach(function (t) {
    var sl = t.url.replace(/^tools\//, "").replace(/\.html$/, "");
    ALL.push({ name: t.name, desc: t.desc, cat: t.catSlug, slug: sl, live: true, url: t.url.replace(/^tools\//, "") });
    catName[t.catSlug] = t.cat;
  });
  var hueFor = {};
  Object.keys(catName).forEach(function (cs) { hueFor[cs] = hueOf(cs); });

  function filtered() {
    var q = state.q.toLowerCase();
    var list = ALL.filter(function (t) {
      if (state.cat !== "all" && t.cat !== state.cat) return false;
      if (q && (t.name + " " + (t.desc || "") + " " + (catName[t.cat] || "")).toLowerCase().indexOf(q) === -1) return false;
      return true;
    });
    if (state.sort === "az") list.sort(function (a, b) { return a.name.toLowerCase() < b.name.toLowerCase() ? -1 : 1; });
    else if (state.sort === "za") list.sort(function (a, b) { return a.name.toLowerCase() > b.name.toLowerCase() ? -1 : 1; });
    else list.sort(function (a, b) { return (b.live ? 1 : 0) - (a.live ? 1 : 0); });
    return list;
  }

  function render() {
    var list = filtered();
    var slice = list.slice(0, state.shown);
    grid.innerHTML = slice.map(function (t) {
      return toolCardHtml(t, catName[t.cat] || t.cat, hueFor[t.cat] || hueOf(t.cat));
    }).join("");
    document.getElementById("tools-count").textContent =
      "Showing " + slice.length + " of " + list.length + " tools" +
      (state.cat !== "all" ? " in " + (catName[state.cat] || state.cat) : "");
    var more = document.getElementById("tools-more");
    more.style.display = list.length > state.shown ? "inline-block" : "none";
  }

  var input = document.getElementById("tools-search");
  if (input) input.addEventListener("input", function () { state.q = input.value; render(); });
  var sort = document.getElementById("tools-sort");
  if (sort) sort.addEventListener("change", function () { state.sort = sort.value; render(); });
  var side = document.getElementById("tools-side");
  if (side) side.addEventListener("click", function (e) {
    var btn = e.target.closest(".side-item");
    if (!btn) return;
    side.querySelectorAll(".side-item").forEach(function (b) { b.classList.remove("active"); });
    btn.classList.add("active");
    state.cat = btn.getAttribute("data-cat");
    render();
  });
  var chips = document.getElementById("cat-chips");
  if (chips) chips.addEventListener("click", function (e) {
    var btn = e.target.closest(".chip");
    if (!btn) return;
    chips.querySelectorAll(".chip").forEach(function (b) { b.classList.remove("active"); });
    btn.classList.add("active");
    state.cat = btn.getAttribute("data-cat");
    if (side) {
      side.querySelectorAll(".side-item").forEach(function (b) { b.classList.toggle("active", b.getAttribute("data-cat") === state.cat); });
    }
    render();
  });
  var more = document.getElementById("tools-more");
  if (more) more.parentNode && more.parentNode.style && (more.parentNode.style.display = "none");

  function useCatalog(catalog) {
    (catalog || []).forEach(function (c) {
      ALL.push({ name: c.n, desc: c.s, cat: c.c, live: false, url: "../" + c.c + "/" });
      if (!catName[c.c]) catName[c.c] = SLUG_NAMES[c.c] || c.c;
    });
    render();
  }
  if (window.CATALOG && window.CATALOG.length) useCatalog(window.CATALOG);
  else fetch("../data/catalog.json").then(function (r) { return r.json(); }).then(useCatalog).catch(function () { render(); });
  render();
}

if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initToolsPage);
else initToolsPage();

/* Newsletter subscribe (client-side placeholder) */
function nlSub(e) {
  e.preventDefault();
  var el = document.getElementById("nl-msg");
  if (el) el.textContent = "You’re on the list — welcome aboard!";
  e.target.reset();
  return false;
}
