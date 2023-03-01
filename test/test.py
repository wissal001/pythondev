import app
#test fonction 1:

def test_addition():
        # Vérifie que 1 + 2 = 3
        assert (app.addition(1, 2), 3)
        
        # Vérifie que -1 + 1 = 0
        assert (app.addition(-1, 1), 0)
        
        # Vérifie que 0 + 0 = 0
        assert (app.addition(0, 0), 0)

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