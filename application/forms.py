from django import forms


class ReminderForm(forms.Form):
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=200)
    reminder_datetime = forms.DateTimeField()
