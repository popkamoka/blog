import os
from datetime import datetime

def get_input(prompt, default=None):
    if default:
        prompt = f"{prompt} (default: {default}): "
    user_input = input(prompt)
    return user_input if user_input else default
def generate_post_md():
    print("Générateur de fiche de post")
    
    # Demander les détails de base
    title = get_input("Titre du post", "Titre par défaut")
    category = get_input("Catégorie", "misc")

    # Crée le titre du fichier en fonction de la date et du titre du post
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{title.replace(' ', '-').lower()}.md"

    # Chemin vers le dossier _posts depuis le dossier scripts
    posts_dir = os.path.join(os.path.dirname(__file__), '..', '_posts')

    # Crée le dossier _posts s'il n'existe pas
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    # Crée le contenu du fichier Markdown
    content = f"""---
layout: post
category: {category}
title: "{title}"
author: POPKAMOKA
date: {datetime.now().strftime('%Y-%m-%d')}
tags: []
---

"""
    # Chemin complet du fichier à créer dans _posts
    file_path = os.path.join(posts_dir, filename)

    # Crée le fichier dans le dossier _posts
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fiche de post générée : {file_path}")

if __name__ == "__main__":
    generate_post_md()
