import os
from datetime import datetime

# Demande les informations nécessaires
title = input("Titre du livre : ")
author = input("Auteur : ")
publisher = input("Éditeur : ")
ean = input("EAN : ")
status = input("Statut de lecture (Lu, En cours, À lire) : ")
start_date = input("Date de début de lecture (AAAA-MM-JJ) : ")
end_date = input("Date de fin de lecture (AAAA-MM-JJ) : ")
review = input("Ton avis sur le livre : ")
rating = input("Ta note (1 à 5) : ")

# Crée le titre du fichier en fonction de la date et du titre du livre
date_str = datetime.now().strftime("%Y-%m-%d")
filename = f"_posts/{date_str}-{title.replace(' ', '-').lower()}.md"

# Crée le contenu du fichier Markdown
content = f"""---
layout: post
title: "{title}"
author: "Ton nom ou pseudo"
date: {datetime.now().strftime('%Y-%m-%d')}
categories: [livre, critique]
tags: [livre, critique]
---

## Couverture du livre
![Couverture du livre](URL_de_l_image)

## Informations sur le livre
- **Titre** : {title}
- **Auteur** : {author}
- **Éditeur** : {publisher}
- **EAN** : {ean}

## Statut de lecture
- **Statut de lecture** : {status}
- **Date de début de lecture** : {start_date}
- **Date de fin de lecture** : {end_date}

## Avis personnel
{review}

## Notes
- **Ma note personnelle** : {"★" * int(rating)}{"☆" * (5 - int(rating))}
"""

# Crée le fichier dans le dossier _posts
with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Fiche de livre générée : {filename}")
