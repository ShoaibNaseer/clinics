from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50, validators=[
        RegexValidator(
            regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$',
            message='Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit',
        ),
    ])
    is_active = models.BooleanField(default=True)