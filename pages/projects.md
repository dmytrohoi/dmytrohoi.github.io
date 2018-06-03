---
layout: page
show_meta: false
title: "Projects | Проекти"
subheadline: "Всі мої проекти"
header:
   image_fullwidth: "projects_header.jpg"
permalink: "/projects/"
---

<ul>
    {% for post in site.categories.projects %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
