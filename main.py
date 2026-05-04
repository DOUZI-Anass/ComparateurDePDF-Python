import os
import os.path
import hashlib
from shutil import copy2

def filtreOnlyPDF(liste_fichiers):
    lstFinal =[]
    for i in liste_fichiers:
        if i.lower().endswith(".pdf"):
            lstFinal.append(i)
    return lstFinal

def hashage(chemin):
    x = hashlib.sha256()
    f = open(chemin,"rb")
    while(True):
        contains =f.read(4096)
        if not contains:
            break
        x.update(contains)
    f.close()
    return x.hexdigest()


def PrepareListTotal(lstTot, path):
    tailleTotal = {}
    for i in lstTot:
        chemin = os.path.join(path, i)
        taille = os.path.getsize(chemin)
        hashh = hashage(chemin)
        if taille not in tailleTotal:
            tailleTotal[taille] = set()
        tailleTotal[taille].add(hashh)
    return tailleTotal


def trouver_nouveaux_pdf(PDF_temporaire,cheminTemp,lstTotal):
    ListePDF_a_Copier=[]
    nb_doublons = 0
    for i in PDF_temporaire:
        chemin = os.path.join(cheminTemp,i)
        sizeTemp = os.path.getsize(chemin)
        hashh = hashage(chemin)
        if sizeTemp not in lstTotal:
            lstTotal[sizeTemp] = set()
            lstTotal[sizeTemp].add(hashh)
            ListePDF_a_Copier.append(i)
        else:
            if hashh not in lstTotal[sizeTemp] : 
                lstTotal[sizeTemp].add(hashh)
                ListePDF_a_Copier.append(i)
            else:
                nb_doublons += 1
    return ListePDF_a_Copier, nb_doublons


def copiePDF(ListePDF_a_Copier,cheminTemp,destination_Resultat,destination_total):
    for i in ListePDF_a_Copier:
        destination_total_fichier = os.path.join(destination_total, i)
        destination_resultat_fichier = os.path.join(destination_Resultat, i)

        source = os.path.join(cheminTemp,i)

        copy2(source, destination_total_fichier)
        copy2(source,destination_resultat_fichier)

def viderDossierTemporaire(lstTempBeforeFiltre,cheminTemp):
    for i in lstTempBeforeFiltre:
        path = os.path.join(cheminTemp,i)
        os.remove(path)

def traiter_pdf(cheminTOT,cheminTemp,cheminResultat):
    os.makedirs(cheminResultat, exist_ok=True)
    os.makedirs(cheminTOT, exist_ok=True)
    os.makedirs(cheminTemp, exist_ok=True)

    lstTempBeforeFiltre = os.listdir(cheminTemp)
    lstTotBeforeFiltre = os.listdir(cheminTOT)

    PDF_temporaire = filtreOnlyPDF(lstTempBeforeFiltre)
    lstTot = filtreOnlyPDF(lstTotBeforeFiltre)

    index_total = PrepareListTotal(lstTot,cheminTOT)

    ListePDF_a_Copier, doublon = trouver_nouveaux_pdf(PDF_temporaire,cheminTemp,index_total)          

    copiePDF(ListePDF_a_Copier,cheminTemp,cheminResultat,cheminTOT)
       
    viderDossierTemporaire(lstTempBeforeFiltre,cheminTemp)

    return ListePDF_a_Copier, doublon


def main():
    pdf_copies, nbDoublon = traiter_pdf(
        "dossier_total",
        "dossier_temporaire",
        "dossier_resultat"
    )

    print("PDF copiés :", len(pdf_copies),"\n Doublons trouvés : ",nbDoublon)


if __name__ == "__main__":
    main()