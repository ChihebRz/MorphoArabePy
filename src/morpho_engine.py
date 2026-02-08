# Cœur du projet : Génération et validation morphologique (énoncé p.4)

def generate_word(root, scheme):
    # Applique la transformation (fonction stockée dans scheme['transform'])
    return scheme['transform'](root)

def extract_root_from_word(word, scheme):
    """
    Extrait la racine supposée à partir du mot et du pattern du schème.
    Ignore les lettres fixes du schème et prend uniquement les positions des placeholders.
    """
    pattern = scheme['pattern'].replace(' ', '')  # Supprime les espaces pour simplifier
    placeholders = ['ف', 'ع', 'ل']               # Ordre classique f-ʿ-l
    root_letters = []
    word_idx = 0

    for c in pattern:
        if c in placeholders:
            # C'est une position de la racine → on prend la lettre du mot
            if word_idx < len(word):
                root_letters.append(word[word_idx])
            word_idx += 1
        else:
            # Lettre fixe du schème → on vérifie qu'elle correspond (optionnel mais utile)
            if word_idx < len(word) and word[word_idx] != c:
                return ""  # Ne correspond pas → échec immédiat
            word_idx += 1

    # On doit avoir exactement 3 lettres pour une racine trilitère standard
    if len(root_letters) != 3:
        return ""
    
    return ''.join(root_letters)
    return extracted

def validate_word(word, root, tree, hash_table, matched_callback):
    """
    matched_callback est une fonction qui reçoit le nom du schème quand trouvé
    """
    for bucket in hash_table.table:
        for pair in bucket:
            key, scheme = pair[0], pair[1]
            extracted = extract_root_from_word(word, scheme)
            if extracted == root:
                if matched_callback:
                    matched_callback(key)
                tree.add_derivative(root, word)
                return True
    return False