from django.conf import settings
from django.db import models
from django.utils import timezone

    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Clue(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    length = models.CharField(max_length=15)

    def __str__(self):
        return self.text
    
    def publish(self):
        self.save()  

class Solution(models.Model):
    clue_type = models.CharField(max_length=200, default="None")
    solution = models.CharField(max_length=200, default="None")
    confidence = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __init__(self, clue_type, solution, confidence):
        self.clue_type = clue_type
        self.solution = solution 
        self.confidence = confidence 

    def __str__(self):
        return self.solution 
    
    def get_type(self):
        return self.clue_type

    def publish (self):
        self.save()



        
