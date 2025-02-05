from django.db import models

class Book(models.Model):
    
    categories = [
        ('Novels','Novels'),
        ('Short Stories','Short Stories'),
        ('Romance','Romance'),
        ('Fantasy','Fantasy'),
        ('Educational','Educational'),
        ('Kids','Kids'),
    ]
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(max_length=250,choices=categories)
    author = models.CharField(max_length=250)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    