---
layout: page
title: Backlog
---
<div id="backlog-toc">
<ul>
  {% assign backlog_sources = "books,games,films,series,misc" | split: "," %}

  {% for source in backlog_sources %}
    {% assign data_key = "backlog_" | append: source %}
    {% assign backlog = site.data[data_key] %}

    {% for section in backlog %}
      {% assign section_key = section[0] %}
      <li>
        <a href="#{{ section_key }}">{{ site.data.translations.backlog[section_key] }}</a>

        {% assign categories = section[1] %}
        {% if categories %}
          <ul>
            {% for category in categories %}
              {% assign category_key = category[0] %}
              {% assign category_items = category[1] %}

              {% if category_items.size > 0 %}
                <li>
                  <a href="#{{ section_key }}-{{ category_key }}">
                    {% assign translation_key = section_key | append: '_categories' %}
                    {% if site.data.translations.backlog[translation_key] and site.data.translations.backlog[translation_key][category_key] %}
                      {{ site.data.translations.backlog[translation_key][category_key] }}
                    {% else %}
                      {{ category_key }}_untranslated
                    {% endif %}
                  </a>
                </li>
              {% endif %}
            {% endfor %}
          </ul>
        {% endif %}
      </li>
    {% endfor %}
  {% endfor %}
</ul>
</div>

{% assign books_section_id = 'books' %}
<div id="{{books_section_id}}" class="backlog-section books-section">
  <h2><i class="fa-solid fa-book category-icon book-icon"></i> {{ site.data.translations.backlog.books }}</h2>

  {% for category in site.data.backlog_books.books %}
    {% assign category_name = category[0] %}
    {% assign subcategories = category[1] %}

    <h3 id="{{books_section_id}}-{{ category_name }}">
      {{ site.data.translations.backlog.books_categories[category_name] }}
    </h3>

    {% assign subcategories_sorted = subcategories %}

    {% for subcategory in subcategories_sorted %}
      {% assign subcategory_name = subcategory[0] %}
      {% assign books_in_subcategory = subcategory[1] %}

      {% if books_in_subcategory.size > 0 %}
        <h4>{{ site.data.translations.backlog.books_subcategories[subcategory_name] }}</h4>

        {% assign books_in_subcategory_sorted = books_in_subcategory | sort: 'series' %}

        <ul>
          {% for book_series in books_in_subcategory_sorted %}
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
</div>

{% assign games_section_id = 'games' %}
<div id="{{games_section_id}}" class="backlog-section games-section">
  <h2><i class="fa-solid fa-gamepad category-icon game-icon"></i> {{ site.data.translations.backlog.games }}</h2>

  <a href="https://store.steampowered.com/wishlist/id/POPKAMOKA/?sort=dateadded">Wishlist Steam</a>

  {% for platform in site.data.backlog_games.games %}
    {% assign platform_name = platform[0] %}
    {% assign games = platform[1] %}

    {% if games.size > 0 %}
      <h3 id="{{games_section_id}}-{{ platform_name }}">
        {{ site.data.translations.backlog.games_categories[platform_name] }}
      </h3>

      {% assign games_sorted = games | sort: 'series' %}

      <ul>
        {% for game_series in games_sorted %}
          <li>
            {% assign series_games_count = game_series.games.size %}
            {% if series_games_count > 1 %}
              {% assign owned_count = 0 %}
              {% assign total_count = game_series.games.size %}

              {% for game in game_series.games %}
                {% if game.ownership_status == 'owned' %}
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
                  {{ game_series.series }}
                  {% if game_series.studio %} - {{ game_series.studio }}{% endif %}
                </summary>
                <ul>
                  {% for game in game_series.games %}
                    <li>
                      {% include ownership_status_icon.html ownership_status=game.ownership_status %}
                      {{ game.title }}
                      {% if game.studio %} - {{ game.studio }}{% endif %}
                    </li>
                  {% endfor %}
                </ul>
              </details>

            {% else %}
              {% assign game = game_series.games[0] %}
              {% include ownership_status_icon.html ownership_status=game.ownership_status %}
              {{ game.title }}
              {% if game.studio %} - {{ game.studio }}{% endif %}
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

