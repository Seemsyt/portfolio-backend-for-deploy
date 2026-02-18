from django.db import models

# Create your models here.
class Pricing(models.Model):
    title = models.CharField(max_length=200)
    is_admin = models.CharField(max_length=200)
    price = models.IntegerField()
    slug = models.SlugField(max_length=200)
    feature_1 = models.CharField(max_length=200)
    feature_2 = models.CharField(max_length=300,blank=True)
    feature_3 = models.CharField(max_length=300,blank=True)
    feature_4 = models.CharField(max_length=300,blank=True)
    feature_5 = models.CharField(max_length=300,blank=True)
    feature_6 = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    sent_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/%Y/%d')
    discription = models.TextField()
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title