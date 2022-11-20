from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cooker",
            password="cooker123",
            years_of_experience="20",
            first_name="test",
            last_name="user",
        )

    def test_cook_years_of_experience_listed(self):
        """
        Tests that check the availability of experience of cooks
        is in list_display on cook administrator page
        """

        url = reverse("admin:kitchen_cook_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_create_additional_fields_listed(self):
        """
        Tests that cook's additional fields
        (first name, last name, years of experience)
        is on cook detail admin page
        """

        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        response = self.client.get(url)

        self.assertContains(response, self.cook.first_name)
        self.assertContains(response, self.cook.last_name)
        self.assertContains(response, self.cook.years_of_experience)
