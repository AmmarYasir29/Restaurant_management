from django.db import models

# Create your models here.


class UserR(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
        return self.firstname + self.lastname
