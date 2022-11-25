from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Cook, Dish, Ingredient


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean_years_of_experience(self) -> int:
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


class CookYearExperienceUpdateForm(forms.ModelForm):

    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_years_of_experience(self) -> int:
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


def validate_years_of_experience(years_of_experience: int) -> int:

    if not isinstance(years_of_experience, int):
        raise ValidationError("The characters must be digits")

    elif not 0 <= len(str(years_of_experience)) <= 2:
        raise ValidationError(
            "Years of experience should be within 0 to 2 digits inclusive"
        )

    return years_of_experience


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..."}
        )
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..."}
        )
    )


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..."}
        )
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username..."}
        )
    )
