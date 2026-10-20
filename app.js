const themeToggle = document.querySelector(".theme-toggle");
const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector(".site-nav");
const filterButtons = [...document.querySelectorAll(".filter-button")];
const projectCards = [...document.querySelectorAll(".project-card")];
const projectSearch = document.querySelector("#project-search");
const noResults = document.querySelector("#no-results");
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

siteNav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    menuToggle?.setAttribute("aria-expanded", "false");
    siteNav.classList.remove("is-open");
  });
});

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

const year = document.querySelector("#current-year");
if (year) year.textContent = String(new Date().getFullYear());
