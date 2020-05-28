from django.test import TestCase

from app.calc import add

class CaclTests(TestCase):

	def test_add_numbers(self):
		"""Test"""
		self.assertEqual(add(3,8),11)