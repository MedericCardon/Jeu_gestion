class Joueur :
    def __init__ (self,nom):
        self.__argent = 100
        self.__repos = False
        self.__choix = 0
        self.__nom = nom
        self.__graines = 0
    

class Parcelle :
    def __init__ (self,nom_parcelle):
        self.__nom = nom_parcelle
        self.__repos_parcelle = False
        self.__etat = 0
    def choix_joueur (self):
        while self.__etat < 5 :
            print("1) Planter des graines")
            print("2) Arroser votre parcelle")
            print("3) Récolter votre parcelle")
            print("4) Aller dormir")
            print("")
            print("")
            self.__choix = int(input("Que voulez vous faire ?"))
            if self.__choix == 1 :
                print("Vous venez de planter des graines dans votre parcelle")
                print("")
                self.__etat = 1

            if self.__etat < 2 and self.__choix ==2:
                print("Vous ne pouvez pas arroser votre parcelle")
                print("")
                if self.__choix == 2 and self.__etat > 2:
                    print("Vous venez d'arroser votre parcelle")
                    print("")
                

            if self.__choix == 3 :
                print("Vous avez récolté votre parcelle")
                print("")

            if self.__choix == 4 :
                print("Vous allez vous coucher")
                print("")
                self.__etat = 2 
    



jack = Joueur("Jack")

parcelle1 = Parcelle("Parcelle1")
parcelle1.choix_joueur()

