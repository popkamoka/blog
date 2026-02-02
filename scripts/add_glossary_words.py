import os
import re
from pathlib import Path

def parse_frontmatter(content):
    """Extrait le frontmatter YAML et le contenu"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content

def parse_glossary(frontmatter):
    """Extrait la liste de glossaire du frontmatter de façon robuste (sans regex complexe).

    Retourne une liste de dicts: [{"word": ..., "definition": ...}, ...]
    """
    lines = frontmatter.splitlines()
    glossary = []
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == 'glossary:')
    except StopIteration:
        return []

    i = start + 1
    while i < len(lines):
        line = lines[i]
        # Attendre une entrée d'item qui commence par '  - word:'
        if line.lstrip().startswith('- word:') or line.startswith('  - word:'):
            # Récupère le mot
            word = line.split(':', 1)[1].strip().strip('"')
            # Définitions attendues sur la ligne suivante indentée
            definition = ''
            if i + 1 < len(lines) and lines[i + 1].lstrip().startswith('definition:'):
                definition = lines[i + 1].split(':', 1)[1].strip().strip('"')
                i += 1
            if word or definition:
                glossary.append({"word": word, "definition": definition})
        else:
            # si on rencontre une ligne qui n'est pas indentée comme un item, on arrête
            if line and not line.startswith('  ') and not line.startswith('    '):
                break
        i += 1

    return glossary

def glossary_to_yaml(glossary):
    """Convertit la liste de glossaire en YAML"""
    if not glossary:
        return "glossary:\n  - word: \"\"\n    definition: \"\""
    
    yaml_lines = ["glossary:"]
    for item in glossary:
        # Échapper les guillemets doubles si nécessaire
        word = str(item.get("word", "")).replace('"', '\\"')
        definition = str(item.get("definition", "")).replace('"', '\\"')
        yaml_lines.append(f'  - word: "{word}"')
        yaml_lines.append(f'    definition: "{definition}"')
    return "\n".join(yaml_lines)

def update_glossary_in_frontmatter(frontmatter, glossary):
    """Remplace ou ajoute le glossaire dans le frontmatter"""
    lines = frontmatter.splitlines()
    yaml_block = glossary_to_yaml(glossary).splitlines()

    # Trouve la ligne de début du bloc glossary s'il existe
    start_idx = None
    for i, l in enumerate(lines):
        if l.strip() == 'glossary:':
            start_idx = i
            break

    if start_idx is None:
        # Ajoute le glossaire à la fin du frontmatter
        if lines and lines[-1].strip() == '':
            lines = lines[:-1]
        lines.extend(yaml_block)
    else:
        # Trouve la fin du bloc (première ligne non indentée après start)
        end_idx = start_idx + 1
        while end_idx < len(lines) and (lines[end_idx].startswith('  ') or lines[end_idx].startswith('    ') or lines[end_idx].strip().startswith('-')):
            end_idx += 1
        # Remplace la tranche start_idx:end_idx par yaml_block
        lines[start_idx:end_idx] = yaml_block

    return "\n".join(lines)

def add_glossary_words():
    print("📚 Outil d'ajout de mots au glossaire\n")
    
    # Trouve le dossier des livres
    script_dir = os.path.dirname(os.path.abspath(__file__))
    books_dir = os.path.join(script_dir, '..', '_posts', 'books')
    
    if not os.path.exists(books_dir):
        print(f"❌ Dossier non trouvé: {books_dir}")
        return
    
    # Liste les fichiers markdown
    book_files = sorted([f for f in os.listdir(books_dir) if f.endswith('.md')])
    
    if not book_files:
        print("❌ Aucun fichier de livre trouvé")
        return
    
    print(f"📖 {len(book_files)} fichier(s) trouvé(s):\n")
    for i, filename in enumerate(book_files, 1):
        # Extrait le titre du nom du fichier
        title = filename.replace('.md', '').split('-', 3)[-1].replace('-', ' ').title()
        print(f"{i}. {title}")
    
    # Demande à l'utilisateur de choisir
    while True:
        try:
            choice = int(input("\nChoisir le numéro du fichier (ou 0 pour taper le chemin): "))
            if choice == 0:
                file_path = input("Chemin du fichier: ").strip()
                break
            elif 1 <= choice <= len(book_files):
                file_path = os.path.join(books_dir, book_files[choice - 1])
                print(f"\n✅ Fichier sélectionné: {book_files[choice - 1]}")
                break
            else:
                print("❌ Numéro invalide")
        except ValueError:
            print("❌ Veuillez entrer un numéro valide")
    
    if not os.path.exists(file_path):
        print(f"❌ Fichier non trouvé: {file_path}")
        return
    
    # Lit le fichier
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse le frontmatter
    frontmatter, body = parse_frontmatter(content)
    if frontmatter is None:
        print("❌ Impossible de parser le frontmatter du fichier")
        return
    
    # Récupère le glossaire existant
    glossary = parse_glossary(frontmatter)
    
    print(f"\n✅ Fichier chargé. Glossaire actuel: {len(glossary)} mot(s)\n")
    
    # Boucle interactive
    while True:
        print("\nOptions:")
        print("1. Ajouter un mot")
        print("2. Voir le glossaire actuel")
        print("3. Supprimer un mot")
        print("4. Sauvegarder et quitter")
        print("5. Quitter sans sauvegarder")
        
        choice = input("\nChoix: ").strip()
        
        if choice == '1':
            # Permet d'ajouter plusieurs entrées à la suite et sauvegarde après chaque ajout
            while True:
                word = input("Mot: ").strip()
                definition = input("Définition: ").strip()

                if word and definition:
                    # Vérifie si le mot existe déjà
                    existing = [g for g in glossary if g["word"].lower() == word.lower()]
                    if existing:
                        update = input(f"Le mot '{word}' existe déjà. Voulez-vous le remplacer? (o/n): ").strip().lower()
                        if update == 'o':
                            glossary = [g for g in glossary if g["word"].lower() != word.lower()]
                            glossary.append({"word": word, "definition": definition})
                            print(f"✅ Mot '{word}' mis à jour")
                        else:
                            print("ℹ️ Mot non modifié")
                    else:
                        glossary.append({"word": word, "definition": definition})
                        print(f"✅ Mot '{word}' ajouté")

                    # Sauvegarde automatique après chaque ajout/mise à jour
                    frontmatter = update_glossary_in_frontmatter(frontmatter, glossary)
                    new_content = f"---\n{frontmatter}\n---\n{body}"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"💾 Sauvegardé ({len(glossary)} mot(s))")
                else:
                    print("❌ Veuillez remplir les deux champs")

                cont = input("Ajouter un autre mot ? (o/n): ").strip().lower()
                if cont != 'o':
                    break
        
        elif choice == '2':
            if glossary:
                print("\n📖 Glossaire actuel:")
                for i, item in enumerate(glossary, 1):
                    print(f"{i}. {item['word']}: {item['definition']}")
            else:
                print("📖 Glossaire vide")
        
        elif choice == '3':
            if glossary:
                print("\n📖 Mots disponibles:")
                for i, item in enumerate(glossary, 1):
                    print(f"{i}. {item['word']}")
                
                try:
                    idx = int(input("Numéro du mot à supprimer: ")) - 1
                    if 0 <= idx < len(glossary):
                        removed = glossary.pop(idx)
                        print(f"✅ Mot '{removed['word']}' supprimé")
                    else:
                        print("❌ Numéro invalide")
                except ValueError:
                    print("❌ Veuillez entrer un numéro valide")
            else:
                print("📖 Glossaire vide")
        
        elif choice == '4':
            # Met à jour le frontmatter avec le nouveau glossaire
            frontmatter = update_glossary_in_frontmatter(frontmatter, glossary)
            
            # Réécrit le fichier
            new_content = f"---\n{frontmatter}\n---\n{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Fichier sauvegardé avec {len(glossary)} mot(s)")
            break
        
        elif choice == '5':
            print("❌ Modification annulée")
            break
        
        else:
            print("❌ Choix invalide")

if __name__ == "__main__":
    add_glossary_words()
