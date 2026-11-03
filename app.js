const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector(".site-nav");
const navLinks = [...document.querySelectorAll('.site-nav a[href^="#"]')];
const filterButtons = [...document.querySelectorAll(".filter-button")];
const projectCards = [...document.querySelectorAll(".project-card")];
const noResults = document.querySelector("#no-results");
const projectStatus = document.querySelector("#project-status");
const expandButtons = [...document.querySelectorAll("[data-expand-all]")];
const menuToggleLabel = menuToggle?.querySelector(".sr-only");

// Las anclas antiguas de la portada viven ahora en páginas propias. Se conserva
// el fragmento para que un enlace a un grupo concreto caiga en su sitio.
// `replace` no deja entrada en el historial: «atrás» vuelve a donde estaba.
const legacyPages = [
  ["#portfolio", "portfolio.html"],
  ["#capa-", "portfolio.html"],
  ["#api", "api.html"],
  ["#ia", "ia.html"],
];
const atHome = location.pathname.endsWith("/") || /(?:^|\/)index\.html$/.test(location.pathname);
const legacyPage = atHome ? legacyPages.find(([prefix]) => location.hash.startsWith(prefix)) : null;
if (legacyPage) location.replace(legacyPage[1] + location.hash);

function setMenuOpen(isOpen) {
  menuToggle?.setAttribute("aria-expanded", String(isOpen));
  siteNav?.classList.toggle("is-open", isOpen);
  document.documentElement.classList.toggle("menu-open", isOpen);
  if (menuToggleLabel) menuToggleLabel.textContent = isOpen ? "Cerrar menú" : "Abrir menú";
}

menuToggle?.addEventListener("click", () => {
  setMenuOpen(menuToggle.getAttribute("aria-expanded") !== "true");
});

function closeMenu() {
  setMenuOpen(false);
}

window.matchMedia("(min-width: 851px)").addEventListener("change", (event) => {
  if (event.matches) closeMenu();
});

siteNav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    const wasOpen = siteNav.classList.contains("is-open");
    closeMenu();
    if (!wasOpen) return;
    const id = link.hash.slice(1);
    const target = id ? document.getElementById(id) : null;
    if (!target) return;
    target.setAttribute("tabindex", "-1");
    target.focus({ preventScroll: true });
  });
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && siteNav?.classList.contains("is-open")) {
    closeMenu();
    menuToggle?.focus();
  }
});

document.addEventListener("click", (event) => {
  if (!siteNav?.classList.contains("is-open")) return;
  if (siteNav.contains(event.target) || menuToggle?.contains(event.target)) return;
  closeMenu();
});

function setActiveSection(id) {
  navLinks.forEach((link) => {
    const isActive = id !== null && link.getAttribute("href") === `#${id}`;
    link.classList.toggle("is-active", isActive);
    if (isActive) link.setAttribute("aria-current", "location");
    else link.removeAttribute("aria-current");
  });
}

function updateActiveSection() {
  // En las páginas de detalle el enlace activo lo fija el build: no hay spy.
  if (navLinks.length === 0) return;

  const header = document.querySelector(".site-header");
  const marker = window.scrollY + (header?.offsetHeight ?? 78) + window.innerHeight * 0.18;
  const sections = [...document.querySelectorAll("main > section[id]")];
  let current = null;

  sections.forEach((section) => {
    if (section.getBoundingClientRect().top + window.scrollY <= marker) current = section.id;
  });

  if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
    current = sections.at(-1)?.id ?? current;
  }

  setActiveSection(current === "inicio" ? null : current);
}

let spyFrame = null;
window.addEventListener("scroll", () => {
  if (spyFrame !== null) return;
  spyFrame = requestAnimationFrame(() => {
    updateActiveSection();
    spyFrame = null;
  });
}, { passive: true });
window.addEventListener("resize", updateActiveSection);
updateActiveSection();

function updateProjects() {
  const activeFilter = document.querySelector(".filter-button.is-active")?.dataset.filter ?? "all";
  let visibleCount = 0;

  projectCards.forEach((card) => {
    const isVisible = activeFilter === "all" || card.dataset.category === activeFilter;
    card.hidden = !isVisible;
    visibleCount += Number(isVisible);
  });

  if (noResults) noResults.hidden = visibleCount > 0;
  if (projectStatus) {
    projectStatus.textContent = `Mostrando ${visibleCount} de ${projectCards.length} proyectos.`;
  }
}

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    filterButtons.forEach((item) => {
      const isActive = item === button;
      item.classList.toggle("is-active", isActive);
      item.setAttribute("aria-pressed", String(isActive));
    });
    updateProjects();
  });
});

const expandControllers = expandButtons.map((button) => {
  const scope = document.querySelector(button.dataset.expandAll);
  const groups = scope ? [...scope.querySelectorAll(".module-group")] : [];

  const sync = () => {
    const allOpen = groups.length > 0 && groups.every((group) => group.open);
    button.setAttribute("aria-expanded", String(allOpen));
    button.textContent = allOpen ? "Contraer todos" : "Desplegar todos";
  };

  button.addEventListener("click", () => {
    const expand = button.getAttribute("aria-expanded") !== "true";
    groups.forEach((group) => {
      group.open = expand;
    });
    sync();
  });

  groups.forEach((group) => group.addEventListener("toggle", sync));
  sync();

  return sync;
});

const expandableItems = [...document.querySelectorAll(".timeline-item, .module-group")];
let printState = [];

window.addEventListener("beforeprint", () => {
  printState = expandableItems.map((item) => item.open);
  expandableItems.forEach((item) => {
    item.open = true;
  });
});

window.addEventListener("afterprint", () => {
  expandableItems.forEach((item, index) => {
    item.open = printState[index] ?? item.open;
  });
  expandControllers.forEach((sync) => sync());
});

const year = document.querySelector("#current-year");
if (year) year.textContent = String(new Date().getFullYear());
