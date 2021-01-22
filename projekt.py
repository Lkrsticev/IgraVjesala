import random
vecUneseno=''
krivaSlova=''
tocnaSlova=''
bodovi=6
kraj=False 
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
                |     /\\
                -
            """
    ]
class Rijec(object):
    __rijec_info={
        'Ako je imaš, želiš je dijeliti. Ako je podijeliš, više je nemaš.':'tajna',
        'Velik sam kao kuća, a malenog se miša bojim. Nos mi je do poda, čak i kada stojim.':'slon',
        'Kada se automobil vozi, koji se kotač ne vrti?':'rezervni',
        'Bijele koke s neba pale, cijelo selo zatrpale.':'snijeg',
        'Vodu pije, a živo nije':'spužva',
        'Ako je mlado ostaje mlado, ako je staro ostaje staro':'slika',
        'Bez kože uđe, sa kožom izađe':'kruh',
        'Ako izgovoriš moje ime, više me neće biti':'tišina',
        'Ima korijenje koje niko ne vidi, više je od najvišeg drveta, a nikad ne raste':'planina',
        'U mraku se rađa, a s vatrom umire':'svijeća',
        'U početku ide na četiri noge, onda na dvije, a na kraju na tri':'čovjek',
        'Jedna glava, a stotinu kapa':'kupus',
        'U dom unosim sunce, ali ne popravljam vid, a ipak kad me ostaviš, možeš gledati kroz zid':'prozor',
        }

    @staticmethod
    def zagonetke():
        return Rijec.__rijec_info.keys()
    
    def __init__(self, zagonetka, rjesenje, pogodena=False):
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
    def zagonetka(self):
        return Rijec.__rijec_info[self.__broj][0]
    
    @property
    def rjesenje(self):
        return self.__rijec_info[self.__broj][1]

    @property
    def pogodena(self):
        return self.__pogodena
    @pogodena.setter
    def pogodena(self, value):
        self.__pogodena = value

    @staticmethod   
    def ispis():
        kljuc=random.choice(list(Rijec.__rijec_info.keys()))
        duljina=len(Rijec.__rijec_info[kljuc])
        print(kljuc +"  "+ '_ '*duljina)
        return Rijec.__rijec_info[kljuc]

class Slovo(object):
    
    def __init__(self, znak):
        self.__znak=znak

    @property
    def znak(self):
        return self.__znak


class Igrac(object):

    def __init__(self, ime):
        self.__ime=ime

    @property
    def ime(self):
        return self.__ime

    def unesiSlovo():
        while True:
            print('Pogodite slovo!')
            slovo = input()
            slovo = slovo.lower()
            slovo=slovo.lower()
            if len(slovo)!=1:
                print("Unesite jedno slovo: ")
            elif slovo not in 'abcćčdđefghijklmnopqrsštuvzž':
                print("Unesite slovo: ")
            else:
                return slovo
        
class Covjek(Igrac):

    def __init__(self, ime):
        super(Covjek, self).__init__(ime)

class PrikazIgre()

    @staticmethod
    def prikaziPocetakIgre():
        print("*"*30+" IGRA VJEŠALA "+"*"*30)

    @staticmethod
    def unesiIgraca():
        while True:
            ime=input("Unesi ime: ")
            if ime.strip():
                print("*"*50)
                return ime.strip()
