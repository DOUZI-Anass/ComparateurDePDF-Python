import tkinter as tk
from tkinter import Label, filedialog
import main

def bouton_Temp():
    global cheminTemp
    cheminTemp = filedialog.askdirectory()
    label_temp.config(text=cheminTemp)

def bouton_Total():
    global cheminTot
    cheminTot = filedialog.askdirectory()
    label_total.config(text=cheminTot)

def bouton_Resultat():
    global cheminResultat
    cheminResultat = filedialog.askdirectory()
    label_Resultat.config(text=cheminResultat)

def lancerTraitement():
    if cheminResultat == "" or cheminTemp =="" or cheminTot=="":
        labelFinal.config(text="Veuiller selectionner tout les dossiers")
        return
    pdfCopier, nbDoublons = main.traiter_pdf(cheminTot,cheminTemp,cheminResultat)
    labelFinal.config(text=str(len(pdfCopier))+" PDF copié \n et \n"+str(nbDoublons)+" doublons détectés")


fenetre = tk.Tk()
couleur_fond ="#F4F7FB"

fenetre.title("Filtreur De PDF")
titre = tk.Label(fenetre, text ="Comparateur intelligent de PDF", font=("Arial",20,"bold"),bg=couleur_fond)
titre.pack()

fenetre.geometry('900x450')
fenetre.configure(bg=couleur_fond)

cheminTemp = ""
cheminTot = ""
cheminResultat = ""

label_Explication = tk.Label(fenetre, text="Cet outil compare les PDF d’un dossier à analyser avec ceux d’un dossier principal.\n" 
                             "Les PDF nouveaux sont copiés dans le dossier de sortie et ajoutés au dossier principal.\n"
                            "Le dossier à analyser est vidé à la fin.",
                            wraplength=700,
                            justify="center",font=("Arial", 10), bg=couleur_fond)
label_Explication.pack(pady=10)


cadre_btn = tk.Frame(fenetre,bg=couleur_fond)
cadre_btn.pack(pady=10, fill="x", padx=40)
cadre_btn.columnconfigure(0, weight=1)
cadre_btn.columnconfigure(1, weight=1)
cadre_btn.columnconfigure(2, weight=1)


tk.Button(cadre_btn,text="Dossier à analyser : nouveaux PDF à vérifier", command=bouton_Temp, bg=couleur_fond, cursor="hand2").grid(row=0, column=0, padx=10, sticky="ew")
label_temp = tk.Label(cadre_btn, text="Aucun dossier choisie",bg=couleur_fond, wraplength=220)
label_temp.grid(row=1, column=0, pady=8)

tk.Button(cadre_btn, text="Dossier de sortie : PDF uniques trouvés", command=bouton_Resultat, bg=couleur_fond, cursor="hand2").grid(row=0, column=1, padx=10, sticky="ew")
label_Resultat = tk.Label(cadre_btn,text="Aucun dossier choisie",bg=couleur_fond,wraplength=220)
label_Resultat.grid(row=1, column=1, pady=8)

tk.Button(cadre_btn, text="Dossier principal : PDF déjà enregistrés", command=bouton_Total, bg=couleur_fond, cursor="hand2").grid(row=0, column=2,padx=10, sticky="ew")
label_total = tk.Label(cadre_btn,text="Aucun dossier choisie", bg=couleur_fond, wraplength=220)
label_total.grid(row=1, column=2, pady=8)

labelFinal = tk.Label(fenetre, text="",bg=couleur_fond)
labelFinal.pack()
tk.Button(fenetre,text="LANCER", command=lancerTraitement, width=25, bg="#00FF38", font=("Arial",12 ,"bold"),cursor="hand2").pack()



fenetre.mainloop()