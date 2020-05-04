# bookmarks/urls.py
from django.urls import path
from bookmarks.views import BookmarkListView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='BookmarkListView'),
]
