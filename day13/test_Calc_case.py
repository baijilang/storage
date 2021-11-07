from unittest import TestCase
from Calc import Calc


class Test_Calc(TestCase):
    def test_add1(self):
        a = 2
        b = 3
        c = 5
        calc = Calc()
        d = calc.add(2,3)
        self.assertEqual(c, d)

    def test_add2(self):
        a = 8
        b = 4
        c = 12
        calc = Calc()
        d = calc.add(8, 4)
        self.assertEqual(c,d)

    def test_add3(self):
        a = 7
        b = -4
        c = 3
        calc = Calc()
        d = calc.add(7, -4)
        self.assertEqual(c, d)

    def test_add4(self):
        a = 7.1
        b = 2.2
        c = 9.3
        calc = Calc()
        d = calc.add(7.1, 2.2)
        self.assertEqual(c, d)

    def test_minus1(self):
        a = 9
        b = 2
        c = 7
        calc = Calc()
        d = calc.minus(9, 2)
        self.assertEqual(c, d)

    def test_minus2(self):
        a = 19
        b = 21
        c = -2
        calc = Calc()
        d = calc.minus(19, 21)
        self.assertEqual(c, d)

    def test_minus3(self):
        a = 8
        b = -2
        c = 10
        calc = Calc()
        d = calc.minus(8, -2)
        self.assertEqual(c, d)

    def test_minus4(self):
        a = -4
        b = 6
        c = -10
        calc = Calc()
        d = calc.minus(-4, 6)
        self.assertEqual(c, d)

    def test_multi1(self):
        a = 4
        b = 6
        c = 24
        calc = Calc()
        d = calc.multi(4, 6)
        self.assertEqual(c, d)

    def test_multi2(self):
        a = 7
        b = 5
        c = 35
        calc = Calc()
        d = calc.multi(7, 5)
        self.assertEqual(c, d)

    def test_multi3(self):
        a = 3
        b = -6
        c = -18
        calc = Calc()
        d = calc.multi(3, -6)
        self.assertEqual(c, d)

    def test_multi4(self):
        a = -4
        b = 5
        c = -20
        calc = Calc()
        d = calc.multi(-4, 5)
        self.assertEqual(c, d)

    def test_multi5(self):
        a = 0
        b = 19
        c = 0
        calc = Calc()
        d = calc.multi(0, 19)
        self.assertEqual(c, d)

    def test_devi1(self):
        a = 0
        b = 10
        c = 0
        calc = Calc()
        d = calc.devi(0, 10)
        self.assertEqual(c, d)

    def test_devi2(self):
        a = 20
        b = 5
        c = 4
        calc = Calc()
        d = calc.devi(20, 5)
        self.assertEqual(c, d)

    def test_devi3(self):
        a = 4
        b = 8
        c = 0.5
        calc = Calc()
        d = calc.devi(4, 8)
        self.assertEqual(c, d)

    def test_devi4(self):
        a = 9
        b = -3
        c = -3
        calc = Calc()
        d = calc.devi(9, -3)
        self.assertEqual(c, d)
