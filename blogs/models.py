from django.db import models
import uuid

# Create your models here.

class Blog(models.Model):
    # owner = models.ForeignKey(
    # Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.featured_image.url
    #     except:
    #         url = ''
    #     return url

class Comments(models.Model):
    id = models.UUIDField(Blog, primary_key=True ,unique=True, editable= False)
    title = models.CharField(max_length=200)
    comment = models.TextField(null=False, blank= False, max_length= 1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title