from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('titel', 'beschreibung','tag', 'monat', 'jahr', 'status')

    DAYS = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
        (11,'11'),
        (12,'12'),
        (13,'13'),
        (14,'14'),
        (15,'15'),
        (16,'16'),
        (17,'17'),
        (18,'18'),
        (19,'19'),
        (20,'20'),
        (21,'21'),
        (22,'22'),
        (23,'23'),
        (24,'24'),
        (25,'25'),
        (26,'26'),
        (27,'27'),
        (28,'28'),
        (29,'29'),
        (30,'30'),
        (31,'31'),
    )
    MONTHS = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
        (11,'11'),
        (12,'12'),
    )
    YEARS = (
        (2019,'2019'),
        (2020,'2020'),
        (2021,'2021'),
        (2022,'2022'),
        (2023,'2023'),
        (2024,'2024'),
        (2025,'2025'),
        (2026,'2026'),
        (2027,'2027'),
        (2028,'2028'),
        (2029,'2029'),
    )
    titel = forms.CharField(label='Titel', max_length=15)
    beschreibung = forms.CharField(label = 'Beschreibung', widget = forms.Textarea, max_length = 160)
    tag = forms.ChoiceField(label="Tag", choices = DAYS, required=True)
    monat = forms.ChoiceField(label="Monat", choices = MONTHS, required=True)
    jahr = forms.ChoiceField(label="Jahr", choices = YEARS, required=True)
    status = forms.IntegerField(label = "Status", required = False)
