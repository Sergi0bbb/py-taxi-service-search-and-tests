from django.test import TestCase

from taxi.forms import DriverSearchForm, CarSearchForm, ManufacturerSearchForm


class DriverSearchFormTest(TestCase):
    def setUp(self):
        self.form_data = {
            "username": "bob"
        }

    def test_valid_form(self):
        form = DriverSearchForm(self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

    def test_valid_char_field_kwargs(self):
        form = DriverSearchForm(self.form_data)
        username_field = form.fields["username"]

        self.assertEqual(username_field.max_length, 150)
        self.assertFalse(username_field.required)
        self.assertEqual(username_field.label, "")
        self.assertEqual(
            username_field.widget.attrs["placeholder"],
            "Search driver:"
        )


class CarSearchFormTest(TestCase):
    def setUp(self):
        self.form_data = {
            "model": "bob"
        }

    def test_valid_form(self):
        form = CarSearchForm(self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

    def test_valid_char_field_kwargs(self):
        form = CarSearchForm(self.form_data)
        model_field = form.fields["model"]

        self.assertEqual(model_field.max_length, 150)
        self.assertFalse(model_field.required)
        self.assertEqual(model_field.label, "")
        self.assertEqual(
            model_field.widget.attrs["placeholder"],
            "Search car:"
        )


class ManufacturerSearchFormTest(TestCase):
    def setUp(self):
        self.form_data = {
            "name": "bob"
        }

    def test_valid_form(self):
        form = ManufacturerSearchForm(self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

    def test_valid_char_field_kwargs(self):
        form = ManufacturerSearchForm(self.form_data)
        model_field = form.fields["name"]

        self.assertEqual(model_field.max_length, 150)
        self.assertFalse(model_field.required)
        self.assertEqual(model_field.label, "")
        self.assertEqual(
            model_field.widget.attrs["placeholder"],
            "Search manufacturer:"
        )
