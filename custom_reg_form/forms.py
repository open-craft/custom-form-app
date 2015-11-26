from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['favorite_movie'].error_messages = {
            "required": u"Please tell us your favorite movie.",
            "invalid": u"We're pretty sure you made that movie up.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('favorite_editor', 'favorite_movie')
