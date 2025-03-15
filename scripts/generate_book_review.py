import os
from datetime import datetime

def get_input(prompt, default=None):
    if default:
        prompt = f"{prompt} (default: {default}): "
    user_input = input(prompt)
    return user_input if user_input else default

def generate_book_md():
    print("Générateur de fiche de livre")
    
    # Ask for basic details
    title = get_input("Titre de l'œuvre", "Titre par défaut")
    author = get_input("Auteur", "Auteur par défaut")

    # Crée le titre du fichier en fonction de la date et du titre de l'œuvre
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{title.replace(' ', '-').lower()}.md"

    # Chemin vers le dossier _posts depuis le dossier scripts
    posts_dir = os.path.join(os.path.dirname(__file__), '..', '_posts')

    # Crée le dossier _posts s'il n'existe pas
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    # Crée le contenu du fichier Markdown
    content = f"""---
layout: book
category: book
title: "{title} - {author}"
author: {author}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: []
work_title: {title}
work_author: {author}
work_publisher: 
ean: 
work_publish_date: 
genre:
cover: 
rating: 
ownership_status: 
progress_status: 
start_date: 
end_date:
---
## Résumé

## Notes personnelles

"""

    # Chemin complet du fichier à créer dans _posts
    file_path = os.path.join(posts_dir, filename)

    # Crée le fichier dans le dossier _posts
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fiche de livre générée : {file_path}")

if __name__ == "__main__":
    generate_book_md()
