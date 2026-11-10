#! /usr/bin/env python3

""" Illustration de quelques éléments de syntaxe à avoir en `self.tete` ;-) """

i=1

def foo1() : 
	print("i vu depuis foo1: ", i)
	# i globale

def foo2() : 
	i=2 # i locale car affectée !

def foo3() : 
    global i 
    i=2 #i globale

def foo4() :
    i = 10 
    def bar() : 
        i=30 # var locale

    bar()
    print("i de foo4: ", i) # i de foo4 n'a pas changé

def foo5() :
    i = 10 
    def bar() : 
        nonlocal i
        i=30 # var englobante

    bar()
    print("i de foo5: ", i)    # i de foo5 a changé

def foo6() :
    i = 10 
    def bar() : 
        global i
        i=30 # var globale

    bar()
    print("i de foo6: ", i) # i de foo6 n'a pas changé, i global a changé

def tests():
    print("Accès à une variable globale en lecture")
    foo1(); print("i global: ", i) # 
    
    print("variable locale car modifiée dans la fonction : i global ne change pas")
    foo2(); print("i global: ", i) # 
    
    print("accès à une variable globale en écriture")
    foo3(); print("i global: ", i) # 

    print("accès à une variable locale d'une fonction locale")
    foo4(); print("i global: ", i) # 
    
    print("accès à une variable englobante depuis une fonction locale")
    foo5(); print("i global: ", i) # 
    
    print("accès à une variable globale depuis une fonction locale")
    foo6(); print("i global: ", i) # 


def concat1(L) : 
    L = L+ [3,4]
    print("L dans la fonction : ", L)

def concat2(L) : 
    L.extend([3,4])
    print("L dans la fonction : ", L)

def tests_listes() :
    L= [1,2]
    print("concaténation à l'aide de l'opérateur +")
    concat1(L) ; print("L après : ", L) #

    print("concaténation à l'aide de l'opérateur extend")
    concat2(L) ; print("L après : ", L) #

if __name__ == "__main__":
    tests()
    tests_listes()
    