---
layout: list
title: Livres
---

<section class="posts">
    <ul>
        {% assign books = site.posts | where_exp: "post", "post.categories contains 'book'" | sort: "date" | reverse %}
        {% for post in books %}
        <li class="book-item">
            <a href="{{ site.baseurl }}{{ post.url }}">
                {{ post.title }}
            </a>
            <time datetime="{{ post.date | date_to_xmlschema }}">
                {{ post.date | date: "%d-%m-%Y" }}
            </time>
        </li>
        {% endfor %}
    </ul>
</section>
