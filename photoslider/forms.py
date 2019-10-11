from django.forms import ModelForm
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['secondname', 'age', 'country', 'email', 'programming_language', 'payment']
        