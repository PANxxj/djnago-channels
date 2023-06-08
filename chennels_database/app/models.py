from django.db import models

class Group(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name
    
class Chat(models.Model):
    group=models.ForeignKey(Group,models.CASCADE,null=True,blank=True)
    content=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now_add=True)
