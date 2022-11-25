from django.test import TestCase

from kitchen.forms import (
    CookCreationForm,
    CookYearExperienceUpdateForm,
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm,
    IngredientSearchForm,
)


class FormTests(TestCase):
    def test_cook_creation_form_with_experience_first_last_name_is_valid(self):
        form_data = {
            "username": "new.user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 15,
        }

        form = CookCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_update_years_of_experience(self):
        form = CookYearExperienceUpdateForm({"years_of_experience": 12})

        self.assertTrue(form.is_valid())

    def test_correct_entry_years_of_experience(self):
        incorrect_years_of_experience = [
            "AW", "D4", "", 150,
        ]
        for years_of_experience in incorrect_years_of_experience:
            form = CookYearExperienceUpdateForm({"years_of_experience": years_of_experience})

            self.assertFalse(form.is_valid())

    def test_cook_search_form(self):
        form_data = {"username": "test.user"}
        form = CookSearchForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_dish_search_form(self):
        form_data = {"name": "test name"}
        form = DishSearchForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_dish_type_search_form(self):
        form_data = {"name": "test name"}
        form = DishTypeSearchForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_ingredient_search_form(self):
        form_data = {"name": "test name"}
        form = IngredientSearchForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
