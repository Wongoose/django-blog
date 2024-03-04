from django import forms
from . import models

# creating our own form class
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["title", "body", "slug", "thumb"]
