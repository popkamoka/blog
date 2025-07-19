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
    posts_dir = os.path.join(os.path.dirname(__file__), '..', '_posts/books')

    # Crée le dossier _posts s'il n'existe pas
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    # Crée le nom du dossier d'images sans la date
    folder_name = f"{title.replace(' ', '-').lower()}-{author.replace(' ', '-').lower()}"
    
    # Crée le chemin pour le dossier d'images du livre dans assets/images/books/
    book_images_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'books', folder_name)
    
    # Crée le dossier d'images si il n'existe pas
    if not os.path.exists(book_images_dir):
        os.makedirs(book_images_dir)

    # Le chemin de la couverture du livre
    cover_path = f"/assets/images/books/{folder_name}/cover.jpg"
    extract_path = f"/assets/images/books/{folder_name}/extrait.png"

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
work_publication_date: 
genre:
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
{{% include lightbox_image.html
src="{extract_path}"
alt=""
caption="" %}}

"""

    # Chemin complet du fichier à créer dans _posts
    file_path = os.path.join(posts_dir, filename)

    # Crée le fichier dans le dossier _posts
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fiche de livre générée : {file_path}")
    print(f"Dossier pour les images créé : {book_images_dir}")
    print(f"Chemin de la couverture : {cover_path}")

if __name__ == "__main__":
    generate_book_md()
