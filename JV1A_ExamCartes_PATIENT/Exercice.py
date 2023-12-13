# Créer une carte.
class carte :
    def __init__ (self,mana,nom,description):
        self.__mana=mana
        self.__nom=nom
        self.__description=description
    def getMana (self):
        return self.__mana
    def getNom (self):
        return self.__nom
    def getDescription (self):
        return self.__description

# Créer un(e) Mage. 
# J'imagine ici que le deck ne pourra dépasser 4 cartes (comme il n'y aura que 4 cartes qui seront créées.)  
class mage :
    def __init__ (self, nomMage, pvMage, total, manaMage):
        self.__nomMage=nomMage
        self.__pvMage=pvMage
        self.__total=total
        self.__manaMage=manaMage

        self.__deck=[0,0,0,0]
        self.__defausse=[0,0,0]
        self.__zoneJeu=[0,0,0,0]

    def getNom (self):
        return self.__nomMage
    def getPv (self):
        return self.__pvMage
    def getTotal (self):
        return self.__total
    def getMana (self):
        return self.__manaMage

    # Liens aux actions du joueur.
    def getDeck (self):
        return self.__deck
    def getDefausse (self):
        return self.__defausse
    def getZoneJeu (self):
        return self.__zoneJeu

    # Actions du joueur.
    def jouerCarte (self, choix, carte_choisie):
        self.__mana -= carte_choisie.getMana()
        self.__zoneJeu = self.__deck[choix]
        self.__deck.pop(choix)

    def gainMana (self):
        self.__mana += 5

    def attaquer (self, carte_choisie):
        carte_choisie.attaque()

# Créer une carte Cristal.
class cristal (carte):
    def __init__(self,mana,nom,description, valeur):
        super().__init__(mana,nom,description)
        self.__valeur=valeur
    def getValeur (self):
        return self.__valeur
    def jouer (self, choix, joueur):
        if choix == 1 :
            total = joueur.getTotal()
            total += self.__valeur

# Créer une carte Créature.
class creature (carte):
    def __init__(self,mana,nom,description,pv,scoreAtk):
        super().__init__(mana,nom,description)
        self.__pv=pv
        self.__scoreAtk=scoreAtk

    def getPv (self):
        return self.__pv
    def getScoreAtk (self):
        return self.__scoreAtk
    

    def jouer (self, joueur):
        mana = joueur.getMana()
        mana -= self.__mana

    def attaque (self, adversaire):
        pv_adversaire = adversaire.getPv()
        pv_adversaire -= self.__scoreAtk

    def pertePV (self, joueur, adversaire, carte_choisie):
        self.__pv -= adversaire.scoreAtk()
        if self.__pv <= 0 :
            defausse_joueur = joueur.getDefausse()
            defausse_joueur = joueur.getDeck[carte_choisie]
            joueur.getDeck().pop[carte_choisie]

# Créer une carte Blast.  
class blast (carte):
    def __init__(self,mana,nom,description,valeur):
        super().__init__(mana,nom,description)
        self.__valeur=valeur

    def getValeur (self):
        return self.__valeur
    
    def lancé (self, adversaire, joueur, carte_choisie):
        pv_adversaire = adversaire.getPv()
        defausse_joueur = joueur.getDefausse()
        pv_adversaire -= self.__valeur
        defausse_joueur = joueur.getDeck[carte_choisie]
        joueur.getDeck().pop[carte_choisie]



cartes = [
    cristal(5, "Pierre de lune", "un cristal permettant d'obtenir +10 de Mana maximum.", 10),
    creature(10, "La terreur des obscurités", "une creature peut amicale. Peut faire une atk de 5.", 15, 5),
    creature(20, "Le verre enchanté", "une creature bien silencieuse. Peut faire une atk de 10.", 5, 10),
    blast(15, "Effet de feu", "permet de faire une attaque de 7.", 7)
]

## Si le jeu se fait par combat entre un joueur et une créature.
# Définir le joueur et l'adversaire.

nom_joueur = input("Joueur 1, veuillez entrer votre nom. \n")
joueur = mage(nom_joueur, 15, 20, 20)
adversaire = creature(25, "La catastrophe", "une creature vraiment maladroite. Peut faire une atk de 8.", 20, 8)


# Présentation du combat.

print ("Vous possédez 4 cartes.")
print (cartes[0].getNom(), cartes[0].getDescription(), "mana", cartes[0].getMana(), "valeur" , cartes[0].getValeur())
print (cartes[1].getNom(), cartes[1].getDescription(), "mana", cartes[1].getMana(), "pv" , cartes[1].getPv(), "et atk", cartes[1].getScoreAtk)
print (cartes[2].getNom(), cartes[2].getDescription(), "mana", cartes[1].getMana(), "pv" , cartes[2].getPv(), "et atk", cartes[2].getScoreAtk)
print (cartes[3].getNom(), cartes[3].getDescription(), "mana" , cartes[3].getMana(), "valeur", cartes[3].getValeur())

# print ("Votre adversaire est", adversaire.getNom(),",", adversaire.getDescription(), "avec mana", adversaire[1].getMana(), "pv" , adversaire.getPv(), "et atk", adversaire.getScoreAtk())

print ("Prêt ? Combattez !")

# Faire le combat.

while adversaire.getPv() > 0 :

    print (joueur.getNom(), ", quelle action voulez-vous faire ? \n")
    choix = int(input(("1 : Jouer une carte  2 : Attaquer \n")))
    if choix == 1 :
        print ("Quelle carte voulez-vous jouer ?")
        choix_02 = int(input(("1 :", cartes[0].getNom(),  " 2 :", cartes[1].getNom(),  "3 :", cartes[2].getNom(),  " 4 :", cartes[3].getNom() )))
        joueur.jouerCarte(cartes[choix_02])
    if choix == 2 :
        print ("Quelle créature ?")
        choix_02 = int(input(("1 :", cartes[1].getNom(), " 2:", cartes[2].getNom())))
        if choix_02 == 1 :
            joueur.attaquer(cartes[1])
        if choix_02 == 2 :
            joueur.attaquer(cartes[2])

    adversaire.attaque(joueur)
    joueur.gainMana()
    print ("Vous avez", joueur.getMana(), "de mana.")

print ("L'adversaire est à terre. Vous avez gagnez, félicitations !")


# Si + de temps : mettre que certains choix possibles QUE SI déjà une carte mise créature par exemple ...