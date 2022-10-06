from random import *
import ctypes  
handle = ctypes.windll.kernel32.GetStdHandle(-11) 
for i in range(2):  
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, i) # on change la couleur  

def calcul_critique(degats,critique,monstre):
    degats=degats*3
    monstre = monstre-degats
    print("COUP CRITIQUE !!!")
    return degats,monstre




attaque = "back"
monstre = 150
pvTotalMonstre = 150
nomMonstre = " 🦍 Gorilles énervés"
TourPoison = 0
N=5
fuite = 0
fireball = 25
lighting = 30
heal = 30
Resistance = 1
rang = "zero"
degats  = 0
poison = 10
timer =0
critique= randint(1,10)
mana = 125
manaTotal = 125
coupEpee = 0
pvjoueur=250
pvTotalJoueur = 250
attaqueMonstre=15
yesno = 0
nomJoueur = ""

nomJoueur = (input("Choisir nom joueur : "))
transition="============================================================================================================================================="
while monstre > 0 and pvjoueur >0 and fuite == 0:
    print("=== TOUR ",timer," ====")
    for i in range(7):  
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, i) # on change la couleur  

    critique= randint(1,10)
    print(transition)
    print("🙂 ",nomJoueur,"| Mana :",mana,"/",manaTotal,"(+5/Tour)","| PV : ",pvjoueur,"/",pvTotalJoueur,"     ⚔ ⚔ ⚔ VS ⚔ ⚔ ⚔     ",nomMonstre,"| PV :", monstre,"/",pvTotalMonstre )
    while attaque == "back" or attaque == "Sort" :
        print("Choisir attaque joueur :Sort    Coup d'épée (15DEG:0MAN)")
        attaque = (input("                        Parer   Fuir       : "))
        print(transition)
        if attaque == "Sort":
            print("Choisir attaque joueur :fireball (25DEG:15MAN)    lighting (35DEG:25MAN)")
            attaque = (input("                        heal (30REG:20MAN)        poison (10DEG/tour:20MAN)    back : "))
            print(transition)
    
    print(transition)
    for i in range(2):  
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, i) # on change la couleur  
    #Partie sort
    if attaque == "fireball" and mana>19 :
        mana = mana-20
        degats = fireball
        critique=7
        print("jet de dé à critique  🎲 ",critique)
        if critique == 7:
            calcul_critique(degats,critique,monstre)
        else:
            degats = fireball
            monstre = monstre - fireball

    elif attaque == "lighting" :
        mana = mana-25
        print("jet de dé à critique  🎲 ",critique)
        if critique == 7:
            degats = lighting *3
            monstre = monstre - lighting *3
            print("COUP CRITIQUE !!")
        else:
            degats = lighting 
            monstre = monstre - lighting

    elif attaque == "poison" :
        mana = mana-20
        degats = 0
        print("jet de dé pour déterminer le nombre de tours de poison  🎲 ",critique)
        TourPoison = critique

    elif attaque == "heal" :
        mana = mana-15
        degats = 0
        print("jet de dé à critique  🎲 ",critique)
        if critique == 7:
            pvjoueur = pvjoueur+ heal*3
            print("COUP CRITIQUE !!")
            MontantSoin = 20*3
        else:
            degats = 0
            pvjoueur = pvjoueur+ heal 
            MontantSoin = heal
        print("Vous vous êtes soigné de",MontantSoin) 
    #Partie sort

    #partie coup d'épée
    elif attaque == "Coup d'épée" :
        coupEpee = 15
        print("jet de dé à critique  🎲 ",critique)
        if (critique == 7):
            degats=coupEpee*3
            monstre = monstre - coupEpee*3
            print("COUP CRITIQUE !!")
        else :
            degats=coupEpee
            monstre = monstre - coupEpee
    #partie coup d'épée

    #partie parer
    elif attaque == "Parer" :
        Resistance = 2
        degats = 0
        print("Vous vous protéger ainsi tous dégats reçu par le joueur est divisé par 2 pour ce tour seulement")
    #partie parer

    #partie fuite
    elif attaque == "Fuir":
        print("Tentative de fuite")
        degats = 0
        fuite = 1
        break
    #partie fuite
    
    
    else :
        print("Veuillez entrez une attaque valide")

    print("le monstre  s'est prit",degats,"de dégats ","Pv actuel du monstre :",monstre)
    if TourPoison>0:
        monstre = monstre-10
        print("le monstre  s'est prit",poison,"de dégats d'empoisonnement, (tours restants :",TourPoison,")","Pv actuel du monstre :",monstre)
    TourPoison = TourPoison-1
    #partie monstre
    if monstre < pvTotalMonstre/4 and monstre > 1 :
        monstre = monstre+10
        attaqueMonstre=attaqueMonstre*2/Resistance
        pvjoueur=pvjoueur-attaqueMonstre
        if yesno == 0:
            print("Le monstre se sent acculé sa régénération augmente de 5 et son attaque augmente de 10")
        yesno = 1
        print("le monstre vous attaque vous avez prit",attaqueMonstre,"il vous reste",pvjoueur,"HP") 
        if (monstre > pvTotalMonstre) :
            monstre = pvTotalMonstre
        print("le monstre  a regen, Pv actuel du monstre",monstre)
    
    elif monstre <=pvTotalMonstre/2 and monstre >= pvTotalMonstre/4 :
        attaqueMonstre=(attaqueMonstre+5)/Resistance
        monstre = monstre+7
        print("Le monstre est dans un état neutre")
        pvjoueur=pvjoueur-attaqueMonstre
        print("le monstre vous attaque vous avez prit",attaqueMonstre,"il vous reste",pvjoueur,"HP")
        if (monstre > pvTotalMonstre) :
            monstre = pvTotalMonstre
        print("le monstre  a regen, Pv actuel du monstre",monstre) 

    elif monstre >pvTotalMonstre/2 :
        attaqueMonstre=attaqueMonstre/Resistance
        monstre = monstre+5
        print("Le monstre vous sous estime")
        pvjoueur=pvjoueur-attaqueMonstre
        print("le monstre vous attaque vous avez prit",attaqueMonstre,"il vous reste",pvjoueur,"HP")
        if (monstre > pvTotalMonstre) :
            monstre = pvTotalMonstre
        print("le monstre  a regen, Pv actuel du monstre",monstre) 
    if (monstre <= 0) :
        monstre = 0
    if (pvjoueur <= 0) :
        pvjoueur = 0
    #partie monstre

    timer+=1
    attaque = "back"
    Resistance = 1



    mana = mana+5
    if mana >manaTotal :
        mana = manaTotal
    if pvjoueur >pvTotalJoueur :
        pvjoueur = pvTotalJoueur