{% assign films_section_id = 'films' %}
<div id="{{films_section_id}}" class="backlog-section films-section">
  <h2><i class="fa-solid fa-film category-icon film-icon"></i> {{ site.data.translations.backlog.films }}</h2>
  {% for category in site.data.backlog_films.films %}
    {% assign subcategory_name = category[0] %}
    {% assign subcategory_films = category[1] %}

    {% if subcategory_films.size > 0 %}
      <h3 id="{{films_section_id}}-{{ subcategory_name }}">
        {{ site.data.translations.backlog.films_categories[subcategory_name] }}
      </h3>

      {% assign subcategory_films_sorted = subcategory_films | sort: 'series' %}

      <ul>
        {% for film_series in subcategory_films_sorted %}
          <li>
            {% assign series_films_count = film_series.films.size %}
            {% if series_films_count > 1 %}
                {% assign owned_count = 0 %}
                {% assign total_count = film_series.films.size %}

                {% for film in film_series.films %}
                  {% if film.ownership_status == 'owned' %}
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
                  {{ film_series.series }}

                  {% if film_series.director %} - {{ film_series.director }}
                  {% elsif film_series.studio %} - {{ film_series.studio }}
                  {% endif %}
                </summary>
                <ul>
                  {% for film in film_series.films %}
                    <li>
                      {% include ownership_status_icon.html ownership_status=film.ownership_status %}

                      {% if film.url %}
                        <a href="{{ film.url }}" target="_blank">{{ film.title }}</a>
                      {% else %}
                        {{ film.title }}
                      {% endif %}
                      
                    </li>
                  {% endfor %}
                </ul>
              </details>
            {% else %}
              {% assign film = film_series.films[0] %}
              {% include ownership_status_icon.html ownership_status=film.ownership_status %}

              {% if film.url %}
                <a href="{{ film.url }}" target="_blank">{{ film.title }}</a>
              {% else %}
                {{ film.title }}
              {% endif %}

              {% if film_series.director %} - {{ film_series.director }}
              {% elsif film_series.studio %} - {{ film_series.studio }}

              {% endif %}
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>


{% assign series_section_id = 'series' %}
<div id="{{series_section_id}}" class="backlog-section series-section">
  <h2><i class="fa-solid fa-tv category-icon series-icon"></i> {{ site.data.translations.backlog.series }}</h2>

  {% for subcategory in site.data.backlog_series.series %}
    {% assign subcategory_name = subcategory[0] %}
    {% assign subcategory_series = subcategory[1] %}

    {% if subcategory_series.size > 0 %}
      <h3 id="{{series_section_id}}-{{ subcategory_name }}">
        {{ site.data.translations.backlog.series_categories[subcategory_name] }}
      </h3>

      {% assign subcategory_series_sorted = subcategory_series | sort: 'title' %}

      <ul>
        {% for serie in subcategory_series_sorted %}
          <li>
            {% assign series_seasons_count = serie.seasons.size %}
            {% if series_seasons_count > 1 %}
                {% assign owned_count = 0 %}
                {% assign total_count = serie.seasons.size %}

                {% for serie in serie.seasons %}
                  {% if serie.ownership_status == 'owned' %}
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
                  {{ serie.title }} 

                  {% if serie.director %} - {{ serie.director }} 
                  {% elsif serie.studio %} - {{ serie.studio }} 
                  {% endif %}    
                </summary>
                <ul>
                  {% for season in serie.seasons %}
                    <li>
                      {% include ownership_status_icon.html ownership_status=season.ownership_status %}
                      {{ season.title }}{% if season.episodes %} ({{ season.episodes }} épisode{% if season.episodes > 1 %}s{% endif %}){% endif %}     
                    </li>
                  {% endfor %}
                </ul>
              </details>
            {% else %}
              {% assign season = serie.seasons[0] %}
              {% include ownership_status_icon.html ownership_status=season.ownership_status %}
              {{ serie.title }} 

              {% if serie.director %} - {{ serie.director }} 
              {% elsif serie.studio %} - {{ serie.studio }} 
              {% endif %}   

              {% if season.episodes %} ({{ season.episodes }} épisode{% if season.episodes > 1 %}s{% endif %}){% endif %}  
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

{% assign misc_section_id = 'misc' %}
<div id="{{misc_section_id}}" class="backlog-section misc-section">
  <h2><i class="fa-solid fa-star category-icon default-icon"></i> {{ site.data.translations.backlog.misc }}</h2>
 {% for category in site.data.backlog_misc.misc %}
    {% assign subcategory_name = category[0] %}
    {% assign subcategory_items = category[1] %}

    {% if subcategory_items.size > 0 %}
      <h3 id="{{misc_section_id}}-{{ subcategory_name }}">
        {{ site.data.translations.backlog.misc_categories[subcategory_name] }}
      </h3>

      {% assign subcategory_items_sorted = subcategory_items | sort: 'title' %}

      <ul>
        {% for item in subcategory_items_sorted %}
          <li>
              {% include ownership_status_icon.html ownership_status="not_applicable" %}
              {% if item.url %}
                <a href="{{ item.url }}" target="_blank">{{ item.title }}</a>
              {% else %}
                {{ item.title }}
              {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>

<script src="{{ '/assets/js/backlog-filters.js' | relative_url }}"></script>

