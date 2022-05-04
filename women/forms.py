# sendemail/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Women


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='About', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = "__all__"


class BeastForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'
# Тег <label> устанавливает связь между определенной
# меткой, в качестве которой обычно выступает текст, и элементом формы
# (<input>, <select>, <textarea>). Такая связь необходима, чтобы изменять значения элементов формы при нажатии курсором мыши на текст.


#  required часто используется для того,
# чтобы сделать поле необязательным, то есть пользователю больше не нужно будет вводить данные в это поле, и оно все равно будет принято.
