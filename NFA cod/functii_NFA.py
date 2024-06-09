#functie care stocheaza datele NFA-ului intr-un dictionar
def NFA(content):
    d={}
    x=None
    for linie in content:
        linie=linie.strip()
        if linie[0]=='#':
            continue #ignora comentariile din fisier
        #creaza chei cu atributele NFA-ului
        if linie[len(linie)-1]==':':
            x=linie[:len(linie)-2]
            d[x] = []
        else:
            d[x].append(linie) #se stocheaza valorile fiecarui atribut pana la urmatorul
    return d
#functie care verifica daca este valid un NFA primit sub forma de text,
#iar daca este, il emuleaza cu ajutorul functiei emulatorNFA
def verificareNFA(content, sir):
    dict=NFA(content)
    #verifica daca are toate atributele
    if "Sigma" in dict and "States" in dict and "Start" in dict and "Final" in dict and "Transitions" in dict:
        # verifica daca starile de start si finale sunt declarate in multimea starilor
        if dict["Start"][0] in dict["States"]:
            for stare in dict["Final"]:
                if stare not in dict["States"]:
                    return "error: Starile finale nu sunt bine definite"
            #verifica daca fiecare tranzitie respecta formatul
            for tranzitie in dict["Transitions"]:
                tranzitie=tranzitie.split()
                for i in range(2,len(tranzitie)):
                    if (tranzitie[0][:-1] not in dict["States"] or tranzitie[i] not in dict["States"] or
                            (tranzitie[1][:-1] not in dict["Sigma"] and tranzitie[1][:-1] not in "*")):
                        return "error: Tranzitiile nu sunt bine definite"
            #daca este valid va incepe emularea
            return emulatorNFA(sir, dict)
        else:
            return "error: Starea initiala nu este bine definita"
    else:
        return "error: NFA-ul nu este bine definit"

#functia care emuleaza NFA-ul
def emulatorNFA(sir, NFA):
    #se incepe cu prima stare
    stari_curente=[NFA["Start"][0]]
    #realizam tranzitile epsilon
    for stare in stari_curente:
        for tranzitie in NFA["Transitions"]:
            tranzitie = tranzitie.split()
            if tranzitie[0][:-1] == stare and tranzitie[1][:-1] == '*':
                for i in range(2, len(tranzitie)):
                    stari_curente.append(tranzitie[i])
    for caracter in sir:
        stari_noi=[]
        #realizam tranzitiile din starile curente in cele noi
        for stare in stari_curente:
            for tranzitie in NFA["Transitions"]:
                tranzitie=tranzitie.split()
                if tranzitie[0][:-1]==stare and tranzitie[1][:-1]==caracter:
                    for i in range(2,len(tranzitie)):
                        stari_noi.append(tranzitie[i])
        stari_curente=stari_noi
        # realizam tranzitile epsilon
        for stare in stari_curente:
            for tranzitie in NFA["Transitions"]:
                tranzitie = tranzitie.split()
                if tranzitie[0][:-1] == stare and tranzitie[1][:-1] == '*':
                    for i in range(2, len(tranzitie)):
                        stari_curente.append(tranzitie[i])
    for stare in stari_curente:
        #acceptat daca la finalul inputului cel putin o stare curenta e una finala
        if stare in NFA["Final"]:
            return "acceptat"
    return "neacceptat"