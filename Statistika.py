print("Šīs sistēmas mērķis ir iemācīt un pārbaudīt tavas zināšanas par tēmām:")
print("Aritmētiskais vidējais")
print("Moda")
print("Mediāna")

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
    vid_teorija_lietotajs = float(input("Tagad ievadi vidējo aritmētisko ( atceries vid. arit. iegust kopēju summu izdalot ar datu kopēju skaitu ): "))
    while atrisinats == False:
        if vid_teorija_lietotajs == vid_teorija:
            print("Pareizi. Tu esi apguvis tēmas vidējais aritmētiskais teoriju :3")
            atrisinats = True
        else:
            vid_teorija_lietotajs = float(input("Nepareizi. Izlasi iepriekš rādīto teoriju un mēgini vēlreiz: "))
    atrisinats = False
