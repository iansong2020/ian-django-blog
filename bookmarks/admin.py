from django.contrib import admin
from bookmarks.models import Bookmark

# Register your models here.
class BookmarksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Bookmark, BookmarksAdmin)
