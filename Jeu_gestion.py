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
        self.__compte_jour = 0
        self.__grille = [".",".",".",".",".",".",".",".","."]
    def grille_parcelle (self):

        if self.__etat == 0 or 1:
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
            print("      ",self.__type)
            print("")
            print("=======================")
            print("|| ",Fore.BLUE+self.__grille[0],Style.RESET_ALL,"|| ",Fore.BLUE+self.__grille[1],Style.RESET_ALL,"|| ",Fore.BLUE+self.__grille[2],Style.RESET_ALL,"||")
            print("=======================")
            print("|| ",Fore.BLUE+self.__grille[3],Style.RESET_ALL,"|| ",Fore.BLUE+self.__grille[4],Style.RESET_ALL,"|| ",Fore.BLUE+self.__grille[5],Style.RESET_ALL,"||")
            print("=======================")
            print("|| ",Fore.BLUE+self.__grille[6],Style.RESET_ALL,"|| ",Fore.BLUE+self.__grille[7],Style.RESET_ALL,"|| ",Fore.BLUE+self.__grille[8],Style.RESET_ALL,"||")
            print("=======================")
            print("")
            print("")

        if self.__etat == 3 :
            print("")
            print("      ",self.__type)
            print("")
            print("=======================")
            print("|| ",Fore.YELLOW+self.__grille[0],Style.RESET_ALL,"|| ",Fore.YELLOW+self.__grille[1],Style.RESET_ALL,"|| ",Fore.YELLOW+self.__grille[2],Style.RESET_ALL,"||")
            print("=======================")
            print("|| ",Fore.YELLOW+self.__grille[3],Style.RESET_ALL,"|| ",Fore.YELLOW+self.__grille[4],Style.RESET_ALL,"|| ",Fore.YELLOW+self.__grille[5],Style.RESET_ALL,"||")
            print("=======================")
            print("|| ",Fore.YELLOW+self.__grille[6],Style.RESET_ALL,"|| ",Fore.YELLOW+self.__grille[7],Style.RESET_ALL,"|| ",Fore.YELLOW+self.__grille[8],Style.RESET_ALL,"||")
            print("=======================")
            print("")
            print("")

        if self.__etat == 4 :
            print("")
            print("      ",self.__type)
            print("")
            print("=======================")
            print("|| ",Fore.GREEN+self.__grille[0],Style.RESET_ALL,"|| ",Fore.GREEN+self.__grille[1],Style.RESET_ALL,"|| ",Fore.GREEN+self.__grille[2],Style.RESET_ALL,"||")
            print("=======================")
            print("|| ",Fore.GREEN+self.__grille[3],Style.RESET_ALL,"|| ",Fore.GREEN+self.__grille[4],Style.RESET_ALL,"|| ",Fore.GREEN+self.__grille[5],Style.RESET_ALL,"||")
            print("=======================")
            print("|| ",Fore.GREEN+self.__grille[6],Style.RESET_ALL,"|| ",Fore.GREEN+self.__grille[7],Style.RESET_ALL,"|| ",Fore.GREEN+self.__grille[8],Style.RESET_ALL,"||")
            print("=======================")
            print("")
            print("")

    def changement_etat (self):

            print("")
            print("1) Planter des graines dans la parcelle ? ")
            print("2) Arroser votre parcelle ? ")
            print("3) Mettre de l'engrais ? ")
            print("4) Récolter la parcelle ? ")
            print("5) Aller se coucher ? ")
            print("")
            self.__choix = int(input("Que voulez vous faire ? "))
            print("")
            print("")

            if self.__choix == 1 :
                self.__etat = 1

            if self.__choix == 2 and self.__compte_jour == 2 :
                self.__etat = 2
            if self.__choix == 2 and self.__etat == 0 :
                print("Vous n'avez pas encore planté de graine !")

            if self.__choix == 3 and  self.__compte_jour == 3 :
                self.__etat = 3
            if self.__choix == 3 and self.__etat == 0 and 1: 
                print("Vous ne pouvez pas mettre d'engrais tant que vous n'avez pas arroser votre parcelle !")

            if self.__choix == 4 and self.__compte_jour == 4 :
                self.__etat = 4
            if self.__choix == 4 and self.__etat == 0 and 2 :
                print("Votre graine ne poussera pas tant que vous n'avez pas mis d'engrais !")


    def etat_parcelle (self):
        if self.__etat == 1 :
            print("Vous avez plantez des graines dans votre parcelle.")
            self.__grille = ["*","*","*","*","*","*","*","*","*"]
        if self.__etat == 2 :
            self.__grille = ["*","*","*","*","*","*","*","*","*"]
            print("Vous avez arroser votre parcelle.")
        if self.__etat == 3 :
            self.__grille = ["*","*","*","*","*","*","*","*","*"]
            print("Vous avez mis de l'engrais sur votre parcelle.")
        if self.__etat == 4 :
            print("Vous avez recolté votre parcelle")
            self.__grille = ["࿈","࿈","࿈","࿈","࿈","࿈","࿈","࿈","࿈"]
            
            




parcelle_1=Parcelle_1("Carottes")
parcelle_1.grille_parcelle()
parcelle_1.changement_etat()
parcelle_1.etat_parcelle()
parcelle_1.grille_parcelle()
print("⌚")



#jack = Joueur("Jack")
#parcelle1 = Parcelle("Parcelle1")
#parcelle1.choix_joueur()

