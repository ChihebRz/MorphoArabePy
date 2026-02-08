# Utilitaires : Chargement fichiers (énoncé p.2)
import arabic_reshaper
from bidi.algorithm import get_display

def display_arabic(text):
    """Reformate le texte arabe pour affichage RTL correct dans terminal."""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)
def load_roots_from_file(tree, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            root = line.strip()
            if root:
                tree.insert(root)  # Charge racines

def load_schemes_from_file(hash_table, filename):
    placeholders = {'ف': 0, 'ع': 1, 'ل': 2}  # dictionnaire indice → position racine

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(';')
            if len(parts) == 2:
                name, pattern = parts
                
                def transform(r, pat=pattern, ph=placeholders):
                    result = []
                    for c in pat:
                        if c == ' ':
                            continue
                        if c in ph:
                            idx = ph[c]
                            if idx < len(r):
                                result.append(r[idx])
                            else:
                                result.append('?')  # marqueur d'erreur
                        else:
                            result.append(c)
                    return ''.join(result)
                
                scheme = {'pattern': pattern, 'transform': transform}
                hash_table.insert(name, scheme)