from django.forms import ModelForm
from .models import *
from django import forms
  
  
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class SearchForm(forms.Form):
    field = forms.ModelChoiceField(queryset=Entry.objects.all().order_by('name'))