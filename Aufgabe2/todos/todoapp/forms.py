from django import forms

class TodoForm(forms.Form):
    titel = forms.CharField(label='titel', max_length=15)
    beschreibung = forms.CharField(widget = forms.Textarea)
    tag = forms.Choices()
    monat = forms.Choices()
    jahr = forms.Choices()

    
