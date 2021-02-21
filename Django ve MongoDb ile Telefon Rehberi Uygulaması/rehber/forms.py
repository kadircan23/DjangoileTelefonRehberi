from  django  import forms
from  .models import rehber


class ekleForm(forms.ModelForm):
    class Meta:
        model=rehber
        fields=[
            'name',
            'surname',
            'number',
            'address',
        ]

class sorgulaForm(forms.ModelForm):
    class Meta:
        model=rehber
        fields=[
            'number'
        ]

class updateForm(forms.ModelForm):
    class Meta:
        model=rehber
        fields=[
            'name',
            'surname',
            'number',
            'address',
        ]