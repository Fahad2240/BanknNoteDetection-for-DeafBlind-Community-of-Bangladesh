from django import forms
from .models import realtimeimg
from django.db import models
# from .Detection import models
FROM_INPUT_CLASSES='w-full px-5 py-3 rounded-xl border'
class Selectpic(forms.ModelForm):
    image = models.ImageField(upload_to='Detect_images')
    # server_key = forms.CharField(max_length=100)
    class Meta:
        model=realtimeimg
        fields=('image',)
        widgets={
            'image':forms.FileInput(attrs={'class':FROM_INPUT_CLASSES})
        }