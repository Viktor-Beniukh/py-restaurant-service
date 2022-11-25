from django.test import TestCase

from kitchen.models import DishType, Cook, Dish, Ingredient


class DishTypeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        DishType.objects.create(name="Desserts",)

    def test_dish_type_str(self):
        dish_type = DishType.objects.get(id=1)

        self.assertEqual(str(dish_type), f"{dish_type.name}")


class DishModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        dish_type = DishType.objects.create(
            name="Pastry",
        )
        cook = Cook.objects.create(
            username="user_name",
            password="user12345"
        )
        dish = Dish.objects.create(
            name="Muffin",
            dish_type=dish_type,
            price=10.50
        )
        dish.cooks.add(cook)

    def test_dish_str(self):
        dish = Dish.objects.get(id=1)

        self.assertEqual(str(dish), f"{dish.name}")


class IngredientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name="Tomato",)

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.get(id=1)

        self.assertEqual(str(ingredient), f"{ingredient.name}")


class CookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cook.objects.create_user(
            username="user_name",
            password="user12345",
            years_of_experience="30",
            first_name="user",
            last_name="name"
        )

    def test_create_cook_with_years_of_experience(self):
        cook = Cook.objects.get(id=1)
        field_label = cook._meta.get_field("years_of_experience").verbose_name

        self.assertEqual(cook.username, "user_name")
        self.assertTrue(cook.check_password("user12345"))
        self.assertEqual(field_label, "years of experience")

    def test_cook_str(self):
        cook = Cook.objects.get(id=1)

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_get_absolute_url(self):
        cook = Cook.objects.get(id=1)

        self.assertEqual(cook.get_absolute_url(), "/cooks/1/")
