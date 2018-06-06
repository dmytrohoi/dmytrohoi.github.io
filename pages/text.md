---
layout: page-fullwidth
show_meta: false
title: "Текст"
header:
   image_fullwidth: "text_header.png"
permalink: "/text/"
---

<!-- SIDEBAR -->

<div class="row">
<div class="medium-4 medium-push-8 columns" markdown="1">
<div class="panel radius" markdown="1">
<div align="center"><h3>Опис</h3></div>
В цьому розділі мова йде про <b>текстові</b> проекти, а саме

Прозові твори
:  Вцілому - книжки написані мною або за моєї участі.

Статті
:  Великі матеріали на певні теми, які мають повний цикл.

Дописи
:  Короткі дописи в основі яких - вираження своєї позиції. Зазвичай, на тему певної послідовності (систематизації) дій.


<div align="center"><h3>Мої посилання</h3></div>
<div align="center">
<p><a href="https://dmytrohoi.github.io/"><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/st.png"></a> <a href="https://fb.com/dmytro.hoi"><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/fb.png"></a><a href="https://github.com/dmytrohoi"  ><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/gh.png"></a><a href="https://twitter.com/criticoffer"  ><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/tw.png"></a></p>
<p><a href="https://dmytrohoi.github.io/cv"  ><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/cv.png"></a> <a href="https://www.linkedin.com/in/dmytrohoi"  ><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/li.png"></a><a href="https://instagram.com/dmhoi78"  ><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/insta.png"></a><a href="https://youtube.com/channel/UCOOftc_XjycxIsDbWsoBFtA"  ><img style="vertical-align: sub !important;" src="https://dmytrohoi.github.io/images/social/yt.png"></a></p>
</div>

<div align="center"><i>Більше дописів - на Facebook та в Twitter..</i></div>

</div>
</div>

<!-- CONTENT -->
<div class="medium-8 medium-pull-4 columns" markdown="1">

<ul>
    {% for post in site.categories.text %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      <i>{{ post.excerpt }}</i>
      <div align="center">{{ posts.tags }}</div>
    </li>
    {% endfor %}
</ul>

</div>
</div>
