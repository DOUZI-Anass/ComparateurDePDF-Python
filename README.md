# 📄 ComparateurDePDF

**ComparateurDePDF** est une application Python avec interface graphique permettant de comparer automatiquement des fichiers PDF entre deux dossiers.  
Elle détecte les doublons grâce à un système de hash (SHA-256) et copie uniquement les fichiers uniques.

---

##  Fonctionnalités

- Détection des doublons basée sur le contenu (SHA-256)
- Comparaison entre un dossier principal et un dossier temporaire
- Copie automatique des nouveaux fichiers PDF uniques
- Mise à jour du dossier principal
- Nettoyage automatique du dossier temporaire après traitement
- Interface graphique simple (Tkinter)

---

##  Interface

L’application propose une interface intuitive permettant de :

- Sélectionner les dossiers
- Lancer le traitement en un clic
- Visualiser le nombre de fichiers copiés

---

##  Technologies utilisées

- **Python**
- **Tkinter** (interface graphique)
- **Hash SHA-256** (détection de doublons)
- **PyInstaller** (création de l’exécutable)

---

##  Installation (version développeur)

1. Cloner le projet :
```bash
git clone https://github.com/TON-USERNAME/ComparateurDePDF.git
cd ComparateurDePDF
```
2. Lancer l’interface :
python interface.py

## Utilisation (exécutable)

1. Télécharger le fichier `.exe` depuis l’onglet Releases  
2. Lancer `ComparateurDePDF.exe`  
3. Sélectionner :
   - Dossier principal (PDF déjà enregistrés)
   - Dossier à analyser (nouveaux PDF)
   - Dossier de sortie  
4. Cliquer sur LANCER

## Attention

Le dossier temporaire est vidé automatiquement après le traitement.  
Assurez-vous de ne pas y laisser de fichiers importants.

---

## Structure du projet
```
ComparateurDePDF/
├── main.py
├── interface.py
├── README.md
└── .gitignore
```
---

## Améliorations possibles

- Ajout d’une barre de progression
- Gestion des sous-dossiers
- Amélioration du design de l’interface
- Export des logs de traitement

---

## Licence

Projet personnel réalisé dans un objectif d’auto-apprentissage et de démonstration.

---

## Auteur

DOUZI Anass
