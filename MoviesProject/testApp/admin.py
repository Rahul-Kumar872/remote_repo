from django.contrib import admin
from testApp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['Rdate','Moviename','Hero','Heroine','Rating']
admin.site.register(Movie,MovieAdmin)
