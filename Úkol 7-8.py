def format(rc):
    """Zkontroluje formát rodného čísla: číslice na prvních 6 a posledních 4 místech,
    lomítko mezi nimi a zda čísla reprezentující měsíc a den odpovídají našemu kalendáři."""
    if len(rc) != 11:
        chyba = "Zadané číslo je příliš krátké."
        return False, chyba
    for i in range(6):
        try:
            val = int(rc[i])
        except ValueError:
            chyba = 'Prvek na ',i+1,'. místě nebyl číslo.'
            return False, chyba

    if rc[6] != "/":
        chyba = "Na sedmé pozici chybí lomítko."
        return False, chyba
    for i in range(7,11):
        try:
            val = int(rc[i])
        except ValueError:
            chyba = "Prvek na ", i+1,". místě nebyl číslo."
            return False, chyba

    #Test, zda je měsíc validní (v intervalu 1-12)
    mesic = int(rc[2:4])
    #Ženy mají číslo měsíce o 50 navýšené, proto kontrola
    if mesic - 50 > 0:
        mesic -= 50
    #Udělal bych ty následující kontroly přes nějakou výjimku místo vracení dvou proměnných,
    #ale nezjistil jsem, jak ji vyvolat při tomhle typu podmínky
    if mesic < 1 or mesic > 12:
        chyba = "Máš divně veliký měsíc."
        return False, chyba
    #Test, zda den validní (v intervalu 1-12)
    den = int(rc[4:6])
    if den < 1 or den > 31:
        chyba = "Máš divně veliký den."
        return False, chyba
    chyba = []
    return True, chyba

def delitelnost11(rc):
    test = rc[:6]+rc[7:]
    if int(test) % 11 == 0:
        return True
    return False

def datumnarozeni(rc):
    #Den a měsíc intovány pro hezčí output (1.2.78 místo 01.02.78)
    rok = rc[:2]
    mesic = int(rc[2:4])
    den = int(rc[4:6])
    if mesic - 50 > 0:
        mesic -= 50
    return den, mesic, rok


def sexdetector(rc):
    cislomesice = rc[2:4]
    if int(cislomesice) - 50 > 0:
        return "žena"
    return "muž"

user_rc = input("Zadej své rodné číslo a já ti možná něco povím: ")
print("Rodné číslo ve správném formátu:", format(user_rc)[0])
if format(user_rc)[0] == False:
    print(format(user_rc)[1])
    print("Končím, s tímhle nechutným formátem víc dělat nebudu.")
else:
    print("Rodné číslo validní (dělitelné jedenácti):", delitelnost11(user_rc),)
    print("Datum narození:", datumnarozeni(user_rc)[0],".", datumnarozeni(user_rc)[1],".",datumnarozeni(user_rc)[2])
    print("Pohlaví:", sexdetector(user_rc))