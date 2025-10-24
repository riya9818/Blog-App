
from django import forms

from blog_app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields={"title","content"}



class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
