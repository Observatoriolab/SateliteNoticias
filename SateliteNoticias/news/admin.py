from django.contrib import admin
from news.models import Edition, News,Comment
# Register your models here.

admin.site.register(Edition)
admin.site.register(News)
admin.site.register(Comment)