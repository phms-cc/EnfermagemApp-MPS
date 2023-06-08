from models.memento import Memento

class Zelador:
    def __init__(self):
        self.mementos = []

    def adicionar_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, indice):
        return self.mementos[indice]

    def remover_memento(self, indice):
        return self.mementos.pop(indice)