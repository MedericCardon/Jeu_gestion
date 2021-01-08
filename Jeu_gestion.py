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
    def etat_parcelle (self):
        if self.__etat == 1 :
            print("Vous avez plantez des graines dans votre parcelle")
            self.__grille = ["*","*","*","*","*","*","*","*","*"]
            



parcelle_1=Parcelle_1("Carottes")
parcelle_1.grille_parcelle()
parcelle_1.changement_etat()
parcelle_1.etat_parcelle()
parcelle_1.grille_parcelle()


#jack = Joueur("Jack")
#parcelle1 = Parcelle("Parcelle1")
#parcelle1.choix_joueur()

