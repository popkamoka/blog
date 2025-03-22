---
layout: page
title: Backlog
---

<div class="backlog-section books-section">
  <h2><i class="fa-solid fa-book category-icon book-icon"></i> {{ site.data.translations.backlog.books }}</h2>

  {% for category in site.data.backlog.books %}
    {% assign category_name = category[0] %}
    {% assign category_books = category[1] %}
    

    {% if category_books.size > 0 %}
      <h3>{{ site.data.translations.backlog.books_categories[category_name] }}</h3>
      <ul>
        {% for book in category_books %}
          <li>
            {% include ownership_status_icon.html ownership_status=book.ownership_status %}
            {{ book.title }}{% if book.author %} - {{ book.author }}{% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

<div class="backlog-section games-section">
  <h2><i class="fa-solid fa-gamepad category-icon game-icon"></i>  {{site.data.translations.backlog.games}}</h2>
  <ul>
    {% for game in site.data.backlog.games %}
      <li>
        {% include ownership_status_icon.html item=game %}
        {{ game.title }} ({{ game.platform }})
      </li>
    {% endfor %}
  </ul>
</div>

<div class="backlog-section films-section">
  <h2> <i class="fa-solid fa-film category-icon film-icon"></i> {{site.data.translations.backlog.films}}</h2>
  <ul>
    {% for film in site.data.backlog.films %}
      <li>
        {% include ownership_status_icon.html item=film %}
        {{ film.title }} - {{ film.director }}
      </li>
    {% endfor %}
  </ul>
</div>

<div class="backlog-section series-section">
  <h2> <i class="fa-solid fa-tv category-icon serie-icon"></i> {{site.data.translations.backlog.series}}</h2>
  <ul>
    {% for serie in site.data.backlog.series %}
      <li>
        {% include ownership_status_icon.html item=serie %}
        {{ serie.title }} ({{ serie.platform }})
      </li>
    {% endfor %}
  </ul>
</div>

<div class="backlog-section misc-section">
  <h2> <i class="fa-solid fa-star category-icon default-icon"></i> {{site.data.translations.backlog.misc}}</h2>
  <ul>
    {% for item in site.data.backlog.misc %}
      <li>
        {% include ownership_status_icon.html item=item %}
        {{ item.title }} - ({{ item.type }})
      </li>
    {% endfor %}
  </ul>
</div>
