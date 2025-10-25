import unittest

SERVER = "server b"


class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("soy un alfa")

    @unittest.skip("En proceso de construcción.")
    def test_skip(self):
        self.assertEqual("hello", "hello")

    @unittest.skipIf(SERVER == "server b", "Saltar mientras no se ejecute en el server indicado")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(10, 11)