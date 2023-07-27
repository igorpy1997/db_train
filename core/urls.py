"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import include, path
from application.views import (
    BookInfoView,
    AuthorInfoView,
    StorePrintView,
    PublisherInfoView,
    StoresListView,
    AuthorsListView,
    BooksPrintView,
    PublishersListView,
    MainPageView,
    remind_me,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    register_user,
)
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("book_info/<int:book_id>/", BookInfoView.as_view(), name="book-info"),
    path("author_info/<int:author_id>/", AuthorInfoView.as_view(), name="author-info"),
    path("store_print/<int:store_id>/", StorePrintView.as_view(), name="store-print"),
    path("publisher_info/<int:publisher_id>/", PublisherInfoView.as_view(), name="publisher-info"),
    path("stores/", StoresListView.as_view(), name="store-list"),
    path("authors_list/", AuthorsListView.as_view(), name="authors-list"),
    path("books_print/", BooksPrintView.as_view(), name="books-print"),
    path("publishers_list/", PublishersListView.as_view(), name="publishers-list"),
    path("main/", MainPageView.as_view(), name="main"),
    path("admin/", admin.site.urls),
    path("remind_me/", remind_me, name="remind-me"),
    path("books_create/", BookCreateView.as_view(), name="book-create"),
    path("books_update/<int:pk>/", BookUpdateView.as_view(), name="book-update"),
    path("books_delete/<int:pk>/", BookDeleteView.as_view(), name="book-delete"),
    path("accounts/login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("accounts/register/", register_user, name="register"),
    path("logout/", LogoutView.as_view(next_page="main"), name="logout"),
]
