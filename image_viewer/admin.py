from django.contrib import admin
from .models import Editor, Image, Category, Tag



class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category','tag')



admin.site.register(Editor)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(Tag)



