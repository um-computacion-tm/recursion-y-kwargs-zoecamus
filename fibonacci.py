import unittest

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

class TestFibbonacci(unittest.TestCase):
    
    def test_with_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)
    
    def test_with_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)
    
    def test_with_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    
    def test_with_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)
    
    def test_with_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)
    
    def test_with_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    
    def test_with_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)
    
    def test_with_7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado, 13)
    
    def test_with_8(self):
        resultado = fibonacci(8)
        self.assertEqual(resultado, 21)
    
    def test_with_9(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 34)
    
    def test_with_10(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 55)
    
    def test_with_12(self):
        resultado = fibonacci(12)
        self.assertEqual(resultado, 144)
unittest.main()
