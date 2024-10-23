from django import forms

class VoteForm(forms.Form):
    OPTIONS = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
    ]
    choice = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)
