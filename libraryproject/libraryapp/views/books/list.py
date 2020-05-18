import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def book_list(request):
    if request.method == 'GET':
        all_books = Book.objects.all()
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     conn.row_factory = model_factory(Book)

        #     db_cursor = conn.cursor()
        #     db_cursor.execute("""
        #     select
        #         b.id,
        #         b.title,
        #         b.isbn,
        #         b.publisher,
        #         b.author,
        #         b.year_published,
        #         b.librarian_id,
        #         b.location_id
        #     from libraryapp_book b
        #     """)

        #     all_books = db_cursor.fetchall()

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        # new_book = Book()
        # new_book.title = form_data['title']
        # new_book.author = form_data['author']
        # new_book.isbn = form_data['isbn']
        # new_book.year_published = form_data['year_published']
        # new_book.librarian_id = request.user.librarian.id
        # # new_book.location_id = form_data['location']
        # library = Library.objects.get(pk=form_data['location'])
        # new_book.location = library
        # new_book.publisher = form_data['publisher']
        
        # new_book.save()
        
        new_book = Book.objects.create(
            title = form_data['title'],
            author = form_data['author'],
            isbn = form_data['isbn'],
            year_published = form_data['year_published'],
            librarian_id = request.user.librarian.id,
            location_id = form_data['location'],
            publisher = form_data['publisher']
        )

    # with sqlite3.connect(Connection.db_path) as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     INSERT INTO libraryapp_book
    #     (
    #         title, author, isbn, publisher,
    #         year_published, location_id, librarian_id
    #     )
    #     VALUES (?, ?, ?, ?, ?, ?, ?)
    #     """,
    #     (form_data['title'], form_data['author'],
    #         form_data['isbn'], form_data['publisher'], form_data['year_published'],
    #         request.user.librarian.id, form_data["location"]))

    return redirect(reverse('libraryapp:books'))