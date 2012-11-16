from django import forms


class LoginForm(forms.Form):
  username = forms.CharField(label=(u"Gebruikersnaam"))
  password = forms.CharField(label=(u"Wachtwoord"), widget=forms.PasswordInput(render_value=False))
