from django.test import TestCase

from ..services import temp_operations


class ServiceTestCase(TestCase):

    def test_plus(self):
        result = temp_operations(6, 13, '+')
        self.assertEqual(19, result)

