from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    '''модель расширяющая таблицу User'''
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)




    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)