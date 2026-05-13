from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro

        fields = '__all__'

        widgets = {

            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date'
            }),

            'fecha_ingreso': forms.DateInput(attrs={
                'type': 'date'
            }),

            'fecha_baja': forms.DateInput(attrs={
                'type': 'date'
            }),

            'reingreso': forms.DateInput(attrs={
                'type': 'date'
            }),

            'vigencia_licencia': forms.DateInput(attrs={
                'type': 'date'
            }),

            'domicilio': forms.Textarea(attrs={
                'rows': 3
            }),

            'observaciones': forms.Textarea(attrs={
                'rows': 4
            }),
        }