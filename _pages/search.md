---
layout: page
title: Recherche
---
<style>
  #search-container {
    max-width: 100%;
  }

  input[type='text'] {
    font-size: normal;
    outline: none;
    padding: 1rem;
    background: rgb(236, 237, 238);
    width: 100%;
    -webkit-appearance: none;
    font-family: inherit;
    font-size: 100%;
    border: none;
  }
  #results-container {
    margin: 0.5rem 0;
  }
</style>

<!-- Html Elements for Search -->
<div id="search-container">
  <input type="text" id="search-input" placeholder="Rechercher...">
  <ol id="results-container"></ol>
</div>

<!-- Script pointing to search-script.js -->
<script src="{{ site.baseurl }}/search.js" type="text/javascript"></script>

<!-- Configuration -->
<script type="text/javascript">
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '{{ site.baseurl }}/search.json',
    searchResultTemplate: '<li><a href="{url}" title="{description}">{title}</a></li>',
    noResultsText: 'Pas de résultat',
    limit: 10,
    fuzzy: false,
    exclude: ['Welcome'],
  });
</script>
