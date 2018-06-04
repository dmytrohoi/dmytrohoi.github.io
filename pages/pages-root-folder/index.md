---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image:  "index_header.jpg"
  pattern:  "pattern_stars.jpg"
widget1:
  title: "Blog | Блог"
  url: '/blog/'
  image: widget-1-302x182.png
  text: 'Кожен має свою думку і якщо думка кожного окремо стосується чогось більш персонального - вона має бути виражена.<br/> Це саме про це.'
widget2:
  title: "Projects | Проекти"
  url: '/projects/'
  image: widget-2-302x182.png
  text: 'Справжню роботу можна оцінити лише кейсами.<br/>Ось вони - мої кейси.<br/><i>Звісно, стосується відкритих для доступу</i>'
widget3:
  title: "About | Про мене"
  url: '/info/'
  image: widget-3-302x182.png
  text: 'Інформація про мене. </br> Все що стосується моєї персони.</br>Що почитати мого, що подивитись мого, що цікавого про мене є.</br>'
#
#  video: '<a href="#" data-reveal-id="videoModal"><img src="http://phlow.github.io/feeling-responsive/images/start-video-feeling-responsive-302x182.jpg" width="302" height="182" alt=""/></a>'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https://tinyletter.com/dmytrohoi
  text: Subscribe | Підписатись ›
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

<!-- <div id="videoModal" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/3b5zCFSmVvU" frameborder="0" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div> -->
