from django import forms
from stocks.models import Post

class HomeForm(forms.Form):
    post = forms.CharField()

    class Meta:
        model = Post
        fields = ('post',)
