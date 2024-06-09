#functie care stocheaza datele CFG-ului intr-un dictionar
def CFG(content):
    d={}
    x=None
    for linie in content:
        linie=linie.strip()
        if linie[0]=='#':
            continue  #ignora comentariile din fisier
        #creaza chei cu atributele CFG-ului
        if linie[len(linie)-1]==':':
            x=linie[:len(linie)-2]
            d[x] = []
        else:
            d[x].append(linie) #se stocheaza valorile fiecarui atribut pana la urmatorul
    return d

#functie care verifica daca este valid un CFG primit sub forma de text,
#iar daca este, il emuleaza cu ajutorul functiei emulatorCFG
def verificareCFG(content, sir):
    dict=CFG(content)
    # verifica daca are toate atributele
    if "Sigma" in dict and "Variables" in dict and "Rules" in dict:
        #verifica daca fiecare regula respecta formatul
        for regula in dict["Rules"]:
            regula=regula.split()
            if len(regula)!=3:
                return "error: Regulile nu sunt bine definite"
            else:
                if regula[0] not in dict["Variables"] or regula[1] !='-':
                    return "error: Regulile nu sunt bine definite"
                valoare = regula[2].split("|")
                #verifica daca terminalele si variabilele din reguli au fost declarate anterior
                for val in valoare: #val reprezinta fiecare valoare cu care poate fi derivata o variabila
                    i = 0
                    while i < len(val):
                        #verifica daca subsir dupa subsir se afla in multimea variabilelor
                        found = False
                        for variable in dict["Variables"]:
                            if val[i:i + len(variable)] == variable:
                                i += len(variable)
                                found = True
                                break
                        # verifica daca apartine alfabetului, in caz ca nu s-a gasit anterior
                        if not found:
                            for simbol in dict["Sigma"]:
                                if val[i:i + len(simbol)] == simbol:
                                    i += len(simbol)
                                    found = True
                                    break
                        if not found:
                            return "error: Regulile nu sunt bine definite"
        #daca este valid va incepe emularea
        return emulatorCFG(sir, dict)
    else:
        return "error: CFG-ul nu este bine definit"


#functie care realizeaza derivarea, adica genereaza toate stringurile de lungime maxim 256
#si daca sirul cautat se afla printre ele, atunci emulatorCFG va returna "acceptat"/ respectiv "neacceptat"
def derivare(CFG, string_curent, string_tinta):
    if string_curent == string_tinta:
        return True #sirul a fost gasit printre cele posibile
    if len(string_curent) > 256:
        return False #daca depaseste limita, sirul nu este generat de CFG
    for i in range(len(string_curent)):
        for variable in CFG["Variables"]: #verifica fiecare subsir
            if string_curent[i:i + len(variable)] == variable: #daca subsirul este variabila
                for regula in CFG["Rules"]:
                    stanga, dreapta = regula.split(" - ") #stanga=variabila, dreapta=stringurile cu care poate fi substituit
                    if stanga == variable:
                        for optiune in dreapta.split("|"): #incearca fiecare varianta de derivare, apelandu-se recursiv
                            string_nou = string_curent[:i] + optiune + string_curent[i + len(variable):] #derivarea variabilelor
                            if derivare(CFG, string_nou, string_tinta):
                                return True
    return False

#functia care emuleaza CFG-ul
def emulatorCFG(sir, CFG):
    #se apeleaza functia de derivare cu variabila de start
    variable = CFG["Variables"][0]
    if derivare(CFG, variable, sir):
        return "acceptat"
    else:
        return "neacceptat"