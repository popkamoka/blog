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

    # Crée le titre du fichier en fonction de la date et du titre du post
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{title.replace(' ', '-').lower()}.md"

    # Répertoire _posts
    posts_dir = os.path.join(os.path.dirname(__file__), '..', '_posts/misc')
    os.makedirs(posts_dir, exist_ok=True)

    # Format updated_at
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")

    # Crée le contenu du fichier Markdown
    content = f"""---
layout: post
category: misc
title: "{title}"
author: POPKAMOKA
date: {datetime.now().strftime('%Y-%m-%d')}
tags: []

progress_status: completed
updated_at: {updated_at}
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
