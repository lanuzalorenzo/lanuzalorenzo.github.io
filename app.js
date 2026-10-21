const themeToggle = document.querySelector(".theme-toggle");
const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector(".site-nav");
const navLinks = [...document.querySelectorAll('.site-nav > a[href^="#"]')];
const filterButtons = [...document.querySelectorAll(".filter-button")];
const projectCards = [...document.querySelectorAll(".project-card")];
const projectSearch = document.querySelector("#project-search");
const noResults = document.querySelector("#no-results");
const projectStatus = document.querySelector("#project-status");
const portfolioExpand = document.querySelector(".portfolio-expand");
const moduleGroups = [...document.querySelectorAll(".module-group")];
const themeColor = document.querySelector('meta[name="theme-color"]');
const themeStorageKey = "portfolio-theme-v2";

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  if (themeColor) themeColor.content = theme === "dark" ? "#081725" : "#edf5fa";
  if (themeToggle) {
    const isDark = theme === "dark";
    themeToggle.setAttribute("aria-label", `Cambiar a tema ${isDark ? "claro" : "oscuro"}`);
    themeToggle.setAttribute("aria-pressed", String(isDark));
  }
}

let savedTheme = null;
try {
  savedTheme = localStorage.getItem(themeStorageKey);
} catch (error) {
  console.warn("No se pudo recuperar la preferencia de tema.", error);
}
setTheme(savedTheme === "dark" || savedTheme === "light" ? savedTheme : "dark");

themeToggle?.addEventListener("click", () => {
  const theme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  setTheme(theme);
  try {
    localStorage.setItem(themeStorageKey, theme);
  } catch (error) {
    console.warn("No se pudo guardar la preferencia de tema.", error);
  }
});

menuToggle?.addEventListener("click", () => {
  const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
  menuToggle.setAttribute("aria-expanded", String(!isOpen));
  siteNav?.classList.toggle("is-open", !isOpen);
});

function closeMenu() {
  menuToggle?.setAttribute("aria-expanded", "false");
  siteNav?.classList.remove("is-open");
}

siteNav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", closeMenu);
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
  const query = projectSearch?.value.trim().toLocaleLowerCase("es") ?? "";
  let visibleCount = 0;

  projectCards.forEach((card) => {
    const matchesFilter = activeFilter === "all" || card.dataset.category === activeFilter;
    const matchesSearch = (card.dataset.search ?? "").toLocaleLowerCase("es").includes(query);
    const isVisible = matchesFilter && matchesSearch;
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

projectSearch?.addEventListener("input", updateProjects);

function syncPortfolioExpand() {
  if (!portfolioExpand) return;
  const allOpen = moduleGroups.length > 0 && moduleGroups.every((group) => group.open);
  portfolioExpand.setAttribute("aria-expanded", String(allOpen));
  portfolioExpand.textContent = allOpen ? "Contraer todos" : "Desplegar todos";
}

portfolioExpand?.addEventListener("click", () => {
  const expand = portfolioExpand.getAttribute("aria-expanded") !== "true";
  moduleGroups.forEach((group) => {
    group.open = expand;
  });
  syncPortfolioExpand();
});

moduleGroups.forEach((group) => group.addEventListener("toggle", syncPortfolioExpand));
syncPortfolioExpand();

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
  syncPortfolioExpand();
});

const year = document.querySelector("#current-year");
if (year) year.textContent = String(new Date().getFullYear());
