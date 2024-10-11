from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    catagory = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title
    
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_images')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        # Call the original save() method
        super().save(*args, **kwargs)
        
        # Open the uploaded image
        img = Image.open(self.image.path)
        
        # Resize the image if it is too large
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)