import random
vjesalo_logo = """
     __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.     
    |  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |     
    |  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |    
    |   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |    
    |  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |    
    |__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
                                                                                    """
vjesalo =[ """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
            """,
                """
                --------
                |      |
                |      o
                |      
                |   
                |     
                -
            """,
            """
                --------
                |      |
                |      o
                |      |
                |      |
                |     
                -
            """,
            """
                --------
                |      |
                |      o
                |     \|
                |      |
                |     
                -
                
            """,
            """
                --------
                |      |
                |      o
                |     \|/
                |      |
                |     
                -
            """,
                
            """
                --------
                |      |
                |      o
                |     \|/
                |      |
                |     /
                -
            """,
            """
                --------
                |      |
                |      o
                |     \|/
                |      |
                |     / \\
                -
            """
    ]
class Rijec(object):
    __rijec_info={
        'Ako je imaš, želiš je dijeliti. Ako je podijeliš, više je nemaš.':'tajna',
        'Velik sam kao kuća, a malenog se miša bojim. Nos mi je do poda, čak i kada stojim.':'slon',
        'Kada se automobil vozi, koji se kotač ne vrti?':'rezervni',
        'Bijele koke s neba pale, cijelo selo zatrpale.':'snijeg',
        'Vodu pije, a živo nije.':'spužva',
        'Ako je mlado ostaje mlado, ako je staro ostaje staro.':'slika',
        'Bez kože uđe, sa kožom izađe.':'kruh',
        'Ako izgovoriš moje ime, više me neće biti.':'tišina',
        'Ima korijenje koje niko ne vidi, više je od najvišeg drveta, a nikad ne raste.':'planina',
        'U mraku se rađa, a s vatrom umire.':'svijeća',
        'U početku ide na četiri noge, onda na dvije, a na kraju na tri.':'čovjek',
        'Jedna glava, a stotinu kapa.':'kupus',
        'U dom unosim sunce, ali ne popravljam vid, a ipak kad me ostaviš, možeš gledati kroz zid.':'prozor',
        'Niti jurim, niti žurim, uvijek sporo idem, ali točno na vrijeme uvijek na cilj stignem.':'sat',
        'Imam oka tri, ali ni jedno ne vidi. Ali moje oči mnogo znače za pješake i vozače.':'semafor',
        'Daj mi hrane živjet ću, daj mi vode umrijet ću.':'vatra',
        'Danju svakog vjerno prati, a noću je nikad nema.':'sjena',
        'Leti nebom, ptica nije, zuji, brunda, insekt nije. Kad je žedan benzin pije, to pogoditi teško nije.':'avion',
        'Što ima jedno uho, a ne može čuti.':'igla',
        'Ja sam ogledalo za slavne, a informator za sve ostale. Pokazat ću ti svijet, ali on će biti malen.':'televizija',
        }

    @staticmethod
    def zagonetke():
        return Rijec.__rijec_info.keys()
    
    def __init__(self, zagonetka, rjesenje, pogodena = False):
        self.__zagonetka=zagonetka
        self.__rjesenje=rjesenje
        self.__pogodena=pogodena

    @property
    def zagonetka(self):
        return self.__zagonetka

    @property
    def rjesenje(self):
        return self.__rjesenje

    @property
    def pogodena(self):
        return self.__pogodena
    
    @pogodena.setter
    def pogodena(self, value):
        self.__pogodena = value

    def __repr__(self):
         return self.__class__.__name__ + '(%r, %r, %r)' % (self.__zagonetka, self.__rjesenje, self.__pogodena)

    def __str__(self):
        return self.__zagonetka + ' '+ '_ '*len(self.__rjesenje)

    def randomZagonetka(self):
        self.__zagonetka = random.choice(list(Rijec.__rijec_info.keys()))
        self.__tajnaRijec=Rijec.__rijec_info[self.__zagonetka]
        return self.__zagonetka + '|'+self.__tajnaRijec
     
    @staticmethod
    def vjesanje(pogresnaSlova, tocnaSlova, tajnaRijec):
        print(vjesalo[len(pogresnaSlova)])
        print()
        print('Pogrešna slova:', end=' ')
        for slovo in pogresnaSlova:
            print(slovo, end=' ')
        print()
        razmaci = '_' * len(tajnaRijec)
        for i in range(len(tajnaRijec)): 
            if tajnaRijec[i] in tocnaSlova:
                razmaci = razmaci[:i] + tajnaRijec[i] + razmaci[i+1:]
        for slovo in razmaci: 
            print(slovo, end=' ')
        print()

