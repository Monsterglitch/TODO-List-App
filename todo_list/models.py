from django.db import models

class List(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing integer field
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item