from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(initial="")
    # message = forms.CharField(widget=forms.Textarea)
    # note = forms.CharField()

    def send_email(self):
        # TODO: Send contact email using the self.cleaned_data dictionary:
        print(self.cleaned_data)
        pass


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def sign_in(self):
        # TODO: Login in the user
        print("Loging in user")
        print(self.cleaned_data)
        pass
