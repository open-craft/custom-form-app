from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    pass

    class Meta(object):
        model = ExtraInfo
        fields = ('favorite_editor', 'favorite_movie')
