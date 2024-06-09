'''
Programul citeste dintr-un fisier datele
pentru un NFA, sub forma unui dictionar.
Fisierul de intrare trebuie sa fie neaparat
de urmatorul format:

Sigma :
....
States :
.....
Start :
.....
Final :
.....
Transitions :
.....

deci trebuie sa contina aceste 5 titluri, neaparat cu aceste nume,
cu spatiu si semnul ':' dupa ele, exact cum e scris mai sus,
apoi datele trebuie scrise fiecare pe un rand, de exemplu

Sigma :
    0
    1

unde '0' si '1' sunt valorile, in cazul de fata ale multimii
"Sigma" (care reprezinta alfabetul NFA-ului).
Astfel se declara si valorile pentru "States" (multimea
starile NFA-ului), "Start" (starea initiala), "Final" (multimea
starilor finale) si "Transitions" (tranzitiile NFA-ului).
In cazul lui "Transitions" valorile sunt de forma: stareCurenta, litera, stareNoua1 stareNoua2....
deci dintr-o stare se poate ajunge in mai multe, starile noi fiind despartite doar printr-un spatiu,
iar in cazul tranzitiilor epsilon, se va folosi caracterul "*" ca litera
de exemplu:

Transitions :
    q0, 0, q1
    q1, 1, q2 q3 q4
    q2, *, q0 q1

Daca nu este respectat acest fomat, sau daca valorile din "Start",
"Final" si "Transitions" nu sunt in concordanta cu "Sigma" si "States"
se va returna o eroare.
Se accepta in fisierul de intrare orice tip de
comentarii daca sunt precedate de caracterul '#', ca in exemplu:

#vom scrie un nou NFA
#acesta este alfabetul
Sigma :
    0
    1
#urmeaza starile
States :
    q0
    q1

Nu se accepta spatii intre randuri.

Rulati programul si introduceti mai intai numele fisierului unde este salvat NFA-ul,
apoi sirul pe care doriti sa-l verificati
'''

#verificareNFA este fuctia care verifica daca un NFA este bine definit si verifica
#daca un sir este acceptat de acesta(are ca parametri un fisier text si un string)
from functii_NFA import verificareNFA
print("Numele fisierului unde ati salvat NFA-ul:")
NFA=input()
f=open(NFA)
print("Sirul pe care doriti sa-l verificati:")
sir=input()
print(verificareNFA(f, sir))
