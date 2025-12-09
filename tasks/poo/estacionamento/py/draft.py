from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = horaEntrada

    def setEntrada(self, value: str):
        self.horaEntrada = value
    def getEntrada(self):
        return self.horaEntrada
    
    def getTipo(self):
        return self.tipo
    def getId(self):
        return self.id
    
    @abstractmethod
    def calcularValor(self, horaSaida: int) -> int:
        pass

    def __str__(self):
        return f""

class Bike(Veiculo):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)
    
    def calcularValor(self, horaSaida: int):
        return 3

class Moto(Veiculo):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, horaSaida: int):
        valorPagar = int(self.horaEntrada) - horaSaida / 20
        return int(valorPagar)
    
class Carro(Veiculo):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, horaSaida: int):
        valorPagar = int(self.horaEntrada) - horaSaida / 10
        if valorPagar < 5:
            valorPagar = 5
            return int(valorPagar)
        return int(valorPagar)
    
class Estacionamento:
    def __init__(self, veiculos: Veiculo, horaAtual: int):
        self.veiculos = veiculos
        self.horaAtual = horaAtual


