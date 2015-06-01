from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.base_fields['username'].widget.attrs['class'] = 'form-control'
        self.base_fields['password'].widget.attrs['class'] = 'form-control'
