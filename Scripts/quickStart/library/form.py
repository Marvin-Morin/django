from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthdate']
        widgets = {
            'name': forms.TextInput(attrs={"type": "text"}),
            'birthdate': forms.DateInput(attrs={"type": "date"})
        }
        labels = {
            'name': 'Nom',
            'birthdate': 'Date de naissance'
        }
        
        
        
class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        
        fields = ['title', 'published', 'author']
        
        widgets = {
            'title': forms.TextInput(attrs = { "type" : "text" }),
            'published' : forms.DateInput(attrs = { 'type' : 'date' }),
            'author': forms.Select(attrs={'class': 'authors-dropdown'}),
        }
        
        labels = {
            'title' : 'Titre du livre :',
            'published' : 'Date de publication :',
            'author' : 'Auteur du livre :'
        }
        
        

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")
