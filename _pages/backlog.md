---
layout: page
title: Backlog
---
<div class="backlog-section books-section">
  <h2><i class="fa-solid fa-book category-icon book-icon"></i> {{ site.data.translations.backlog.books }}</h2>

  {% for category in site.data.backlog.books %}
    {% assign category_name = category[0] %}
    {% assign genres_in_category = category[1] %}

    <h2>{{ site.data.translations.backlog.books_categories[category_name] }}</h2>

    {% for genre in genres_in_category %}
      {% assign genre_name = genre[0] %}
      {% assign editors_in_genre = genre[1] %}

      <h3>{{ site.data.translations.backlog.books_genres[genre_name] }}</h3>

      {% for editor in editors_in_genre %}
        {% assign editor_name = editor[0] %}
        {% assign books_in_editor = editor[1] %}

        {% if books_in_editor.size > 0 %}
          <h4>{{ site.data.translations.backlog.books_editors[editor_name] }}</h4>

          {% assign books_in_editor_sorted = books_in_editor | sort: 'series' %}

          <ul>
            {% for book_series in books_in_editor_sorted %}
              <li>
                {% assign series_books_count = book_series.books.size %}
                {% if series_books_count > 1 %}
                  {% assign owned_count = 0 %}
                  {% assign total_count = book_series.books.size %}

                  {% for book in book_series.books %}
                    {% if book.ownership_status == 'owned' %}
                      {% assign owned_count = owned_count | plus: 1 %}
                    {% endif %}
                  {% endfor %}

                  {% if owned_count == total_count %}
                    {% assign series_ownership_status = 'owned' %}
                  {% elsif owned_count == 0 %}
                    {% assign series_ownership_status = 'not_owned' %}
                  {% else %}
                    {% assign series_ownership_status = 'partially_owned' %}
                  {% endif %}

                  <details>
                    <summary>
                      {% include ownership_status_icon.html ownership_status=series_ownership_status %}
                      {{ book_series.series }} - {{ book_series.author }}
                      {% if book_series.edition %} ({{ book_series.edition }}){% endif %}
                      {% if book_series.price %} ({{ book_series.price }}€){% endif %}
                    </summary>
                    <ul>
                      {% for book in book_series.books %}
                        <li>
                          {% include ownership_status_icon.html ownership_status=book.ownership_status %}
                          {{ book.title }}
                          {% if book.edition %} ({{ book.edition }}){% endif %}
                          {% if book.price %} ({{ book.price }}€){% endif %}
                        </li>
                      {% endfor %}
                    </ul>
                  </details>

                {% else %}
                  {% assign book = book_series.books[0] %}
                  {% include ownership_status_icon.html ownership_status=book.ownership_status %}
                  {{ book.title }} - {{ book_series.author }}
                  {% if book.edition %} ({{ book.edition }}){% endif %}
                  {% if book.price %} ({{ book.price }}€){% endif %}
                {% endif %}
              </li>
            {% endfor %}
          </ul>
        {% endif %}
      {% endfor %}
    {% endfor %}
  {% endfor %}
</div>


<div class="backlog-section games-section">
  <h2><i class="fa-solid fa-gamepad category-icon game-icon"></i> {{ site.data.translations.backlog.games }}</h2>
  {% for platform in site.data.backlog.games %}
    {% assign platform_name = platform[0] %}
    {% assign games = platform[1] %}

    {% if games.size > 0 %}
      <h3>{{ site.data.translations.backlog.games_platforms[platform_name] }}</h3>
      <ul>
        {% for game in games %}
          <li>
            {% include ownership_status_icon.html ownership_status=game.ownership_status %}
            {{ game.title -}}
            {%- if game.studio %} - {{ game.studio }}{% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

<div class="backlog-section films-section">
  <h2><i class="fa-solid fa-film category-icon film-icon"></i> {{ site.data.translations.backlog.films }}</h2>
  {% for category in site.data.backlog.films %}
    {% assign genre_name = category[0] %}
    {% assign genre_films = category[1] %}

    {% if genre_films.size > 0 %}
      <h3>{{ site.data.translations.backlog.media_genres[genre_name] }}</h3>

      {% assign genre_films_sorted = genre_films | sort: 'series' %}

      <ul>
        {% for film_series in genre_films_sorted %}
          <li>
            {% assign series_films_count = film_series.films.size %}
            {% if series_films_count > 1 %}
              <details>
                <summary>{{ film_series.series }} - {{ film_series.director }}</summary>
                <ul>
                  {% for film in film_series.films %}
                    <li>
                      {% include ownership_status_icon.html ownership_status=film.ownership_status %}
                      {{ film.title }}
                    </li>
                  {% endfor %}
                </ul>
              </details>
            {% else %}
              {% assign film = film_series.films[0] %}
              {% include ownership_status_icon.html ownership_status=film.ownership_status %}
              {{ film.title }} - {{ film_series.director }}
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

<div class="backlog-section series-section">
  <h2><i class="fa-solid fa-tv category-icon series-icon"></i> {{ site.data.translations.backlog.series }}</h2>

  {% for genre in site.data.backlog.series %}
    {% assign genre_name = genre[0] %}
    {% assign series = genre[1] %}

    {% if series.size > 0 %}
      <h3>{{ site.data.translations.backlog.media_genres[genre_name] }}</h3>
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
  <h2><i class="fa-solid fa-star category-icon default-icon"></i> {{ site.data.translations.backlog.misc }}</h2>
  <ul>
    {% for item in site.data.backlog.misc %}
      <li>
        {% include ownership_status_icon.html item=item %}
        {{ item.title }} - ({{ item.type }})
      </li>
    {% endfor %}
  </ul>
</div>
