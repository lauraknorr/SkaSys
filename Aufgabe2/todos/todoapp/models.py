from django.db import models

# Create your models here.
class Todo(models.Model):
    DAYS = (
        (1,'one'),
        (2,'two'),
        (3,'three'),
        (4,'four'),
        (5,'five'),
        (6,'six'),
        (7,'seven'),
        (8,'eight'),
        (9,'nine'),
        (10,'ten'),
        (11,'eleven'),
        (12,'twelve'),
        (13,'thirteen'),
        (14,'fourteen'),
        (15,'fifteen'),
        (16,'sixteen'),
        (17,'seventeen'),
        (18,'eighteen'),
        (19,'nineteen'),
        (20,'twenty'),
        (21,'twenty-one'),
        (22,'twenty-two'),
        (23,'twenty-three'),
        (24,'twenty-four'),
        (25,'twenty-five'),
        (26,'twenty-six'),
        (27,'twenty-seven'),
        (28,'twenty-eight'),
        (29,'twenty-nine'),
        (30,'thirty'),
        (31,'thirty-one'),
    )
    MONTHS = (
        (1,'one'),
        (2,'two'),
        (3,'three'),
        (4,'four'),
        (5,'five'),
        (6,'six'),
        (7,'seven'),
        (8,'eight'),
        (9,'nine'),
        (10,'ten'),
        (11,'eleven'),
        (12,'twelve'),
    )
    YEARS = (
        (2019,'two-thousand-nineteen'),
        (2020,'two-thousand-twenty'),
        (2021,'two-thousand-twenty-one'),
        (2022,'two-thousand-twenty-two'),
        (2023,'two-thousand-twenty-three'),
        (2024,'two-thousand-twenty-four'),
        (2025,'two-thousand-twenty-five'),
        (2026,'two-thousand-twenty-six'),
        (2027,'two-thousand-twenty-seven'),
        (2028,'two-thousand-twenty-eight'),
        (2029,'two-thousand-twenty-nine'),
    )

    titel = models.CharField(max_length=15)
    beschreibung = models.TextField(max_length=160)
    tag = models.IntegerField(choices=DAYS)
    monat = models.IntegerField(choices=MONTHS)
    jahr = models.IntegerField(choices=YEARS)
    status = models.IntegerField()

    def __str__(self):
        return self.titel
