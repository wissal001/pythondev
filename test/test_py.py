

import app


#test fonction 1:


def test_pyaddition():


    # Vérifie que 1 + 2 = 3


        assert (app.addition(1, 2) == 3)


    # Vérifie que -1 + 1 = 0


        assert (app.addition(5, 1) == 6)
        
    #test fonction 2


def test_pysoustraction():


    # Vérifie que 1 - 2 = 3


        assert (app.soustraction(2, 1) == 1)

        
    # Vérifie que 5 -1 = 6


        assert (app.soustraction(5, 1) == 4)

    
    #teset fonction 3


def test_pyanswer2():
       assert( app.deinc(3) == 2)