import numpy as np
import matplotlib.pyplot as plt

die, probabilities = [1,2,3,4,5,6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

def Damage_sim(Unit_attacks, Unit_damage, Enemy_saves):
    damages=[]
    for i in range(10000):
        Shooting=0
        for j in range(Unit_attacks[1]):
            outcome=np.random.choice(die, size=1, p=probabilities)
            if outcome>=Unit_attacks[0]:
                Shooting+=1
        Wounding=0
        for j in range(Shooting):
            outcome=np.random.choice(die, size=1, p=probabilities)
            if outcome>=Enemy_saves[0]:
                Wounding+=1
        Damaging=0
        for j in range(Wounding):
            outcome=np.random.choice(die, size=1, p=probabilities)
            if outcome>=Enemy_saves[1]:
                Damaging+=1
        Total_damage=0
        for j in range(Damaging):
            damage_per=Unit_damage[0]
            if len(Unit_damage)>1:
                damage_per=np.random.choice(Unit_damage, size=1, p=probabilities)
            Total_damage+=int(damage_per)
        final_damage=Total_damage
        if Enemy_saves[2]>0:
            for j in range(Total_damage):
                outcome=np.random.choice(die, size=1, p=probabilities)
                if outcome>=Enemy_saves[2]:
                    final_damage-=1

        # Increment `wins` by 1 if the dice show same number
        #print('total :', Total_damage)
        damages.append(final_damage)
    return damages

    
if __name__=="__main__":
    # Initialize model parameters & simulate dice throw
    #np.random.seed(111)
    #Write a for loop to repeat throwing the dice.

    #Ballistic Skill, number of attacks
    ghostkeel_attacks=[3, 5]
    ghostkeel_damage=[3,4,5,6,7,8]


    rip_attacks_ion=[3,8]
    rip_damage_ion=[4]
    rip_at_plasma=[3,2]
    rip_dam_plasma=[4]

    #Wounding roll, Invuln Save, FNP
    tyranid_Inv=[4,4,5]

    Ghost_damage = Damage_sim(ghostkeel_attacks, ghostkeel_damage, tyranid_Inv)
    GDamageDict=unique, counts = np.unique(Ghost_damage, return_counts=True)
    print('Ghostkeel Damages: ',GDamageDict)

    Rip_ion_dam=Damage_sim(rip_attacks_ion, rip_damage_ion, tyranid_Inv)
    Rip_plasma_dam=Damage_sim(rip_at_plasma, rip_dam_plasma, tyranid_Inv)

    Rip_dam=np.add(Rip_ion_dam, Rip_plasma_dam)
    RDamageDict=unique, counts = np.unique(Rip_dam, return_counts=True)
    print('Riptide Damages: ',RDamageDict)
