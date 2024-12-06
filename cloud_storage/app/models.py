from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Files(models.Model):
    dis=models.TextField()
    file=models.FileField()
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    @property
    def file_name(self):
        return os.path.basename(self.file.name)

    @property
    def file_extension(self):
        return os.path.splitext(self.file.name)[1]


    