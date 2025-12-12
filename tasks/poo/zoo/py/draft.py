import abc

class Animal(abc.ABC):
    def __init__(self, nome: str):
        self.nome = nome
        
    def apresentar_nome(self):
        print(f"Eu sou {self.nome}")
    
    @abc.abstractmethod
    def fazer_som(self):
        pass

    @abc.abstractmethod
    def mover(self):
        pass
    
    def __str__(self):
        return self.nome
class Tatu(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Faço *sons de tatu*")

    def mover(self):
        print("Eu me enrolo como uma bola e rolo pelo chão")

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("ROOOOARRR")

    def mover(self):
        print("Eu caminho pela savana")


class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Sssssssssss")

    def mover(self):
        print("Eu deslizo pelo chão")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"Tipo da classe: {type(animal).__name__}")
    print("-" * 40)

animais = [
    Tatu("Rammus"),
    Leao("Simba"),
    Cobra("Nagini")
]

for a in animais:
    apresentar(a)
