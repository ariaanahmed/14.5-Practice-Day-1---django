from django import forms
from django.forms.widgets import NumberInput
import datetime

class ContactForm(forms.Form):
    # Name field
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"}),
        max_length=10,
        required=False,
    )

    # Email field
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Enter your email"}),
        required=False,
    )

    # Comment field (text area)
    comment = forms.CharField(
        label="Post a Comment",
        widget=forms.Textarea(attrs={"placeholder": "Add a comment", "rows": 3}),
        initial="Your name comment",
    )

    # Agreement check box
    agree = forms.BooleanField(
        label="Agree to terms",
        initial=True,
    )

    # Date field
    date = forms.DateField(label="Date", required=False)

    # Birthday field with date input widget
    birthday = forms.DateField(
        label="Birthday", widget=NumberInput(attrs={"type": "date"})
    )

    # Birthday by year selection
    BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
    birth_year = forms.DateField(
        label="Birth Year", widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )

    # Decimal value field
    decimal_value = forms.DecimalField(
        label="Decimal Value",
    )

    # intial date
    day = forms.DateField(label="Today's date", initial=datetime.date.today)

    # drop down menu
    FAVORITE_COLORS_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black"),
    ]

    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    # choice field with radio select
    favorite_color2 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES
    )

    favorite_colors3 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

    favorite_colors4 = forms.MultipleChoiceField(
        choices=FAVORITE_COLORS_CHOICES
    )
