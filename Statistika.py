from random import randint
from statistics import mode
from statistics import median
def arit_vid(x):
    return sum(x) / len(x)
path = "C:\\Users\\12DRJermacans\\Downloads\\PB2-py-sistema-Mana_Matematiska_Sistema-Raitis_Jermacans\\atzimes.txt"
atver_failu = open(path, 'a')

print("Šīs sistēmas mērķis ir iemācīt un pārbaudīt tavas zināšanas par tēmām:")
print("Aritmētiskais vidējais")
print("Moda")
print("Mediāna")
vards = input("Lai sāktu darības lūdz vieadiet savu vārdu un uzvārdu: ")
atver_failu.write(vards)
atver_failu.write("\n")
atver_failu.read
print("Labdien", vards)
print("Ierakstot arit_vid_teorija(); moda_teorija();mediana_teorija() varēsiet apskatīt teoriju par priekšmetu un izpildīt dažus uzdevumus\n")
print("Ierakstot arit_vid_pd(); moda_pd(); mediana_pd() varēsiet pildīt pārbaudes darbus par izvēlēto tēmu\n")
print("Kad uzskatat ka esat pietiekoši atkartojuši tēmu ievadiet gala_pd() lai izpildītu pārbaudes darbu kurš ietvers uzdevumus no visām tēmām\n")
print("Lai redzētu darbu rezultātus ieraksti temas_punkti()")
print("-------------------------------------------------------------------------------------------------------------------------------------------------")
def temas_punkti():
    for i in range(3):
        if i == 0:
            print("Aritmētiskais vidējais darba iegūtie punkti", temas_pd[0])
        elif i == 1:
            print("Medianas darba iegūtie punkti", temas_pd[1])
        else:
            print("Modas darba iegutie punkti", temas_pd[2])
            
temas_pd = [[0,0,0],[0,0,0],[0,0,0]]
gala_pd = []
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
        if vid_teorija_lietotajs == "{:.2f}".format(vid_teorija):
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
def mediana_teorija():
    atrisinats = False
    print("Mediāna ir vidējais rezultāts skaitļu virknē, kurā visi elementi sakārtoti augošā secībā ")
    print("Teiksim ir saraksts 1,6,2,4,3,6,6,3,2")
    print("Lai iegūtu mediānu sākumā vajag sakārtot vērtības augošā secībā")
    print("Tad iznāk 1,2,2,3,3,4,6,6,6")
    print("Sarakstā pa vidu atrodas skaitlis 3 tātad 3 ir mediāna")
    print("Gadījumā kad ir pāra skaita elementu paņem abas vērtības tuvāk saraksta vidum, tās saskaita, un izdala ar 2")
    print("Sarakstā 1,2,2,3,4,4 pa vidu atrodas 2 skaitļi 2 un 3 tāpēc mediānu iegūsim saskaitot 2 un 3 kopā un izdalot uz 2 dodot atbildi 2.5")
    a = [0] * 9
    for i in range(9):
        a[i] = randint(1,10)

    mediana_teorija = int(input("Pamēģināsi pats. Kas ir mediāna sarakstam" + str(a)+": " ))
    while atrisinats == False:
        if mediana_teorija == median(a):
            print("Pareizi")
            atrisinats = True
        else:
            mediana_teorija = int(input("Mēģini vēlreiz: "))
    atrisinats = False

    print("Tagad tev jāizveido saraksts kura mediāna ir 5. Sarakstā būs 9 elementi")
    while atrisinats == False:
        a = [0] * 9
        for i in range(9):
            a[i] = int(input("Ievadi "+str(i+1)+". saraksta elementu: "))
        if median(a) == 5:
            print("Pareizi. Esi apguvis tēoriju par tēmu mediāna ^_^")
            atrisinats = True
        else:
            print("Mēģini vēlreiz")
            for i in range(9):
                a[i] = int(input("Ievadi "+str(i+1)+". saraksta elementu: "))

