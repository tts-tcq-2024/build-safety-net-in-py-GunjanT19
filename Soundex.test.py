import unittest

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")

    def test_vowels_ignored(self):
        self.assertEqual(generate_soundex("AEIOU"), "A000")
        self.assertEqual(generate_soundex("BOAT"), "B300")

    def test_adjacent_same_code(self):
        self.assertEqual(generate_soundex("BFPV"), "B100")
        self.assertEqual(generate_soundex("CGJKQSXZ"), "C220")

    def test_h_w_between_same_code(self):
        self.assertEqual(generate_soundex("BHW"), "B000")
        self.assertEqual(generate_soundex("BPV"), "B100")
        self.assertEqual(generate_soundex("BXZW"), "B200")

    def test_zeros_padding(self):
        self.assertEqual(generate_soundex("D"), "D000")
        self.assertEqual(generate_soundex("DL"), "D400")

    def test_length_limited_to_four(self):
        self.assertEqual(generate_soundex("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "A123")

    def test_real_names(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Rubin"), "R150")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Tymczak"), "T522")
        self.assertEqual(generate_soundex("Pfister"), "P236")

if __name__ == "__main__":
    unittest.main()

