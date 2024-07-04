import unittest

class TestSoundex(unittest.TestCase):

    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('A'), '0')  # Vowel
        self.assertEqual(get_soundex_code('H'), '0')  # Ignored character
        self.assertEqual(get_soundex_code('Z'), '2')
        self.assertEqual(get_soundex_code('x'), '2')  # Lowercase input

    def test_remove_consecutive_duplicates(self):
        self.assertEqual(remove_consecutive_duplicates("A111223344"), "A1234")
        self.assertEqual(remove_consecutive_duplicates("A111"), "A1")
        self.assertEqual(remove_consecutive_duplicates("A"), "A")
        self.assertEqual(remove_consecutive_duplicates("A1"), "A1")
        self.assertEqual(remove_consecutive_duplicates(""), "")

    def test_encode_characters(self):
        self.assertEqual(encode_characters("Robert"), "R163")
        self.assertEqual(encode_characters("Rupert"), "R163")
        self.assertEqual(encode_characters("Rubin"), "R150")
        self.assertEqual(encode_characters("Ashcraft"), "A22631")
        self.assertEqual(encode_characters("Tymczak"), "T5222")
        self.assertEqual(encode_characters("Pfister"), "P1236")
        self.assertEqual(encode_characters(""), "")

    def test_generate_soundex(self):
        self.assertEqual(generate_soundex(""), "")
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Rubin"), "R150")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Tymczak"), "T522")
        self.assertEqual(generate_soundex("Pfister"), "P236")
        self.assertEqual(generate_soundex("BOAT"), "B300")
        self.assertEqual(generate_soundex("BFPV"), "B100")
        self.assertEqual(generate_soundex("CGJKQSXZ"), "C220")

if __name__ == "__main__":
    unittest.main()
