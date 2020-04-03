#!/bin/bash
heroku apps:create satelite-noticias
heroku git:remote --app satelite-noticias
heroku buildpacks:add --index 1 heroku/nodejs
heroku buildpacks:add --index 2 heroku/python
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DJANGO_SETTINGS_MODULE=backend.settings.prod
heroku config:set DJANGO_SECRET_KEY='-yfc1z9s0xhz=iy5$qp5hn%bmv0*04+jgzx-xp2*js$)4c=h-*'
git push heroku

