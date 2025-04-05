import os
import re
from datetime import datetime

def get_input(prompt, default=None):
    if default:
        prompt = f"{prompt} (default: {default})"
    return input(prompt + ": ") or default

def slugify(value):
    value = value.lower()
    value = re.sub(r'[^\w\s-]', '', value)  # supprime caractères spéciaux
    value = re.sub(r'[\s_]+', '-', value)   # espaces et underscores → tirets
    return value.strip('-')

def yaml_escape(value):
    if value is None:
        return ""
    return f"\"{value.replace('\"', '\\\"')}\""

def generate_game_md():
    print("🎮 Générateur de fiche de jeu vidéo\n")

    title = get_input("Titre du jeu", "Titre par défaut")
    developer = get_input("Développeur", "Développeur par défaut")
    publisher = get_input("Éditeur")
    platform = get_input("Plateforme")
    genre = get_input("Genre")
    release_date = get_input("Date de sortie (JJ/MM/AAAA)")

    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_title = slugify(title)
    filename = f"{date_str}-{safe_title}.md"

    # Répertoire _posts
    posts_dir = os.path.join(os.path.dirname(__file__), '..', '_posts')
    os.makedirs(posts_dir, exist_ok=True)

    # Dossier images
    folder_name = f"{slugify(title)}-{slugify(developer)}"
    game_images_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'games', folder_name)
    os.makedirs(game_images_dir, exist_ok=True)

    cover_path = f"/assets/images/games/{folder_name}/cover.jpg"

    # Contenu du fichier Markdown
    content = f"""---
layout: game
category: game
title: {yaml_escape(f"{title} - {developer}")}
author: POPKAMOKA
date: {date_str}
tags: []

work_title: {yaml_escape(title)}
work_developer: {yaml_escape(developer)}
work_publisher: {yaml_escape(publisher)}
work_platform: {yaml_escape(platform)}
work_release_date: {yaml_escape(release_date)}
genre: {yaml_escape(genre)}
cover: {cover_path}
rating:

ownership_status:
ownership_format:
progress_status:
start_date:
end_date:
---

## Résumé

## Notes personnelles

"""

    file_path = os.path.join(posts_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Fiche de jeu générée : {file_path}")
    print(f"📁 Dossier images créé : {game_images_dir}")
    print(f"🖼️  Chemin de la couverture : {cover_path}")

if __name__ == "__main__":
    generate_game_md()
