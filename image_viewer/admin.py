from django.contrib import admin
from .models import Editor, Image, Category, Tag, Location, Comment, NewsLetterRecipients



class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category','tag', 'location', 'comment' )



admin.site.register(Editor)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(NewsLetterRecipients)



