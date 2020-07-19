from django import forms



class form_delete_account(forms.Form):
    username = forms.CharField(label="",
        widget=forms.TextInput(attrs={'placeholder': 'type your username'}))
