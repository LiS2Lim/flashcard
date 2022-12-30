from django.db import models

# Flash card table
class Flash(models.Model):
    key=models.CharField(max_length=30)
    answer=models.TextField()
    tags=models.ManyToManyField('Tag')
    created_at=models.DateField(auto_now_add=True)
    count=models.IntegerField(default=0)

    def __str__(self):
        return self.key

# Tags table
class Tag(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
