from django.shortcuts import render, redirect
from application.models import Store, Book, Publisher, Author
from django.db.models import Count, Avg
from application.forms import ReminderForm
from application.tasks import reminder
from django.utils import timezone


def main_page(request):
    return render(request, "main_page.html")


def stores_list(request):
    stores = Store.objects.all()
    count = stores.aggregate(count=Count("id"))["count"]
    return render(request, "stores_list.html", {"stores": stores, "count": count})


def store_print(request, store_id):
    store = Store.objects.get(id=store_id)
    books_count = (
        Store.objects.filter(id=store_id).annotate(num_books=Count("books")).values("num_books").first()["num_books"]
    )
    books = store.books.prefetch_related("authors")
    store_authors = Author.objects.filter(book__in=books).distinct()
    return render(
        request,
        "store_print.html",
        {"store": store, "books": books, "store_authors": store_authors, "books_count": books_count},
    )


def books_print(request):
    books = Book.objects.all()
    avg_price = books.aggregate(avg_price=Avg("price"))["avg_price"]
    return render(request, "books_list.html", {"books": books, "avg_price": avg_price})


def book_info(request, book_id):
    book = Book.objects.select_related("publisher").get(id=book_id)
    authors = book.authors.prefetch_related()
    publisher = book.publisher
    return render(request, "book_info.html", {"book": book, "authors": authors, "publisher": publisher})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, "authors_list.html", {"authors": authors})


def author_info(request, author_id):
    author = Author.objects.get(id=author_id)
    author_books = author.book_set.all().prefetch_related("authors", "publisher__book_set__authors")
    publishers = set(book.publisher for book in author_books)
    return render(
        request,
        "author_info.html",
        {
            "author_books": author_books,
            "author": author,
            "publishers": publishers,
        },
    )


def publishers_list(request):
    publishers = Publisher.objects.all()
    sum_books = publishers.aggregate(sum_books=Count("book"))["sum_books"]
    return render(request, "publishers_list.html", {"publishers": publishers, "sum_books": sum_books})


def publisher_info(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    publisher_books = publisher.book_set.prefetch_related("authors", "publisher__book_set__store_set")
    publisher_authors = set()
    for book in publisher_books:
        publisher_authors.update(book.authors.all())
    publisher_stores = set()
    for book in publisher_books:
        publisher_stores.update(book.store_set.all())
    return render(
        request,
        "publisher_info.html",
        {
            "publisher": publisher,
            "publisher_books": publisher_books,
            "publisher_authors": publisher_authors,
            "publisher_stores": publisher_stores,
        },
    )


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
