# -*- encoding: utf-8 -*-
from amount import Amount, AmountError
from decimal import Decimal
import unittest

class TestAmountInWords(unittest.TestCase):

    def test_convert_to_words(self):
        cases = [
            ('0.94', u"dziewięćdziesiąt cztery grosze"),
            ('7092.12', u"siedem tysięcy dziewięćdziesiąt dwa złote i dwanaście groszy"),
            ('112301.01', u"sto dwanaście tysięcy trzysta jeden złotych i jeden grosz"),
            ('1000018', u"jeden milion osiemnaście złotych"),
            ('1.23', u"jeden złoty i dwadzieścia trzy grosze"),
        ]
        for amount, words in cases:
            self.assertEqual(Amount.in_words(amount), words)

    def test_to_big_amount(self):
        self.assertRaises(AmountError, Amount.in_words, Decimal(10**18))

if __name__ == '__main__':
    unittest.main()
