from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.TextField()
    ratting=models.FloatField()
    m_format=models.TextField()
    duration=models.TextField()
    genre=models.TextField()
    r_date=models.DateField()
    cover_image=models.FileField()
    cover_image1=models.FileField()
    main_image=models.FileField()
    def __str__(self):
        return self.name
class member(models.Model):
    type=models.TextField()
    name=models.TextField()
    role=models.TextField()
    photo=models.FileField()
    def __str__(self):
        return self.name
class language(models.Model):
    language=models.TextField()
    movie_name=models.ForeignKey(movie,on_delete=models.CASCADE)
