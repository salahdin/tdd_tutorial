from django.test import TestCase

# Create your tests here.
class failingtest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1 , 3)