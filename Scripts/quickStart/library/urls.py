from django.urls import path
from . import views

urlpatterns = [
    #Liste des Auteurs
    path('authors/', views.AuthorsView.as_view(), name='authors'),
    # Détail d'un auteur
    # path('author/<int:authorId>/', views.authorDetail),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='detail-author'),
    # Delete un auteur
    path('author/<int:primaryKey>/delete', views.AuthorsView.as_view(), name='delete-author'),

    # Liste d'un livre
    path('books/', views.BooksView.as_view(), name='books'),
    # Détail d'un livre
    path('book/<int:primaryKey>/detail', views.bookDetail),
    # Delete un livre
    path('books/<int:primaryKey>/delete', views.BooksView.as_view(), name='delete-author'),
]