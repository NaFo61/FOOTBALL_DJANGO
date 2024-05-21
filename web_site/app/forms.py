from django import forms
from .models import *
from django.utils import timezone

class NationalTeamForm(forms.ModelForm):
    class Meta:
        model = NationalTeam
        fields = [
            'country_team',
            'year_of_start_team'
        ]
        labels = {
            'country_team': 'Национальная сборная',
            'year_of_start_team': 'Начало карьеры в сборной'
        }

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'name',
            'surname',
            'date_of_birthday',
            'city',
            'national_team_id_team',
        ]
        labels = {
            'name': "Имя игрока",
            'surname': "Фамилия игрока",
            'date_of_birthday': "Дата рождения",
            'city': "Город рождения",
            'national_team_id_team': "Национальная команда",
        }
        widgets = {
            "date_of_birthday": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
        }

    def clean_date_of_birthday(self):
        date_of_birthday = self.cleaned_data.get("date_of_birthday")

        if date_of_birthday and date_of_birthday > timezone.now().date():
            raise forms.ValidationError("День рождения не может быть в будущим")

        return date_of_birthday
