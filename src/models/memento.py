class Memento:
    def __init__(self, estado_salvo):
        self.estado_salvo = estado_salvo

    def get_estado_salvo(self):
        return self.estado_salvo