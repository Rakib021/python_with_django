from django.urls import path
# from book.views import home,store_book,show_books,edit_book,delete_book
from . import views

urlpatterns = [
    # path('',home,name="homepage"),
    path('<int:roll>/',views.MyTemplateView.as_view(template_name='home.html'),{'author':'rakib'}),
    # path('store_new_book/',views.store_book,name="storebook"),
    path('store_new_book/',views.BookFromView.as_view(),name="storebook"),
    # path('show_books/',views.show_books,name="showbook"),
    path('show_books/',views.BookListView.as_view(),name="showbook"),
    path('book_details/<int:id>/',views.BookDetailsView.as_view(),name="book_details"),
    path('edit_book/<int:id>',views.edit_book,name="edit_book"),
    path('delete_book/<int:id>',views.delete_book,name="delete_book"),
]
