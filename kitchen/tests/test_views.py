from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish, Ingredient, Cook

INDEX_URL = reverse("kitchen:index")
DISH_TYPE_URL = reverse("kitchen:dish_type-list")
DISH_URL = reverse("kitchen:dish-list")
INGREDIENT_URL = reverse("kitchen:ingredient-list")
COOK_URL = reverse("kitchen:cook-list")


class PublicIndexTests(TestCase):

    def test_login_required(self):
        response = self.client.get(INDEX_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateIndexTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user_name",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_index(self):
        response = self.client.get(INDEX_URL)

        self.assertEqual(response.status_code, 200)


class PublicDishTypeTests(TestCase):

    def test_login_required(self):
        response = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user_name",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Desserts")
        DishType.objects.create(name="Pastry")

        response = self.client.get(DISH_TYPE_URL)
        dish_type = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_type)
        )
        self.assertTemplateUsed(
            response,
            "kitchen/dish_type_list.html"
        )


class PublicDishTests(TestCase):

    def test_login_required(self):
        response = self.client.get(DISH_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateCarTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user_name",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_dishes(self):
        dish_type_one = DishType.objects.create(name="Desserts",)
        dish_type_two = DishType.objects.create(name="Pastry",)
        Dish.objects.create(
            name="Tiramisu",
            dish_type=dish_type_one,
            price=12.00,
        )
        Dish.objects.create(
            name="Muffin",
            dish_type=dish_type_two,
            price=10.30,
        )

        response = self.client.get(DISH_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(
            response,
            "kitchen/dish_list.html"
        )


class PublicIngredientTests(TestCase):

    def test_login_required(self):
        response = self.client.get(INGREDIENT_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateIngredientTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user_name",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_ingredients(self):
        Ingredient.objects.create(name="Tomato")
        Ingredient.objects.create(name="Potato")

        response = self.client.get(INGREDIENT_URL)
        ingredient = Ingredient.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredient)
        )
        self.assertTemplateUsed(
            response,
            "kitchen/ingredient_list.html"
        )


class PublicCookTests(TestCase):

    def test_login_required(self):
        response = self.client.get(COOK_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user_name",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        Cook.objects.create(
            username="CookOne",
            password="cooker111",
            years_of_experience=6,
        )
        Cook.objects.create(
            username="CookTwo",
            password="cooker222",
            years_of_experience=3,
        )
        Cook.objects.create(
            username="CookThree",
            password="cooker333",
            years_of_experience=20,
        )

        response = self.client.get(COOK_URL)
        cooks = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(
            response,
            "kitchen/cook_list.html"
        )

    def test_create_cook(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 15,
        }

        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])
