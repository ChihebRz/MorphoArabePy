# Implémentation manuelle d'une table de hachage pour schèmes (énoncé p.3 : table de hachage manuelle)
# Clé : nom schème, Valeur : dict {'pattern': str, 'transform': fonction}

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]  # Buckets pour chaining

    def _hash(self, key):
        # Hash simple : somme ord() % size
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update si existe
                return
        self.table[index].append([key, value])  # Ajout nouveau

    def find(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Retourne value (dict pattern/transform)
        return None

    def remove(self, key):
        index = self._hash(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]