document.addEventListener("DOMContentLoaded", function () {
  // Variables globales
  let currentFilter = "all";
  let currentSearchTerm = "";

  // Fonction pour initialiser la recherche
  function initBacklogSearch() {
    const searchInput = document.getElementById("backlog-search");
    const clearButton = document.getElementById("clear-search");

    if (!searchInput || !clearButton) return;

    // Recherche en temps réel
    searchInput.addEventListener("input", function () {
      currentSearchTerm = this.value.toLowerCase().trim();
      applyFiltersAndSearch();
      toggleClearButton();
    });

    // Bouton effacer
    clearButton.addEventListener("click", function () {
      searchInput.value = "";
      currentSearchTerm = "";
      applyFiltersAndSearch();
      toggleClearButton();
      searchInput.focus();
    });

    // Masquer le bouton effacer au départ
    toggleClearButton();
  }

  // Fonction pour afficher/masquer le bouton effacer
  function toggleClearButton() {
    const clearButton = document.getElementById("clear-search");
    const searchInput = document.getElementById("backlog-search");

    if (searchInput.value.length > 0) {
      clearButton.style.display = "flex";
    } else {
      clearButton.style.display = "none";
    }
  }

  // Fonction pour rechercher dans le texte d'un élément
  function searchInElement(element, searchTerm) {
    if (!searchTerm) return true;

    // Récupérer tout le texte de l'élément (sans les balises HTML)
    const textContent = element.textContent.toLowerCase();

    // Recherche simple par inclusion
    return textContent.includes(searchTerm);
  }

  // Fonction pour rechercher dans une section sans filtres de statut (comme misc)
  function searchOnlySection(sectionId) {
    const section = document.getElementById(sectionId);
    if (!section) return;

    const items = section.querySelectorAll("ul li");

    items.forEach((item) => {
      let shouldShow = true;

      // Appliquer seulement la recherche
      if (currentSearchTerm) {
        shouldShow = searchInElement(item, currentSearchTerm);
      }

      // Afficher/masquer l'élément
      item.style.display = shouldShow ? "list-item" : "none";
    });
  }

  // Fonction pour appliquer filtres + recherche
  function applyFiltersAndSearch() {
    const sectionsToFilter = ["books", "games", "films", "series", "misc"];

    sectionsToFilter.forEach((sectionId) => {
      if (sectionId === "misc") {
        // Pour la section misc, on fait seulement la recherche (pas de filtres de statut)
        searchOnlySection(sectionId);
      } else {
        filterAndSearchSection(sectionId);
      }
    });

    // Masquer les catégories vides et les sections entières si nécessaire
    hideEmptyCategoriesAndSections();
  }

  // Fonction pour filtrer et rechercher dans une section
  function filterAndSearchSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (!section) return;

    const items = section.querySelectorAll("ul li");

    items.forEach((item) => {
      let shouldShow = true;

      // 1. Appliquer le filtre de statut
      if (currentFilter !== "all") {
        const parentDetails = item.closest("details");
        let isInPartialSeries = false;
        if (parentDetails) {
          const seriesIcon = parentDetails.querySelector(
            "summary .partially-owned-icon"
          );
          if (seriesIcon) {
            isInPartialSeries = true;
          }
        }

        const ownedIcon = item.querySelector(".owned-icon");
        const notOwnedIcon = item.querySelector(".not-owned-icon");
        const partiallyOwnedIcon = item.querySelector(".partially-owned-icon");

        if (partiallyOwnedIcon || isInPartialSeries) {
          // Séries partielles toujours visibles
          shouldShow = true;
        } else {
          let itemStatus = "";
          if (ownedIcon) {
            itemStatus = "owned";
          } else if (notOwnedIcon) {
            itemStatus = "not_owned";
          }

          if (itemStatus && itemStatus !== currentFilter) {
            shouldShow = false;
          }
        }
      }

      // 2. Appliquer la recherche
      if (shouldShow && currentSearchTerm) {
        shouldShow = searchInElement(item, currentSearchTerm);
      }

      // 3. Afficher/masquer l'élément
      item.style.display = shouldShow ? "list-item" : "none";
    });
  }

  // Fonction globale pour masquer les catégories vides dans toutes les sections
  function hideEmptyCategoriesAndSections() {
    const allSections = ["books", "games", "films", "series", "misc"];

    allSections.forEach((sectionId) => {
      hideEmptyCategoriesInSection(sectionId);
    });

    // Gérer spécifiquement le lien Steam pour la section jeux
    toggleSteamWishlistLink();
  }

  // Fonction pour masquer/afficher le lien Wishlist Steam selon la visibilité des jeux
  function toggleSteamWishlistLink() {
    const steamLink = document.getElementById("steam-wishlist-link");
    if (!steamLink) return;

    const gamesSection = document.getElementById("games");
    if (!gamesSection) return;

    // Compter les jeux visibles dans toute la section
    const visibleGameItems = Array.from(
      gamesSection.querySelectorAll("ul li")
    ).filter((li) => li.style.display !== "none");

    // Masquer le lien si aucun jeu n'est visible
    steamLink.style.display = visibleGameItems.length > 0 ? "inline" : "none";
  }

  // Fonction pour masquer les catégories vides (reprise du fichier existant)
  function hideEmptyCategoriesInAllSections() {
    const sectionsToFilter = ["books", "games", "films", "series"];

    sectionsToFilter.forEach((sectionId) => {
      hideEmptyCategoriesInSection(sectionId);
    });
  }

  function hideEmptyCategoriesInSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (!section) return;

    // Gérer les sous-catégories (h4)
    const subcategories = section.querySelectorAll("h4");
    subcategories.forEach((h4) => {
      const nextUl = h4.nextElementSibling;
      if (nextUl && nextUl.tagName === "UL") {
        const visibleItems = Array.from(nextUl.querySelectorAll("li")).filter(
          (li) => li.style.display !== "none"
        );
        h4.style.display = visibleItems.length > 0 ? "block" : "none";
      }
    });

    // Gérer les catégories principales (h3)
    const categories = section.querySelectorAll("h3");
    categories.forEach((h3) => {
      let hasVisibleContent = false;
      let currentElement = h3.nextElementSibling;

      while (
        currentElement &&
        currentElement.tagName !== "H3" &&
        currentElement.tagName !== "H2"
      ) {
        if (
          currentElement.tagName === "H4" &&
          currentElement.style.display !== "none"
        ) {
          hasVisibleContent = true;
          break;
        } else if (currentElement.tagName === "UL") {
          const visibleItems = Array.from(
            currentElement.querySelectorAll("li")
          ).filter((li) => li.style.display !== "none");
          if (visibleItems.length > 0) {
            hasVisibleContent = true;
            break;
          }
        } else if (currentElement.tagName === "A") {
          // Pour la section games qui a un lien Steam wishlist
          hasVisibleContent = true;
        }
        currentElement = currentElement.nextElementSibling;
      }

      h3.style.display = hasVisibleContent ? "block" : "none";
    });

    // Vérifier si la section entière doit être masquée
    const h2 = section.querySelector("h2");
    if (h2) {
      const visibleCategories = Array.from(
        section.querySelectorAll("h3")
      ).filter((h3) => h3.style.display !== "none");

      // Pour la section games, vérifier aussi les liens directs (mais seulement s'ils sont visibles)
      const directLinks = Array.from(section.querySelectorAll("a")).filter(
        (link) =>
          link.href &&
          link.href.includes("steam") &&
          link.style.display !== "none"
      );

      // Pour la section misc et autres, vérifier les listes directes sous h2
      const directLists = [];
      let currentElement = h2.nextElementSibling;
      while (currentElement && currentElement.tagName !== "H2") {
        if (currentElement.tagName === "UL") {
          const visibleItems = Array.from(
            currentElement.querySelectorAll("li")
          ).filter((li) => li.style.display !== "none");
          if (visibleItems.length > 0) {
            directLists.push(currentElement);
          }
        }
        currentElement = currentElement.nextElementSibling;
      }

      const hasContent =
        visibleCategories.length > 0 ||
        directLinks.length > 0 ||
        directLists.length > 0;
      section.style.display = hasContent ? "block" : "none";
    }
  }

  // Écouter les changements de filtres depuis l'autre script
  function onFilterChange(newFilter) {
    currentFilter = newFilter;
    applyFiltersAndSearch();
  }

  // Interface publique pour l'intégration avec les filtres
  window.backlogSearch = {
    onFilterChange: onFilterChange,
    hideEmptyCategoriesAndSections: hideEmptyCategoriesAndSections,
  };

  // Initialiser la recherche
  initBacklogSearch();
});
