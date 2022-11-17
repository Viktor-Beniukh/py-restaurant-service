from django.shortcuts import render

from kitchen.models import Cook, DishType, Dish, Ingredient


def index(request):
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_ingredients = Ingredient.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_ingredients": num_ingredients,
    }

    return render(request, "kitchen/index.html", context=context)
