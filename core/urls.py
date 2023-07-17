"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from application import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("book_info/<int:book_id>/", views.book_info, name="book-info"),
    path("author_info/<int:author_id>/", views.author_info, name="author-info"),
    path("store_print/<int:store_id>/", views.store_print, name="store-print"),
    path("publisher_info/<int:publisher_id>/", views.publisher_info, name="publisher-info"),
    path("stores/", views.stores_list, name="store-list"),
    path("authors_list/", views.authors_list, name="authors-list"),
    path("books_print/", views.books_print, name="books-print"),
    path("publishers_list/", views.publishers_list, name="publishers-list"),
    path("main/", views.main_page, name="main"),
    path("admin/", admin.site.urls),
    path("remind_me/", views.remind_me, name="remind-me"),
]
