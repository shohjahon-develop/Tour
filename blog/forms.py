from django import forms
from blog.models import *


class Your_emailForms(forms.ModelForm):


    class Meta:
        model = Your_email
        fields = "__all__"
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
