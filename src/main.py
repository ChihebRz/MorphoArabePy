# Interface CLI interactive (énoncé p.4 : application en ligne de commande)

from avl_tree import AVLTree
from hash_table import HashTable
from morpho_engine import generate_word, validate_word
from utils import load_roots_from_file, load_schemes_from_file

def main():
    tree = AVLTree()
    hash_table = HashTable()

    # Chargement initial
    load_roots_from_file(tree, 'data/racines.txt')
    load_schemes_from_file(hash_table, 'data/schemas.txt')

    while True:
        print("\nMenu:")
        print("1. Ajouter une racine")
        print("2. Ajouter/modifier un schème")
        print("3. Générer un mot dérivé")
        print("4. Valider un mot")
        print("5. Afficher dérivés d'une racine")
        print("6. Quitter")
        choice = input("Choix: ")

        if choice == '6':
            break
        elif choice == '1':
            root = input("Entrez racine (ex. كتب): ")
            tree.insert(root)
            print("Racine ajoutée.")
        elif choice == '2':
            name = input("Nom schème (ex. مفعول): ")
            pattern = input("Pattern (ex. م ف ع ول): ")
            # Crée transform simple (améliore si besoin)
            placeholders = ['ف', 'ع', 'ل']
            transform = lambda r: ''.join(r[placeholders.index(c)] if c in placeholders else c for c in pattern if c != ' ')
            scheme = {'pattern': pattern, 'transform': transform}
            hash_table.insert(name, scheme)
            print("Schème ajouté/modifié.")
        elif choice == '3':
            root = input("Racine: ")
            name = input("Schème: ")
            scheme = hash_table.find(name)
            if scheme:
                word = generate_word(root, scheme)
                print(f"Mot généré: {word}")
            else:
                print("Schème non trouvé.")
        elif choice == '4':
            word = input("Mot à valider: ")
            root = input("Racine supposée: ")
            
            # On passe une liste ou une variable mutable pour récupérer le schème
            matched = [""]
            
            def set_matched(s):
                matched[0] = s
            
            valid = validate_word(word, root, tree, hash_table, set_matched)
            
            if valid:
                print(f"OUI (Schème: {matched[0]})")
                # Optionnel : afficher directement les dérivés mis à jour
                node = tree.search(root)
                if node and matched[0] in node.derivatives:
                    print(f"   → Fréquence actuelle de '{word}': {node.derivatives[word]}")
            else:
                print("NON")
        elif choice == '5':
            root = input("Racine: ")
            node = tree.search(root)
            if node:
                print("Dérivés:")
                for w, freq in node.derivatives.items():
                    print(f"{w} (fréq: {freq})")
            else:
                print("Racine non trouvée.")

if __name__ == "__main__":
    main()