class Igrac(object):

    def __init__(self, ime):
        self.__ime=ime

    @property
    def ime(self):
        return self.__ime

    def __str__(self):
        return "Igrač " + self.__ime

    def pogodi(self,uneseno):
        while True:
            print('Unesite slovo: ')
            self.pokusaj = input()
            self.pokusaj = self.pokusaj.lower()
            if len(self.pokusaj) != 1:
                print('Unesite samo 1 slovo.')
            elif self.pokusaj in uneseno:
                print('Već ste unijeli ovo slovo, pokušajte ponovno.')
            elif self.pokusaj not in 'abcčćdđefghijklmnoprsštuvzž':
                print('Molim unesite slovo.')
            else:
                return self.pokusaj
        
class Covjek(Igrac):

    def __init__(self, ime):
        super(Covjek, self).__init__(ime)

class PrikazIgre(object):
    
    def prikaziPocetakIgre(self):
        print(vjesalo_logo)
        opcija = input ("Jesu li Vam potrebne dodatne upute za igranje? d/n: ")
        if opcija.lower().startswith('d'):
            print ("\nUpute:\n" \
                  "Sustav će generirati i prikazati jednu random zagonetku, te će se prikazati njena duljina u obliku crtica.\n" \
                  "U svakom pokušaju trebate unijeti jedno slovo i tako pogoditi određenu zagonetku. Na samom početku dodijeljeno Vam je 6 bodova.\n" \
                  "Svakom pogreškom sve ste bliže gubitku igre. Svako pogođeno slovo donosi dodatna 2 boda, svaka pogreška Vas košta 1 boda.\n" \
                   "Cilj je uz što manje pogrešaka pogoditi prikazanu zagonetku.\nSretno :) " ) 
        print ("Vrijeme je za igru!\n")

    def unesiIgraca(self):
        while True:
            ime=input("Unesite ime: ")
            if ime.strip():
                print("*"*20)
                return ime.strip()

class Igra(object):

    def __init__(self, prikaz):
        self.__prikaz=prikaz
        self.__rijec=Rijec('zagonetka','rjesenje',False)
        self.__krivaSlova=''
        self.__tocnaSlova=''
        self.__igrac=Igrac('')
        
    @property
    def prikaz(self):
        return self.__prikaz

    @property
    def rijec(self):
        return self.__rijec

    @property
    def igrac(self):
        return self.__igrac

    def igrajPonovno(self):
        print('Želite li ponovno igrati? d/n: ')
        self.odg=input().lower().startswith('d')
        return self.odg
        
    def pogadanjeSlova(self):
        string=self.rijec.randomZagonetka().split('|')
        print(string[0])
        igraZavrsena=False
        bodovi=6
        while True:
            tajnaRijec=string[1]
            self.rijec.vjesanje(self.__krivaSlova, self.__tocnaSlova, tajnaRijec)
            pokusaj = self.igrac.pogodi(self.__krivaSlova + self.__tocnaSlova)
            if pokusaj in tajnaRijec:
                self.__tocnaSlova = self.__tocnaSlova + pokusaj
                bodovi+=2
                pronadenaSvaSlova = True
                for i in range(len(tajnaRijec)):
                    if tajnaRijec[i] not in self.__tocnaSlova:
                        pronadenaSvaSlova = False
                        break
                if pronadenaSvaSlova:
                    print('Bravo! Tajna riječ je: "' + tajnaRijec + '"! Pobijedili ste!')
                    print("Bodovi: " + str(bodovi))
                    igraZavrsena = True
            else:
                bodovi-=1
                self.__krivaSlova = self.__krivaSlova + pokusaj
                if len(self.__krivaSlova) == len(vjesalo) - 1:
                    self.rijec.vjesanje(self.__krivaSlova, self.__tocnaSlova, tajnaRijec)
                    print('Žao nam je, iskoristili ste sve pokušaje.\nBroj pogrešaka: ' + str(len(self.__krivaSlova)) + '\nBroj točnih: ' +str(len(self.__tocnaSlova)) + '\nTočna riječ je: "' + tajnaRijec + '"')
                    print("Bodovi: " + str(bodovi))
                    igraZavrsena = True
            if igraZavrsena:
                if igra.igrajPonovno():
                    self.__krivaSlova = ''
                    self.__tocnaSlova = ''
                    igraZavrsena = False
                    bodovi=6
                    string=self.rijec.randomZagonetka().split('|')
                    print(string[0])
                    tajnaRijec=string[1]
                else:
                    break

    def igranjeVjesala(self):
        self.prikaz.prikaziPocetakIgre()
        self.prikaz.unesiIgraca()
        self.pogadanjeSlova()

prikaz=PrikazIgre()
igra=Igra(prikaz)
igra.igranjeVjesala()   
