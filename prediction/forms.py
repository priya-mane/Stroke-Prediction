from django import forms


class InputForm(forms.Form):
    CHOICES = [('Male', 'Male'),
               ('Female', 'Female'),
               ('Other', 'Other')]

    BINARY_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    WORK_CHOICES = [
        ('Private', 'Private'),
        ('Self-employed', 'Self-employed'),
        ('Govt_job', 'Government Job'),
        ('children', 'Under age'),
        ('Never_worked', 'Never worked')
    ]

    RESIDENCE_CHOICES = [
        ('Urban', 'Urban'),
        ('Rural', 'Rural')
    ]

    SMOKING_CHOICES = [
        ('formerly smoked', 'formerly smoked'),
        ('never smoked', 'never smoked'),
        ('smokes', 'smokes'),
        ('Unknown', 'Unknown')
    ]

    Gender = forms.CharField(widget=forms.Select(choices=CHOICES))

    Age = forms.IntegerField(min_value=0)

    Hypertension = forms.CharField(widget=forms.Select(choices=BINARY_CHOICES))

    Heart_disease = forms.CharField(
        widget=forms.Select(choices=BINARY_CHOICES))

    Ever_married = forms.CharField(widget=forms.Select(choices=BINARY_CHOICES))

    Work_type = forms.CharField(widget=forms.Select(choices=WORK_CHOICES))

    Residence_type = forms.CharField(
        widget=forms.Select(choices=RESIDENCE_CHOICES))

    Avg_glucose_level = forms.FloatField(min_value=0)

    Bmi = forms.FloatField(min_value=0)

    Smoking_status = forms.CharField(
        widget=forms.Select(choices=SMOKING_CHOICES))