#si gagner
if(monstre == 0) :
    for i in range(6):  
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, i)
    print(transition)   
    print("Le monstre est vaincu vous êtes victorieux")
    if timer <= 4:
        rang ="S"
    elif timer >4 and timer<=8:
        rang = "A"
    elif timer >8 and timer<=12:
        rang = "B"
    elif timer >12 and timer<=15:
        rang = "C"
    elif timer >15 :
        rang = "D"
    print("Vous avez mis",timer," tours a tuer le monstre vous obtenez le rang ",rang)
    
    print(" __     ______  _    _  __          _______ _   _ ")
    print(" \ \   / / __ \| |  | | \ \        / /_   _| \ | |")
    print("  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |")
    print("   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |")
    print("    | | | |__| | |__| |    \  /\  /   _| |_| |\  |")
    print("    |_|  \____/ \____/      \/  \/   |_____|_| \_|")
    print(transition) 
elif(pvjoueur ==0):
    for i in range(5):  
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, i)
  #si gagner
    
 #si perdu                               
    print(" __ __              _ _       _ ")
    print("|  |  |___ _ _    _| |_|___ _| |")
    print("|_   _| . | | |  | . | | -_| . |")
    print("  |_| |___|___|  |___|_|___|___|")
    print("                                ")
    print("=======================================================================")
    print("   _____          __  __ ______    ______      ________ _____   ")
    print("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \  ")
    print(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | ")
    print(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /  ")
    print(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \  ")
    print("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ")
    print("========================================================================")
#si perdu

#si enfui
else :
    print(transition)
    print("Tu t'es enfui comme un couard")
    print(transition)
#si enfui
for i in range(8):  
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, i)        
        
        
                
