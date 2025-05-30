from abc import ABC, abstractmethod

class Pessoas(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def __str__(self):
        return f'Parbéns, {self.nome}, sua conta foi criada.'