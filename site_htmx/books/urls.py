from django.urls import path
from .views import book_list, create_book


urlpatterns = [
    path("", book_list, name="book_list"),
    path("create_book/", create_book, name="create_book"),
]
