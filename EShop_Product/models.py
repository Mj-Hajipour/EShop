import os
from django.db import models

# Create your models here.
def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name=f"{instance.id}_{instance.title}{ext}"
    return f"products/{final_name}"

class Product(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.title