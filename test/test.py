import app
import unittest
#test fonction 1
# La fonction que nous allons tester
def addition(a, b):
    return a + b

# La classe de test
class TestAddition(unittest.TestCase):

    def test_addition(self):
        # Vérifie que 1 + 2 = 3
        self.assertEqual(addition(1, 2), 3)
        
        # Vérifie que -1 + 1 = 0
        self.assertEqual(addition(-1, 1), 0)
        
        # Vérifie que 0 + 0 = 0
        self.assertEqual(addition(0, 0), 0)

# Exécute les tests
unittest.main()

#test fonction 2
def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "2002/09/11".split(""))   
    # When.
    age = app.get_age(yyyy, mm, dd)
    # Then.
    assert age == 25 
    
#teset fonction 3
def test_answer2():
    assert app.deinc(3) == 2