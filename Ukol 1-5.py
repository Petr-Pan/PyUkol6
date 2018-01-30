zviratka = ["pes", "kočka", "králík", "had"]
zviratka2 = ["drak", "včelojed", "pes"]

def kratkyzvire(seznam):
    """Vrátí zviřátka se jménem kratším než 5 písmen."""
    navrat = []
    for prvek in seznam:
        if len(prvek) < 5:
            navrat.append(prvek)
    return navrat

def zacinana_k(seznam):
    """Vrátí ty zvířátka, co začínají na k."""
    navrat = []
    for prvek in seznam:
        if prvek.startswith("k"):
            navrat.append(prvek)
    return navrat

def je_moje_zviratko(zviratko):
    """Vrátí takový zvířátka, co jsou v mojem seznamu zvířátek."""
    if zviratko in zviratka:
        return True
    else:
        return False

def zviratkoseznamy(sez1, sez2):
    """Vrátí tři seznamy. První bude průnikem, druhý rozdíl sez1 a sez2, třetí rozdíl sez2 a sez1."""
    ret1 = []
    for zviratko in sez1:
        if zviratko in sez2:
            ret1.append(zviratko)
    for zviratko in sez2:
        if zviratko in sez1 and zviratko not in ret1:
            ret1.append(zviratko)
    ret2 = []
    for zviratko in sez1:
        if zviratko in sez1 and zviratko not in sez2:
            ret2.append(zviratko)
    ret3 = []
    for zviratko in sez2:
        if zviratko in sez2 and zviratko not in sez1:
            ret3.append(zviratko)
    return ret1, ret2, ret3


def zviratkadleabecedy(sez):
    return sorted(sez)

def zviratkadledivneabecedy(sez):
    pomocny = []
    for zviratko in sez:
        pomocny.append(zviratko[1:])
    vystup = []
    for zviratko in sorted(zip(pomocny, sez)):
        vystup.append(zviratko[1])
    return vystup