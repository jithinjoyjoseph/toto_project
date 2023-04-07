from django.db import models
#default django user model,user name ,email ,password.one to many idoms
from django.contrib.auth.models import User

# Create your models here.

#todoadmin
#jithinjoy98

class Task(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True ,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
