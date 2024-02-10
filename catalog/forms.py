from django import forms
from .models import BusTour, Cruise
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):

    def use_required_attribute(self, *args):
        return False


class BusTourForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание',
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    
    timeline = forms.CharField(
        label='Программа тура',
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    charges = forms.CharField(
        label='Стоимость тура',
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )


    class Meta:
        model = BusTour
        fields = [
            'title', 'description', 'price',
            'country', 'tourdates', 'timeline',
            'charges', 'group_size', 'image'
        ]
        
    


class CruiseForm(BusTourForm):
    class Meta:
        model = Cruise
        fields = [
            'title', 'description', 'price',
            'tourdates', 'timeline', 'charges',
            'group_size', 'image'
        ]
    

class FilterForm(forms.Form):
    price = forms.IntegerField(label='Стоимость', widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': 500, 'max': 15000}))
    n_days = forms.IntegerField(label='Продолжительность', widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': 1, 'max': 7}))

    price.widget.attrs.update({'class': 'form-control'})