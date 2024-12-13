from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    
    # retourn le nom de l'autheur au lieu de l'objet au moment de choisir un autheur dans l'ajout d'un livre
    def __str__(self):
        return self.name
    
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')