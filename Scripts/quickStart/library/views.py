from django.shortcuts import get_object_or_404, redirect, render
from .models import Author, Book
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.views.generic import View, DetailView
from .form import AuthorForm, BookForm
from django.contrib import messages
from .form import SignInForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .mixins import PostPermissionMixin
import tkinter as tk
from django.views.generic.edit import FormMixin


# CBV Class base view
class AuthorsView(LoginRequiredMixin, View):

    def get(self, request : HttpRequest) -> HttpResponse:
        
        form = AuthorForm()
    
        
        return render(
            request,
            'authors.html',
            {'authors' : Author.objects.all(), 'form' : form },
            )


    def post(self, request: HttpRequest)->HttpResponse:
        
        if request.POST.get("_method") == "delete":
            return self.delete(request)
        
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = AuthorForm()
        
        messages.error(request, "Error in the form")
        
        return render(
            request,
            'authors.html',
            { 'authors': Author.objects.all(), 'form': form },
        )
    
    
    def delete(self, request: HttpRequest) -> HttpResponse:
    
        try:
            
            author = Author.objects.get(id=request.POST.get('id'))
            author.delete()
        
        except Author.DoesNotExist:
            raise Http404("Author does not exist")
        
        return HttpResponseRedirect(redirect_to='/authors')



class AuthorDetail(DetailView, FormMixin, LoginRequiredMixin ):
    model = Author
    template_name = 'detail-author.html'
    context_object_name = 'author'
    form_class = AuthorForm


    def post(self, request):
        
        """Gérer la soumission du formulaire pour modifier l'auteur"""
        
        author = self.get_object()
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Auteur modifié avec succès !")

            return redirect('detail-author', pk=author.pk)


            
        else:
            messages.error(request, "Erreur lors de la modification.")
            return render(
                request,
                self.template_name,
                {'author': author, 'form': form},
            )
            
    def get_context_data(self, **kwargs):
        # Pré-remplir le formulaire avec les données de l'auteur
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorForm(instance=self.get_object())
        return context



@login_required
def authorDetail(request : HttpRequest, authorId: int) -> HttpResponse:

    try:
        
        author = Author.objects.get(id = authorId)
        
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = AuthorForm()
        
    except Author.DoesNotExist:
            raise Http404('Author does not exists !')
    return render (
        request,
        'detail-author.html',
        { 'author': author, 'form' : form }
    )





class BooksView(PostPermissionMixin, View):
    
    def get(self, request: HttpRequest)->HttpResponse:
        
        form = BookForm()
        
        return render(
            request,
            'books.html',
            { 'form': form, 'books': Book.objects.all() },
        )


    def post(self, request: HttpRequest)->HttpResponse:
        
        if request.POST.get('_method') == 'delete':
            return self.delete(request)
        
        form = BookForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = BookForm()
            
        return render(
            request,
            'books.html',
            { 'form': form, 'books': Book.objects.all() },
        )


    def delete(self, request: HttpRequest) -> HttpResponse:
        
        try:
            book = Book.objects.get(id=request.POST.get('id'))
            book.delete()
        
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        return HttpResponseRedirect(redirect_to='/books')
    

class BookDetail(DetailView):
    
    model = Book
    template_name = 'detail-book.html'
    context_object_name = 'book'
    
# Detail d'un livre
@login_required
def bookDetail(request: HttpRequest, primaryKey: int) -> HttpResponse:
    
    try:
        book = Book.objects.get(id = primaryKey)
        
    except Book.DoesNotExist:
        raise Http404('Book does not exists !')
    return render(
        request,
        'detail-book.html',
        { 'book' : book}
    )