from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    skin_issues = forms.MultipleChoiceField(
        choices=[
            ('Acne', 'Acne'),
            ('Eczema', 'Eczema'),
            ('Psoriasis', 'Psoriasis'),
            ('Rosacea', 'Rosacea'),
            ('Hyperpigmentation', 'Hyperpigmentation'),
            ('Melasma', 'Melasma'),
            ('Sunburn', 'Sunburn'),
            ('Blackheads', 'Blackheads'),
            ('Whiteheads', 'Whiteheads'),
            ('Cystic Acne', 'Cystic Acne'),
            ('Skin Aging', 'Skin Aging'),
            ('Wrinkles', 'Wrinkles'),
            ('Fine Lines', 'Fine Lines'),
            ('Dryness', 'Dryness'),
            ('Flakiness', 'Flakiness'),
            ('Enlarged Pores', 'Enlarged Pores'),
            ('Dark Circles', 'Dark Circles'),
            ('Under-Eye Bags', 'Under-Eye Bags'),
            ('Skin Irritation', 'Skin Irritation'),
            ('Rashes', 'Rashes'),
            ('Hives', 'Hives'),
            ('Contact Dermatitis', 'Contact Dermatitis'),
            ('Seborrheic Dermatitis', 'Seborrheic Dermatitis'),
            ('Stretch Marks', 'Stretch Marks'),
            ('Cellulite', 'Cellulite'),
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Customer
        fields = ['name', 'mobile_number', 'age', 'skin_type', 'skin_issues']