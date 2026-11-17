from django import forms
from django.contrib import admin
from .models import Player, Position


class PlayerAdminForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        positions = cleaned_data.get('positions')
        specialist_eligible = cleaned_data.get('specialist_eligible')

        if positions and not specialist_eligible:
            has_specialist_position = positions.filter(is_specialist=True).exists()
            if has_specialist_position:
                raise forms.ValidationError(
                    'This player is not marked as eligible for specialist positions.'
                )
        return cleaned_data


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_specialist')
    list_filter = ('is_specialist',)
    search_fields = ('name',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    form = PlayerAdminForm
    list_display = ('first_name', 'last_name', 'age', 'specialist_eligible')
    list_filter = ('specialist_eligible', 'positions')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('positions',)
