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

      {% assign category_books_sorted = category_books | sort: "series" %}

      <ul>
        {% for book_series in category_books_sorted %}
          <li>
            {% assign series_books_count = book_series.books.size %}
            {% if series_books_count > 1 %}
              <details>
                <summary>{{ book_series.series }} - {{ book_series.author }} {% if book_series.edition %} ({{ book_series.edition }}){% endif %} </summary>
                <ul>
                  {% for book in book_series.books %}
                    <li>
                      {% include ownership_status_icon.html ownership_status=book.ownership_status %}
                      {{ book.title }}{% if book.author %} - {{ book.author }}{% endif %}
                    </li>
                  {% endfor %}
                </ul>
              </details>
            {% else %}
              {% assign book = book_series.books[0] %}
              {% include ownership_status_icon.html ownership_status=book.ownership_status %}
              {{ book.title }} - {{ book_series.author }} {% if book_series.edition %} ({{ book_series.edition }}){% endif %}
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

<div class="backlog-section games-section">
  <h2><i class="fa-solid fa-gamepad category-icon game-icon"></i>  {{site.data.translations.backlog.games}}</h2>
{% for platform in site.data.backlog.games %}
    {% assign platform_name = platform[0] %}
    {% assign games = platform[1] %}

    {% if games.size > 0 %}
      <h3>{{ site.data.translations.backlog.games_platforms[platform_name] }}</h3>
      <ul>
        {% for game in games %}
          <li>
            {% include ownership_status_icon.html ownership_status=game.ownership_status %}
            {{ game.title }}{% if game.studio %} - {{ game.studio }}{% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
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
  <h2><i class="fa-solid fa-tv category-icon series-icon"></i>  {{site.data.translations.backlog.series}}</h2>
  
  {% for genre in site.data.backlog.series %}
    {% assign genre_name = genre[0] %}
    {% assign series = genre[1] %}

    {% if series.size > 0 %}
      <h3>{{ site.data.translations.backlog.series_genres[genre_name] }}</h3>
      <ul>
        {% for serie in series %}
          <li>
            {% assign series_seasons_count = serie.seasons.size %}
            {% if series_seasons_count > 1 %}
              <details>
                <summary>{{ serie.title }}</summary>
                <ul>
                  {% for season in serie.seasons %}
                    <li>
                      {% include ownership_status_icon.html ownership_status=season.ownership_status %}
                      {{ season.title }} ({{ season.episodes }} épisodes)
                    </li>
                  {% endfor %}
                </ul>
              </details>
            {% else %}
              {% assign season = serie.seasons[0] %}
              {% include ownership_status_icon.html ownership_status=season.ownership_status %}
              <p>{{ serie.title }} - {{ season.title }} ({{ season.episodes }} épisodes)</p>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
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
