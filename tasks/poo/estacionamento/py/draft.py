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
        tipo = self.tipo.rjust(10, "_")
        id_ = self.id.rjust(10, "_")
        return f"{tipo} : {id_} : {self.horaEntrada}"

class Bike(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Bike", horaEntrada)

    def calcularValor(self, horaSaida: int):
        return 3

class Moto(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Moto", horaEntrada)

    def calcularValor(self, horaSaida: int):
        tempo = horaSaida - self.horaEntrada
        return tempo / 20
    
class Carro(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Carro", horaEntrada)

    def calcularValor(self, horaSaida: int):
        tempo = horaSaida - self.horaEntrada
        valor = tempo / 10
        return max(valor, 5.0)
    
class Estacionamento:
    def __init__(self):
        self.veiculos: list[Veiculo] = []
        self.horaAtual: int = 0

    def passarTempo(self, minutos: int):
        self.horaAtual += minutos

    def estacionar(self, tipo: str, id: str):
        if tipo == "bike":
            self.veiculos.append(Bike(id, self.horaAtual))
        elif tipo == "moto":
            self.veiculos.append(Moto(id, self.horaAtual))
        elif tipo == "carro":
            self.veiculos.append(Carro(id, self.horaAtual))

    def pagar(self, id: str):
        try:
            for v in self.veiculos:
                if v.getId() == id:
                    valor = v.calcularValor(self.horaAtual)
                    self.veiculos.remove(v)
                    print(
                        f"{v.getTipo()} chegou {v.getEntrada()} saiu {self.horaAtual}. "
                        f"Pagar R$ {valor:.2f}"
                    )
                    return
            raise ValueError("Veículo não encontrado")

        except Exception as e:
            print(f"Erro ao pagar: {e}")

    def show(self):
        for v in self.veiculos:
            print(v)
        print(f"Hora atual: {self.horaAtual}")

def main():
    estacionamento = Estacionamento()
    while True:
        try:
            line: str = input()
            print("$" + line)
            args: list[str] = line.split(" ")
            if args[0] == "end":
                break
            elif args[0] == "show":
                estacionamento.show()
            elif args[0] == "estacionar":
                estacionamento.estacionar(args[1], args[2])
            elif args[0] == "tempo":
                estacionamento.passarTempo(int(args[1]))
            elif args[0] == "pagar":
                estacionamento.pagar(args[1])
            else:
                print("Comando inválido")
        except IndexError:
            print("Erro: parâmetros insuficientes")
        except ValueError:
            print("Erro: valor inválido")
        except Exception as e:
            print(f"Erro inesperado: {e}")

main()