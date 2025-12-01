# class Animal:
#     def __init__(self, nome: str):
#         self.nome = nome
        
#     def aprensentar_nome(self):
#         print(f"Eu me chamo {self.nome}")

# class Tatu(Animal):
#     def __init__(self, nome: str):
#         super().__init__(nome)

#     def fazer_som(self):
#         print("Faço *sons de tatu*")

#     def mover(self):
#         print("Me encolho em formato de bola")

#     def apresentar(self, animal: Animal):
#         print(f"{self.aprensentar_nome}\n{self.fazer_som()}\n{self.mover()}\nTipo de animal: {animal}")

#     def __str__(self):
#         return f"{self.nome}"

# animal = Tatu("Rammus")
# animal.aprensentar_nome()
# animal.fazer_som()
