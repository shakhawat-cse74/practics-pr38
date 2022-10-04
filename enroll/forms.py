from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label='Password(Agian)', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valrepass = self.cleaned_data['repassword']

        if valpass != valrepass:
            raise forms.ValidationError('Password does not match')
