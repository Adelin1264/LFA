#functie care stocheaza datele DFA-ului intr-un dictionar
def DFA(content):
    d={}
    x=None
    for linie in content:
        linie=linie.strip()
        if linie[0]=='#':
            continue #ignora comentariile din fisier
        #creaza chei cu atributele DFA-ului
        if linie[len(linie)-1]==':':
            x=linie[:len(linie)-2]
            d[x] = []
        else:
            d[x].append(linie) #se stocheaza valorile fiecarui atribut pana la urmatorul
    return d

#functie care verifica daca este valid un DFA primit sub forma de text,
#iar daca este, il emuleaza cu ajutorul functiei emulatorDFA
def verificareDFA(content, sir):
    dict=DFA(content)
    #verifica daca are toate atributele
    if "Sigma" in dict and "States" in dict and "Start" in dict and "Final" in dict and "Transitions" in dict:
        #verifica daca starile de start si finale sunt declarate in multimea starilor
        if dict["Start"][0] in dict["States"]:
            for stare in dict["Final"]:
                if stare not in dict["States"]:
                    return "error: Starile finale nu sunt bine definite"
            #verifica daca fiecare tranzitie respecta formatul
            for tranzitie in dict["Transitions"]:
                tranzitie=tranzitie.split()
                if len(tranzitie)!=3:
                    return "error: Tranzitiile nu sunt bine definite"
                else:
                    if tranzitie[0][:-1] not in dict["States"] or tranzitie[2] not in dict["States"] or tranzitie[1][:-1] not in dict["Sigma"]:
                        return "error: Tranzitiile nu sunt bine definite"
            #daca este valid va incepe emularea
            return emulatorDFA(sir, dict)
        else:
            return "error: Starea initiala nu este bine definita"
    else:
        return "error: DFA-ul nu este bine definit"

#functia care emuleaza DFA-ul
def emulatorDFA(sir, DFA):
    #se incepe cu prima stare
    stare=DFA["Start"][0]
    #cautam literele din string, intrucat un alfabet poate avea stringuri ca litere
    for i in range(len(sir)):
        for j in range(i, len(sir)):
            subsir=sir[i:j+1]
            if subsir in DFA["Sigma"]: #la fiecare litera din alfabet
                for k in DFA["Transitions"]: #se cauta tranzitia potrivita
                    tranzitie=k
                    tranzitie=tranzitie.split()
                    if tranzitie[0][:-1]==stare and tranzitie[1][:-1]==subsir:
                        stare=tranzitie[2] #se realizeaza tranzitia
                        break
                break
    #acceptat daca la finalul inputului starea e una finala
    if stare in DFA["Final"]:
        return "acceptat"
    else:
        return "neacceptat"