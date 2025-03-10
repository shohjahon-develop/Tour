from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


# Create your models here.

class Category_of_Offres(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Tips(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="index/img")
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name






class Direct(models.Model):
    img = models.ImageField(upload_to="index/img")
    name = models.CharField(max_length=50)
    rating = models.FloatField()
    offer = models.ForeignKey(Category_of_Offres,on_delete=models.CASCADE)
    price = models.FloatField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return str(self.location)


class Your_email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Food(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="index/img")
    text = models.TextField(blank=True)
    slug = models.SlugField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("foodDetail", args=[self.slug])


class Medical(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to="index/img")
    text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Services(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to="index/img")
    text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Shopping(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to="index/img")
    text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to="index/img")
    img2 = models.ImageField(upload_to="index/img")
    text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Automotive(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to="index/img")
    text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to="index/img")
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jobsDetail", args=[self.slug])


class Comment(models.Model):
    tips = models.ForeignKey(Tips, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tips.name}"


class D_comment(models.Model):
    dir = models.ForeignKey(Direct, on_delete=models.CASCADE, related_name='comments_2')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    created_time = models.DateTimeField(default=now,null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.dir.name}"




















