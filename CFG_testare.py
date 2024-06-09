'''
Programul citeste dintr-un fisier datele
pentru un CFG, sub forma unui dictionar.
Fisierul de intrare trebuie sa fie neaparat
de urmatorul format:

Sigma :
....
Variables :
.....
Rules :
.....

deci trebuie sa contina aceste 3 titluri, neaparat cu aceste nume,
cu spatiu si semnul ':' dupa ele, exact cum e scris mai sus,
apoi datele trebuie scrise fiecare pe un rand, de exemplu

Sigma :
    0
    1
    *

unde '0' si '1' sunt valorile, in cazul de fata ale multimii
"Sigma" (care reprezinta alfabetul CFG-ului).
Astfel se declara si valorile pentru "Variables" (multimea
variabilelor CFG-ului), si "Rules" (regulile CFG-ului).
In cazul lui "Variables" prima variabila va fi si variabila de start, iar
in cazul lui "Rules" valorile sunt de forma: variabila - string1|string2|string3 ....
de exemplu:

Rules :
    A - 0A1|B
    B - *

Daca nu este respectat acest fomat, sau daca valorile din "Rules",
nu sunt in concordanta cu "Sigma" si "Variables"
se va returna o eroare.
Se accepta in fisierul de intrare orice tip de
comentarii daca sunt precedate de caracterul '#', ca in exemplu:

#vom scrie un nou CFG
#acesta este alfabetul
Sigma :
    0
    1
    *
#urmeaza variabilele
Variables :
    A
    B

Nu se accepta spatii intre randuri si in "Sigma" sau "Variables" nu poate exista caracterul '#'

Rulati programul si introduceti mai intai numele fisierului unde este salvat CFG-ul,
apoi sirul pe care doriti sa-l verificati(maxim 256 de caractere).
'''

#verificareCFG este fuctia care verifica daca un CFG este bine definit si verifica
#daca un sir este acceptat de acesta(are ca parametri un fisier text si un string)
from CFG_functii import verificareCFG
print("Numele fisierului unde ati salvat CFG-ul:")
CFG=input()
f=open(CFG)
print("Sirul pe care doriti sa-l verificati:")
sir=input()
print(verificareCFG(f, sir))
