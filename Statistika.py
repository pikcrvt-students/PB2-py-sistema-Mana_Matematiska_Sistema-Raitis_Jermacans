from random import randint
from statistics import mode
print("Šīs sistēmas mērķis ir iemācīt un pārbaudīt tavas zināšanas par tēmām:")
print("Aritmētiskais vidējais")
print("Moda")
print("Mediāna")
print("Ierakstot arit_vid_teorija(); moda_teorija();mediana_teorija() varēsiet apskatīt teoriju par priekšmetu un izpildīt dažus uzdevumus")
print("Ierakstot arit_vid_pd(); moda_pd(); mediana_pd() varēsiet pildīt pārbaudes darbus par izvēlēto tēmu")
print("Kad uzskatat ka esat pietiekoši atkartojuši tēmu ievadiet gala_pd() lai izpildītu pārbaudes darbu kurš ietvers uzdevumus no visām tēmām")

def arit_vid_teorija():
    #teorija
    print("Aritmētiskais vidējais ir vienāds ar pētījuma datu kopas visu vērtību summas un pētījuma novērojumu skaita dalījumu")
    print('xVID = (X1 + X2 +...Xn) / n')
    print("n ir visu datu kopējais skaits")
    print("Nospied Enter taustiņu lai lasītu tālāk")
    input()
    print("Piemēram ja mēs aizgājām uz 5 veikaliem lai pārbaudītu maizes cenu un uzzinātu kāds ir vidējais aritmētiskais baltmaizes cenai un ieguvām cenas: ")
    print("0,78 euro")
    print("0,67 euro")
    print("0,72 euro")
    print("0,59 euro")
    print("0,81 euro")
    print("Tad n = 5 jo ievākti dati par cenām no pieciem veikaliem")
    print("Lai aprēķinātu vidējo aritmētisko jāsakaita visas cenas kopā un jāizdala ar n")

    
    #dota piemera vid arit aprekinasana
    cenas_summa = 3.57
    summa_ievade = float(input("Ievadi visu cenu summu: "))
    atrisinats = False
    while atrisinats == False:
        if summa_ievade == cenas_summa:
            print("Pareizi")
            atrisinats = True
        else:
            print("Nepareizi mēģini vēlreiz")
            summa_ievade = float(input("Ievadi visu cenu summu: "))
    atrisinats = False

    
    #lietotajs pats ievada piemeru uz izrekina vid arit
    summa = 0
    saraksta_garums = int(input("Tagad pats ievadīsi vērtibas kurai izrēkinasi vidējo aritmētisko. No sākuma izvēlies cik vērtības gribi ievadīt: "))
    saraksts = [0] * saraksta_garums
    for x in range(saraksta_garums):
        saraksts[x] = float(input("Ievadi "+ str((x + 1)) +". vērtibu: "))
        summa += saraksts[x]

        
    summa_lietotajs = int(input("Tagad ievadi tiko ievadīto skaitļu summu: "))
    while atrisinats == False:
        if summa_lietotajs == summa:
            print("Pareizi")
            atrisinats = True
        else:
            summa_lietotajs = int(input("Nepareizi. Mēģini vēlreiz: "))
    atrisinats = False

    
    vid_teorija = summa / saraksta_garums
    float(vid_teorija)
    print("Tagad ievadi vidējo aritmētisko")
    vid_teorija_lietotajs = float(input("!!Atceries vid. arit. iegust kopēju summu izdalot ar datu kopēju skaitu!!. Raksti obligāti ar diviem skaitļiem aiz komata : "))
    while atrisinats == False:
        if vid_teorija_lietotajs == vid_teorija:
            print("Pareizi. Tu esi apguvis tēmas vidējais aritmētiskais teoriju :3")
            atrisinats = True
        else:
            vid_teorija_lietotajs = float(input("Nepareizi. Izlasi iepriekš rādīto teoriju un mēgini vēlreiz: "))
    atrisinats = False

    
def moda_teorija(): 
    atrisinats = False
    print("Statistikā moda ir datu vienība kura atkārtojas visvairāk")
    print("Piemēram mums ir saraksts kurš satur elementus 4,1,2,6,4,2,4,3,5,2")
    print("Šajā sarakstā moda ir vērtība 4 jo tā atkārtojas visvairāk reizes jeb trīs reizes")

    
    a = randint(8,10)
    moda_teorija_saraksts = [0] * a
    for i in range(a):
        moda_teorija_saraksts[i] = randint(1,7)
        
        
    print("Tagad pamēģini pats, dotajam sarakstam pieraksti modu")
    print(moda_teorija_saraksts)
    moda_saraksts_teorjia_lietotajs = int(input("Ievadi saraksta modu: "))
    while atrisinats == False:
        if moda_saraksts_teorjia_lietotajs == mode(moda_teorija_saraksts):
            print("Pareizi")
            atrisinats = True
        else:
            moda_saraksts_teorjia_lietotajs= int(input("Nepareizi mēģini vēlreiz: "))
    atrisinats = False
    
    
    a = randint(1,12)
    moda_teorija_saraksts = [0] * 8
    print("Tagad pats izveidosi sarakstu bet sarakasta modai ir jābūt", a," Sarakstam būs 8 elementi")
    for i in range(8):
        moda_teorija_saraksts = int(input("Ievadi "+ str(i+1) +". vērtību: "))
    lietotaja_saraksts_moda = mode(moda_teorija_saraksts)
    int(lietotaja_saraksta_moda)
    
    while atrisinats == False:
        if lietotaja_saraksts_moda == 8:
            print("Uzrakstīji pareizi. Esi apguvis teoriju par tēmu moda 0_0")
            atrisinats = True
        else:
            print("Nepareizi. Ievadi sarakstu vēlreiz")
            for i in range(8):
                moda_teorija_saraksts = int(input("Ievadi "+ str(i+1) +". vērtību: "))
            lietotaja_saraksts_moda = mode(moda_teorija_saraksts)
            int(lietotaja_saraksta_moda)
    atrisinats = False
    
