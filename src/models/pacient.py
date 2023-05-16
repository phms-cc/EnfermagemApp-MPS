from abc import ABC, abstractmethod


class Paciente(ABC):
    def __init__(self, nome, idade, peso, altura, endereço):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.endereço = endereço