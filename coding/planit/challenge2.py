import unittest
def high_occur_char(str):
    str = str.lower()
    high_occur_char = str[0]
    high_count = 0
    for i in range(len(str)):
        count = 0
        for char in str:
            if str[i] == char:
                count += 1
        if count > high_count:
            high_count = count
            high_occur_char = str[i]
    return high_occur_char

class Tester(unittest.TestCase):

    def test_high_occur_char(self):
        self.assertEqual(high_occur_char('Character'), 'c')
        self.assertEqual(high_occur_char('aBcaBcbcab'), 'b')
        self.assertEqual(high_occur_char('abcabcbcabA'), 'a')
        self.assertEqual(high_occur_char('##abcabcbcab##!'), '#')
        self.assertEqual(high_occur_char('12abcabcb4%cab'), 'b')
        self.assertEqual(high_occur_char('abcabc*235bcab'), 'b')

if __name__ == "__main__":
    unittest.main()

