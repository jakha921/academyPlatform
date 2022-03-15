from django import forms

from .models import User

class SignUpForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'placeholder': '*******',     
                },
    ))
    confirm_password=forms.CharField(widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'placeholder': '*******',     
                },
    ))
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'password' ]
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',                
                }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'support@themezhub.com',                
                }),
        }
        
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )



# <input type="text" class="form-control" placeholder="support@themezhub.com" />
# <input type="text" class="form-control" placeholder="*******" />
