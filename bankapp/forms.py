from django.forms import ModelForm
from django import forms
from .models import CustomUser,Account
class UserRegistrationForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields=["first_name","last_name","address","phone","username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class AccountCreationForm(ModelForm):
    account_number = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model=Account
        fields=["account_number","balance","account_type","user","active_status"]

class TransactionCreateForm(forms.Form):
    user = forms.CharField()
    to_account_number = forms.CharField()
    confirm_account_number = forms.CharField()
    amount = forms.CharField(max_length=5)
    remarks = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        to_account_number = cleaned_data.get("to_account_number")
        confirm_account_number = cleaned_data.get("confirm_account_number")
        amount = cleaned_data.get("amount")
        user = cleaned_data.get("user")

        # check the given account number is valid or not
        try:
            account = Account.objects.get(account_number=to_account_number)
        except:
            msg = "Invalid account number"
            self.add_error("to_account_number", msg)
        if to_account_number != confirm_account_number:
            msg = "Account number mismatch"
            self.add_error("to_account_number", msg)
        account = Account.objects.get(user__username=user)
        aval_bal = account.balance
        if float(amount) > aval_bal:
            message = ("Insufficient Balance")
            self.add_error("amount", message)
