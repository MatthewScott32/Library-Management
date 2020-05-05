from django.urls import path, include
from .views import *
from django.urls import path


app_name = "libraryapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('librarians/', librarians_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('library/form', library_form, name='library_form'),
    path('libraries/<int:library_id>/', library_details, name='library'),
]