#pārbaudes darbi par tēmām
def arit_vid_pd():
    print("Pārbaudes darbs par tēmu Aritmētiskai Vidējais")
    print("Darbā būs 3 uzdevumi")
    print("Maksimālais punktu skaits ir 6")
    #1
    a = [0] * 7
    for i in range(7):
        a[i] = randint(1,12)
    print(a)
    y = float("{:.2f}".format(arit_vid(a)))
    AV_pirm_uzd = float(input("(3 punkti) Kāds ir vidējais aritmētiskais sarakstam ( lieto 2 ciparus aiz komata): "))
    if AV_pirm_uzd == y:
        temas_pd[0][0] = 3
    #2
    x = randint(4,7)
    a = [0] * x
    print("(2 punkti) Izveido sarakastu kurā ir", x ,"elementi un vidējā vērtība ir 6")
    for i in range(x):
        a[i] = int(input("Ievadi "+ str(i+1) +". saraksta vērtību: "))
    if arit_vid(a) == 6:
        temas_pd[0][1] = 2
    #3
    x = randint(4,7)
    a = [0] * x
    for i in range(x):
        a[i] = randint(1,15)
    AV_tres_uzd = int(input("(1 punkts) Kāda ir summa sarakstam ja tajā ir "+ str(x) +" vērtības un "+ str("{:.2f}".format(arit_vid(a))) +" ir aritmētiskai vidējais: "))
    if AV_tres_uzd == sum(a):
        temas_pd[0][2] = 1
    print("Ieguvi", str(sum(temas_pd[0])) ,"punktus")
    
    atver_failu.write("Aritmētsikais vidējais pārbaudes darba punkti skaits"+ str(sum(temas_pd[0])) +"/6")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    
def moda_pd():
    print("Pārbaudes darbs par tēmu Moda")
    print("Darbā būs 3 uzdevumi")
    print("Maksimālais punktu skaits ir 5")
    #1
    x = randint(9,15)
    a = [0] * x
    for i in range(x):
        a[i] = randint(3,10)
    moda_a = mode(a)
    print(a)
    MODA_pirm_uzd = int(input("(3 punkti) Kas ir moda dotajam sarakstam: "))
    if MODA_pirm_uzd == moda_a:
        temas_pd[1][0] = 3
    #2
    x = randint(9,15)
    a = [0] * x
    for i in range(x):
        a[i] = randint(3,10)
    moda_a = mode(a)
    print(a)
    MODA_otr_atbild = randint(3,10)
    MODA_otr_uzd = input("(1 punkts) Vai saraksta moda ir "+ str(MODA_otr_atbild) +" (atbildi ar jā vai nē): ")
    if MODA_otr_atbild == moda_a:
        if MODA_otr_uzd == "jā":
            temas_pd[1][1] = 1
    else:
        if MODA_otr_uzd == "nē":
            temas_pd[1][1] = 1
    #3
    x = randint(9,15)
    a = [0] * x
    for i in range(x):
        a[i] = randint(3,10)
    moda_a = mode(a)
    print(a)
    arit_vid_a = arit_vid(a)
    iespeja = randint(1,2)
    if iespeja == 1:
        print(moda_a)
        MODA_tres_atbilde = "moda"
    else:
        print(arit_vid_a)
        MODA_tres_atbilde = "videjais aritmetiskais"
    MODA_tres_uzd = input("(1 punkts) Vai iepriekš dotais skaitlis ir saraksta moda vai videjais aritmetiskais: ")
    if MODA_tres_uzd == MODA_tres_atbilde:
        temas_pd[1][2] = 1
    print("Ieguvi", str(sum(temas_pd[1])) ,"punktus")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
def mediana_pd():
    print("Pārbaudes darbs par tēmu Mediāna")
    print("Darbā būs 3 uzdevumi")
    print("Maksimālais punktu skaits ir 6")

    #1
    x = randint(6,10)
    a = [0] * x
    for i in range(x):
        a[i] = randint(1,20)
    mediana_a = median(a)
    print(a)
    MEDI_pirm_uzd = float(input("(3 punkti) Ievadi saraksta mediānu ( raksti ar 2 cipariem aiz komata ) :"))
    if MEDI_pirm_uzd == mediana_a:
        temas_pd[2][0] = 3
    #2
    x = randint(5,11)
    print("(2 punkti) Izveido sarakstu kura mediāna ir", x, "Sarakstā būs 8 elementi")
    a = [0] * 8
    for i in range(8):
        a[i] = int(input("Ievadi saraksta "+ str(i+1)+" elementu: "))
    if median(a) == x:
        temas_pd[2][1] = 2
    #3
    x = randint(6,9)
    a = [0] * x
    for i in range(x):
        a[i] = randint(1,10)
    print(a)
    mediana_a = median(a)
    vid_arit_a = arit_vid(a)
    iespeja = randint(1,2)
    if iespeja == 1:

        print(mediana_a)
        MEDI_tres_atbilde = "jā"
    else:
        print(vid_arit_a)
        MEDI_tres_atbilde = "nē"
    MEDI_tres_uzd = input("(1 punkts) Vai dotais skaitlis ir saraksta mediāna (jā vai nē): ")
    if MEDI_tres_uzd == MEDI_tres_atbilde:
        temas_pd[2][2] = 1
    print("Ieguvi", str(sum(temas_pd[2])) ,"punktus")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
atver_failu.close()
    

