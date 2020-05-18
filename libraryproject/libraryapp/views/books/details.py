import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
from libraryapp.models import model_factory
from ..connection import Connection


def get_book(book_id):
    
    return Book.objects.get(pk=book_id)
    
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = create_book
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         b.id book_id,
    #         b.title,
    #         b.isbn,
    #         b.author,
    #         b.year_published,
    #         b.publisher,
    #         b.librarian_id,
    #         b.location_id,
    #         li.id librarian_id,
    #         u.first_name,
    #         u.last_name,
    #         loc.id library_id,
    #         loc.title library_name
    #     FROM libraryapp_book b
    #     JOIN libraryapp_librarian li ON b.librarian_id = li.id
    #     JOIN libraryapp_library loc ON b.location_id = loc.id
    #     JOIN auth_user u ON u.id = li.user_id
    #     WHERE b.id = ?
    #     """, (book_id,))

        # return db_cursor.fetchone()

@login_required
def book_details(request, book_id):
    if request.method == 'GET':
        book = get_book(book_id)
        
        template_name = 'books/detail.html'
        context = {
            'book': book
        }

        return render(request, template_name, {'book': book})

    if request.method == 'POST':
        form_data = request.POST


    # elif request.method == 'POST':
    #     form_data = request.POST

        # if (
        #     "actual_method" in form_data
        #     and form_data["actual_method"] == "PUT"
        # ):
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            book_to_delete = get_book(book_id)
            book_to_delete.delete()
            
            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #     UPDATE libraryapp_book
            #     SET title = ?,
            #         author = ?,
            #         isbn = ?,
            #         publisher = ?,
            #         year_published = ?,
            #         location_id = ?
            #     WHERE id = ?
            #     """,
            #     (
            #         form_data['title'], form_data['author'],
            #         form_data['isbn'], form_data['publisher'], form_data['year_published'],
            #         form_data["location"], book_id,
            #     ))

            return redirect(reverse('libraryapp:books'))

        # if (
        #     "actual_method" in form_data
        #     and form_data["actual_method"] == "DELETE"
        # ):
        #     with sqlite3.connect(Connection.db_path) as conn:
        #         db_cursor = conn.cursor()

        #         db_cursor.execute("""
        #             DELETE FROM libraryapp_book
        #             WHERE id = ?
        #         """, (book_id,))
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            book_to_update = get_book(book_id)

            book_to_update.title = form_data['title']
            book_to_update.author = form_data['author']
            book_to_update.isbn = form_data['isbn']
            book_to_update.year_published = form_data['year_published']
            book_to_update.publisher = form_data['publisher']
            book_to_update.location_id = form_data['location']

            book_to_update.save()

            return redirect(reverse('libraryapp:books'))
        
# def create_book(cursor, row):
#     _row = sqlite3.Row(cursor, row)

#     book = Book()
#     book.id = _row["book_id"]
#     book.author = _row["author"]
#     book.isbn = _row["isbn"]
#     book.title = _row["title"]
#     book.publisher = _row["publisher"]
#     book.year_published = _row["year_published"]

#     librarian = Librarian()
#     librarian.id = _row["librarian_id"]
#     librarian.first_name = _row["first_name"]
#     librarian.last_name = _row["last_name"]

#     library = Library()
#     library.id = _row["library_id"]
#     library.title = _row["library_name"]

#     book.librarian = librarian
#     book.location = library

#     return book