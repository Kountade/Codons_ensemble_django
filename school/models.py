from django.db import models

from django.contrib.auth.models import User



class Teacher(models.Model):
    name = models.CharField( max_length=200,)
    description = models.TextField()
    image = models.ImageField( upload_to='teachers/', blank=True, null=True, verbose_name="Image de l'événement" )
   
    def __str__(self):
        return self.name
    
    
class Program(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre du programme") 
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    image = models.ImageField(upload_to='programs/', blank=True, null=True, verbose_name="Image du programme")
    seats = models.PositiveIntegerField(default=30, verbose_name="Nombre de places disponibles")
    lessons = models.PositiveIntegerField(default=0, verbose_name="Nombre de leçons")
    hours = models.PositiveIntegerField(default=0, verbose_name="Nombre d'heures totales")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)  # Correction de "blanc" à "blank"
    
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField( max_length=200,)
    description = models.TextField()
    date = models.DateTimeField(verbose_name="Date et heure de début" )
    time_from = models.TimeField()
    time_to = models.TimeField()
    location = models.CharField(  max_length=200,verbose_name="Lieu de l'événement")
    image = models.ImageField( upload_to='events/', blank=True, null=True, verbose_name="Image de l'événement" )

    def __str__(self):
        return self.title



class Student(models.Model):
    name = models.CharField( max_length=100,)
    subject = models.CharField( max_length=100)
    image = models.ImageField(upload_to="students/")
    grade_level = models.CharField( max_length=50,)
    
  

    def __str__(self):
        return self.name

  
class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grades")
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.user.username} - {self.mark}"
    
    
class FeedBackUser(models.Model):  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    
    def __str__(self):
        return self.name

    
class Review(models.Model):
    user = models.ForeignKey(FeedBackUser, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Ajoutez auto_now_add=True
    
    def __str__(self):
        return f"{self.user.name} - {self.program.title}"  # Correction : user.name au lieu de user.username
    
    
class Testimonial(models.Model):
    RATING_CHOICES = [
        (1, '1 étoile'),
        (2, '2 étoiles'),
        (3, '3 étoiles'),
        (4, '4 étoiles'),
        (5, '5 étoiles'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(verbose_name="Témoignage")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.rating}/5"
    
    def get_rating_stars(self):
        """Retourne le rating sous forme d'étoiles"""
        return '★' * self.rating + '☆' * (5 - self.rating)