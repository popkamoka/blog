---
layout: page
title: Backlog
---
<h1>🎯 Ma Todo Culture</h1>

<!-- Section Livres -->
<h2>📚 Livres à lire</h2>
<ul>
  {% for book in site.data.todo.books %}
    <li><i class="fa-solid fa-book book-icon"></i> {{ book.title }} - {{ book.author }}</li>
  {% endfor %}
</ul>

<!-- Section Jeux -->
<h2>🎮 Jeux à essayer</h2>
<ul>
  {% for game in site.data.todo.games %}
    <li><i class="fa-solid fa-gamepad game-icon"></i> {{ game.title }} ({{ game.platform }})</li>
  {% endfor %}
</ul>

<!-- Section Films -->
<h2>🎬 Films à voir</h2>
<ul>
  {% for movie in site.data.todo.movies %}
    <li><i class="fa-solid fa-film"></i> {{ movie.title }} - Réal. {{ movie.director }}</li>
  {% endfor %}
</ul>

<!-- Section Séries -->
<h2>📺 Séries à regarder</h2>
<ul>
  {% for serie in site.data.todo.series %}
    <li><i class="fa-solid fa-tv"></i> {{ serie.title }} ({{ serie.platform }})</li>
  {% endfor %}
</ul>

<!-- Section Musique -->
<h2>Divers</h2>
<ul>
  {% for item in site.data.todo.misc %}
    <li><i class="fa-solid fa-star"></i> {{ item.title }}</li>
  {% endfor %}
</ul>
