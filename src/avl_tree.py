# Implémentation de l'arbre AVL pour gérer les racines arabes (énoncé p.3 : ABR/AVL, préférence AVL pour équilibre)
# Chaque nœud : racine, liste de dérivés (dict mot:fréquence pour simplicité)

class Node:
    def __init__(self, root):
        self.root = root  # Racine arabe ex. "كتب"
        self.derivatives = {}  # Dict {mot: fréquence}
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        return node.height if node else 0  # Hauteur ou 0 si None

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0  # Balance

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x  # Nouvelle racine

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        return y

    def _insert(self, node, key):
        if not node:
            return Node(key)  # Nouveau nœud

        if key < node.root:
            node.left = self._insert(node.left, key)
        elif key > node.root:
            node.right = self._insert(node.right, key)
        else:
            return node  # Déjà existant

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Rotations pour équilibre
        if balance > 1 and key < node.left.root:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.root:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.root:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.root:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)  # Insertion publique O(log n)

    def _search(self, node, key):
        if not node or node.root == key:
            return node
        if key < node.root:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        return self._search(self.root, key)  # Recherche O(log n)

    def add_derivative(self, root_key, word):
        node = self.search(root_key)
        if node:
            if word in node.derivatives:
                node.derivatives[word] += 1  # Incrémente freq
            else:
                node.derivatives[word] = 1  # Ajoute nouveau

    def _in_order(self, node, func):
        if node:
            self._in_order(node.left, func)
            func(node)  # Appel fonction ex. print
            self._in_order(node.right, func)

    def display_in_order(self, func):
        self._in_order(self.root, func)  # Affichage structuré