from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Post
 
 
class CustomForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'created')
        widgets = {
            'created': AdminDateWidget(),
        }