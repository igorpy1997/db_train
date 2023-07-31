from django.shortcuts import render, redirect
from application.models import Store, Book, Publisher, Author
from django.db.models import Count
from application.forms import ReminderForm
from application.tasks import reminder
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .mixins import PaginatedCacheMixin


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


class MainPageView(TemplateView):
    template_name = "main_page.html"


class StoresListView(ListView):
    model = Store
    template_name = "stores_list.html"
    context_object_name = "stores"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stores = self.object_list
        count = stores.aggregate(count=Count("id"))["count"]
        context["count"] = count
        return context


class AuthorsListView(ListView):
    model = Author
    template_name = "authors_list.html"
    context_object_name = "authors"


class StorePrintView(DetailView):
    model = Store
    template_name = "store_print.html"
    context_object_name = "store"
    pk_url_kwarg = "store_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        store = self.object
        books_count = store.books.count()
        books = store.books.prefetch_related("authors")
        store_authors = Author.objects.filter(book__in=books).distinct()
        context["books"] = books
        context["store_authors"] = store_authors
        context["books_count"] = books_count
        return context


class BooksPrintView(PaginatedCacheMixin, ListView):
    model = Book
    template_name = "books_list.html"
    context_object_name = "books"
    paginate_by = 100


class BookInfoView(DetailView):
    model = Book
    template_name = "book_info.html"
    context_object_name = "book"
    pk_url_kwarg = "book_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        authors = book.authors.prefetch_related()
        publisher = book.publisher
        context["authors"] = authors
        context["publisher"] = publisher
        return context


class AuthorInfoView(DetailView):
    model = Author
    template_name = "author_info.html"
    context_object_name = "author"
    pk_url_kwarg = "author_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        author_books = author.book_set.all().prefetch_related("authors", "publisher__book_set__authors")
        publishers = {book.publisher for book in author_books}
        context["author_books"] = author_books
        context["publishers"] = publishers
        return context


class PublishersListView(ListView):
    model = Publisher
    template_name = "publishers_list.html"
    context_object_name = "publishers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publishers = self.object_list
        sum_books = publishers.aggregate(sum_books=Count("book"))["sum_books"]
        context["sum_books"] = sum_books
        return context


class PublisherInfoView(DetailView):
    model = Publisher
    template_name = "publisher_info.html"
    context_object_name = "publisher"
    pk_url_kwarg = "publisher_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publisher = self.object
        publisher_books = publisher.book_set.prefetch_related("authors", "publisher__book_set__store_set")
        publisher_authors = {author for book in publisher_books for author in book.authors.all()}
        publisher_stores = {store for book in publisher_books for store in book.store_set.all()}
        context["publisher_books"] = publisher_books
        context["publisher_authors"] = publisher_authors
        context["publisher_stores"] = publisher_stores
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "book_create.html"
    fields = "__all__"
    success_url = reverse_lazy("books-print")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "book_update.html"
    fields = "__all__"
    success_url = reverse_lazy("books-print")


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("books-print")


def remind_me(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("message")
            reminder_datetime = form.cleaned_data.get("reminder_datetime")
            email = form.cleaned_data.get("email")
            now = timezone.now()
            if reminder_datetime > now:
                reminder.apply_async(args=[message, email], eta=reminder_datetime)
            return redirect("main")
    else:
        form = ReminderForm()
    now = timezone.now()
    return render(request, "create_reminder.html", {"form": form, "now": now})
