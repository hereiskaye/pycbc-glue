from glue.lal import *
import unittest


#
# Define the components of the test suite.
#

class test_LIGOTimeGPS(unittest.TestCase):
	def test__init__(self):
		correct = LIGOTimeGPS(100, 500000000)
		tests = [
			(100.5,),
			(100.500000000,),
			(100.50000000000000000000000,),
			(100, "500000000"),
			(100, "500000000.0000000000000"),
			(101, "-500000000"),
			(101, "-500000000.0000000000000"),
			("100.5",),
			("100.500000000",),
			("100.50000000000000000000000",),
			("100", 500000000),
			("100", 500000000.0000000000000),
			("101", -500000000),
			("101", -500000000.0000000000000),
			("100", "500000000"),
			("100", "500000000.0000000000000"),
			("101", "-500000000"),
			("101", "-500000000.0000000000000"),
			(0, 100500000000),
			(0, 100500000000.0000000000000),
			(99, 1500000000),
			(99.5, 1000000000),
			(-10, 110500000000),
			(-10.5, 111000000000)
		]
		for num, test in enumerate(tests):
			try:
				self.assertEqual(correct, LIGOTimeGPS(*test))
			except AssertionError, e:
				raise AssertionError, "Test %d failed: " % (num) + str(e)

	def test__float__(self):
		self.assertEqual(100.5, float(LIGOTimeGPS(100.5)))

	def test__int__(self):
		self.assertEqual(100, int(LIGOTimeGPS(100.1)))
		self.assertEqual(100, int(LIGOTimeGPS(100.9)))

	def testns(self):
		self.assertEqual(100500000000, LIGOTimeGPS(100.5).ns())

	def test__nonzero__(self):
		self.assertEqual(True, bool(LIGOTimeGPS(100.5)))
		self.assertEqual(False, bool(LIGOTimeGPS(0)))


#
# Construct and run the test suite.
#

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_LIGOTimeGPS))

unittest.TextTestRunner(verbosity=2).run(suite)
