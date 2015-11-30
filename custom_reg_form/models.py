from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
    FAVORITE_EDITOR = (
        ('vim', 'Vim'),
        ('emacs', 'Emacs'),
        ('np', 'Notepad'),
        ('cat', 'cat > filename'),
    )

    favorite_movie = models.CharField(
        verbose_name="Fav Flick",
        max_length=100,
    )
    favorite_editor = models.CharField(
        verbose_name="Favorite Editor",
        choices=FAVORITE_EDITOR,
        blank=True, 
        max_length=5,
    )
