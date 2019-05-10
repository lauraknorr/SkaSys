from django import forms

class TodoForm(forms.Form):
    titel = forms.CharField(label='titel', max_length=15)
    beschreibung = forms.CharField(widget = forms.Textarea)
    tag = forms.ChoiceField(label="tag", initial='', widget=forms.Select(), required=True)
    monat = forms.ChoiceField(label="monat", initial='', widget=forms.Select(), required=True)
    jahr = forms.ChoiceField(label="jahr", initial='', widget=forms.Select(), required=True)
