from colorama import Fore, Back, Style
print(Fore.WHITE + 'some red text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


class Joueur :
    def __init__ (self,nom):
        self.__argent = 100
        self.__repos = False
        self.__choix = 0
        self.__nom = nom
        self.__graines = 0
    

class Parcelle_1 :
    def __init__(self,plante):
        self.__type = plante
        self.__etat = 0
        self.__choix = 0
        self.__grille = [".",".",".",".",".",".",".",".","."]
    def grille_parcelle (self):
        if self.__etat == 0 :
            print("")
            print("   ",self.__type)
            print("")
            print("=================")
            print("||",self.__grille[0],"||",self.__grille[1],"||",self.__grille[2],"||")
            print("=================")
            print("||",self.__grille[3],"||",self.__grille[4],"||",self.__grille[5],"||")
            print("=================")
            print("||",self.__grille[6],"||",self.__grille[7],"||",self.__grille[8],"||")
            print("=================")
            print("")
            print("")

        if self.__etat == 2 :
            print("")
            print("     ",self.__type)
            print("")
            print("====================")
            print("||",Fore.BLUE+self.__grille[0],Style.RESET_ALL,"||",Fore.BLUE+self.__grille[1],Style.RESET_ALL,"||",Fore.BLUE+self.__grille[2],Style.RESET_ALL,"||")
            print("====================")
            print("||",Fore.BLUE+self.__grille[3],Style.RESET_ALL,"||",Fore.BLUE+self.__grille[4],Style.RESET_ALL,"||",Fore.BLUE+self.__grille[5],Style.RESET_ALL,"||")
            print("====================")
            print("||",Fore.BLUE+self.__grille[6],Style.RESET_ALL,"||",Fore.BLUE+self.__grille[7],Style.RESET_ALL,"||",Fore.BLUE+self.__grille[8],Style.RESET_ALL,"||")
            print("====================")
            print("")
            print("")


    def changement_etat (self):
        print("")
        print("1) Planter des graines dans la parcelle ? ")
        print("2) Arroser votre parcelle ? ")
        print("3) Mettre de l'engrais ? ")
        print("4) Récolter la parcelle ? ")
        print("")
        self.__choix = int(input("Que voulez vous faire ? "))
        print("")
        print("")
        if self.__choix == 1 :
            self.__etat = 1
        if self.__choix == 2 :
            self.__etat = 2
    def etat_parcelle (self):
        if self.__etat == 1 :
            print("Vous avez plantez des graines dans votre parcelle")
            self.__grille = ["*","*","*","*","*","*","*","*","*"]
        if self.__etat == 2 :
            self.__grille = ["*","*","*","*","*","*","*","*","*"]
            print("Vous avez arroser votre parcelle.")
            
            
            
            



parcelle_1=Parcelle_1("Carottes")
parcelle_1.grille_parcelle()
parcelle_1.changement_etat()
parcelle_1.etat_parcelle()
parcelle_1.grille_parcelle()



#jack = Joueur("Jack")
#parcelle1 = Parcelle("Parcelle1")
#parcelle1.choix_joueur()

