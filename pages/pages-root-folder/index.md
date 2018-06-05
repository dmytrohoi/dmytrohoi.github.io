---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image:  "index_header.png"
  pattern:  "pattern_stars.png"
widget1:
  title: "Проекти"
  url: '/projects/'
  image: widget-1-302x182.png
  text: 'Справжню роботу можна оцінити лише кейсами.</br>Ось вони - мої кейси.</br>'
widget2:
  title: "Текст"
  url: '/text/'
  image: widget-2-302x182.png
  text: 'Написання прози та статей на різні теми - одне з небагатьох філософських занять сьогодення. Окремо варто зазначити, що твори та дописи написані не філологом, але з їх допомоги.'
widget3:
  title: "Про мене"
  url: '/info/'
  image: widget-3-302x182.png
  text: 'Інформація про мене. </br> Все що стосується моєї персони.</br></br>Що почитати мого, що подивитись мого, що цікавого про мене є.'
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
  text: Підписатись ›
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---
