from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self): # the save method is automatically run whenever the model is saved,
        # but we are adding features, so will need to access it ourselves
        super().save()

        img = Image.open(self.image.path)
        
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            if img.height > img.width:
                diff = img.height - img.width
                #crop(left, upper, right, lower)
                img = img.crop((0, diff/2, img.width, img.height-diff/2))
            else:
                diff = img.width - img.height
                img = img.crop((diff/2, 0, img.width-diff/2, img.height))
            
            img.thumbnail(output_size)
            img.save(self.image.path)