import app


#test fonction 1
def test_pyaddition():
    assert(app.addition(1, 2) == 3)
    assert(app.addition(5, 1) == 6)
#test fonction 2
def test_pysoustraction():
    assert(app.soustraction(2, 1) == 1)
    assert(app.soustraction(6, 1) == 5)
    
#tset fonction 3
def test_pyanswer2():
    assert app.deinc(3) == 2