from django.forms import forms

from orm_all_queries_cookbook.models import Country, State, City


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"
