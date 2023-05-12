
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import BookList, BookSearch, BookUpdate, BookView, BookDelete

router = routers.DefaultRouter()
router.register('books', BookView)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='books'),
    path('books/search/', BookSearch.as_view(), name='book-search'),
    path('books/<int:id>/update/', BookUpdate.as_view(), name='book-update'),
    path('books/<int:id>/delete/', BookDelete.as_view(), name='book-delete'),
]
