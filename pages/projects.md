---
layout: page-fullwidth
show_meta: false
title: "Проекти"
subheadline: "Інформація про мої проекти"
header:
   image_fullwidth: "projects_header.jpg"
permalink: "/projects/"
---
<!-- SIDEBAR -->

<div class="row">
<div class="medium-4 medium-push-8 columns" markdown="1">
<div class="panel radius" markdown="1">
<details>
    <h3>Класифікація:</h3>
Задачі
:


</details>
<a class="radius button small" href="{{ site.url }}{{ site.baseurl }}/blog/">Блог</a>
<a class="radius button small" href="{{ site.url }}{{ site.baseurl }}/contact/">Зв'язатись</a>
</div>
</div>

<!-- CONTENT -->
<div class="medium-8 medium-pull-4 columns" markdown="1">

<ul>
    {% for post in site.categories.projects %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>

</div>
</div>
