import unittest

class TestChallengeMethods(unittest.TestCase):

	def test_max_score(self):
		import re
		path = "customer_products.txt"
		file = open(path, 'r')
		text = file.readlines()
		self.assertTrue(get_score(text[0]), 21.00)
		self.assertTrue(get_score(text[1]), 83.50)
		self.assertTrue(get_score(text[2]), 71.25)

if __name__ == "__main__":
	unittest.main()
