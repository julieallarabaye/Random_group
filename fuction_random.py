
ma_liste = ["Hamidé", "Nil", "Hassan", "Ezechiel", "Succès", "Elie", "Bray", "Innocent", "Hamza", "Bertrand", "Issa", "Julie", "Exaucé", "Yannick", "Sevrin", "Hyppolite", "Seraphin", "Sakayo"]
liste_randomise = []
list_randomise=[x for x in ma_liste]
groupe = 1

if len(ma_liste) > 5:
    liste_randomise = (ma_liste, 6)
else:

    for elem in liste_randomise:
     ma_liste.remove(elem)
     elem =ma_liste    
print("Groupe N° ", groupe)
print(liste_randomise)
print("----------------------------------------------------------")
groupe+=1
if ma_liste:
    print(ma_liste)
        
