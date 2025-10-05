from django.contrib.auth.models import AbstractUser
from django.db import models
import os
import uuid

def user_avatar_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join("avatars",str(instance.id), filename)


class CustomUser(AbstractUser): # models.Model
    avatar = models.ImageField(
        upload_to=user_avatar_path,
        default="avatars/default.png",
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Usuario: {self.username}"
