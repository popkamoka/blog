document.addEventListener("DOMContentLoaded", function () {
  // Fonction pour initialiser les filtres globaux du backlog
  function initGlobalBacklogFilters() {
    const filterContainer = document.querySelector(".global-filter-container");
    if (!filterContainer) return;

    // Ajouter les événements aux boutons
    const filterButtons = filterContainer.querySelectorAll(".filter-btn");
    filterButtons.forEach((button) => {
      button.addEventListener("click", function () {
        // Retirer la classe active de tous les boutons
        filterButtons.forEach((btn) => btn.classList.remove("active"));
        // Ajouter la classe active au bouton cliqué
        this.classList.add("active");

        // Filtrer toutes les sections
        filterAllSections(this.dataset.filter);
      });
    });
  }

  // Fonction pour filtrer toutes les sections du backlog
  function filterAllSections(filter) {
    // Sections à filtrer (exclut 'misc' qui n'a pas d'ownership status)
    const sectionsToFilter = ["books", "games", "films", "series"];

    sectionsToFilter.forEach((sectionId) => {
      filterSection(sectionId, filter);
    });

    // Masquer les catégories vides dans toutes les sections
    hideEmptyCategoriesInAllSections();
  }

  // Fonction pour filtrer une section spécifique
  function filterSection(sectionId, filter) {
    const section = document.getElementById(sectionId);
    if (!section) return;

    const items = section.querySelectorAll("ul li");

    // Filtrer les éléments individuels
    items.forEach((item) => {
      if (filter === "all") {
        item.style.display = "list-item";
        return;
      }

      // Vérifier si l'élément est dans une série partiellement possédée
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

      // Chercher l'icône de statut dans l'élément lui-même
      const ownedIcon = item.querySelector(".owned-icon");
      const notOwnedIcon = item.querySelector(".not-owned-icon");
      const partiallyOwnedIcon = item.querySelector(".partially-owned-icon");

      // Si c'est une série partielle OU un livre dans une série partielle, toujours afficher
      if (partiallyOwnedIcon || isInPartialSeries) {
        item.style.display = "list-item";
        return;
      }

      // Déterminer le statut pour les autres éléments
      let itemStatus = "";
      if (ownedIcon) {
        itemStatus = "owned";
      } else if (notOwnedIcon) {
        itemStatus = "not_owned";
      } else {
        // Si aucune icône n'est trouvée, afficher l'élément
        item.style.display = "list-item";
        return;
      }

      // Afficher ou masquer l'élément selon le filtre
      if (itemStatus === filter) {
        item.style.display = "list-item";
      } else {
        item.style.display = "none";
      }
    });
  }

  // Fonction pour masquer les catégories vides dans toutes les sections
  function hideEmptyCategoriesInAllSections() {
    const sectionsToFilter = ["books", "games", "films", "series"];

    sectionsToFilter.forEach((sectionId) => {
      hideEmptyCategoriesInSection(sectionId);
    });
  }

  // Fonction pour masquer les catégories vides dans une section
  function hideEmptyCategoriesInSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (!section) return;

    // Gérer les sous-catégories (h4) d'abord
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
      // Vérifier s'il y a des sous-catégories visibles ou des listes directement après h3
      let hasVisibleContent = false;
      let currentElement = h3.nextElementSibling;

      while (currentElement && currentElement.tagName !== "H3") {
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
        }
        currentElement = currentElement.nextElementSibling;
      }

      h3.style.display = hasVisibleContent ? "block" : "none";
    });
  }

  // Initialiser les filtres globaux
  initGlobalBacklogFilters();
});
