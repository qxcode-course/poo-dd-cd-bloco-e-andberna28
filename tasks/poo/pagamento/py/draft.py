from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor: float = valor
        self.descricao: str = descricao
    
    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")
    
    @abstractmethod
    def processar(self):
        pass


class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: int, nome_titular: str, limite: float):
        super().__init__(valor, descricao)
        self.numero: int = numero
        self.nome_titular: str = nome_titular
        self.limite: float = limite

    def resumo(self):
        return "Cartão de Crédito -> " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print(f"Erro: limite insuficiente no cartão {self.numero}")
            return
        
        self.limite -= self.valor
        print(f"Pagamento aprovado no cartão {self.nome_titular}. Limite restante: {self.limite}")

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.__chave: str = chave
        self.__banco: str = banco

    def processar(self):
        print(f"PIX enviado via banco {self.__banco} usando chave {self.__chave}")


class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: int, vencimento: str):
        super().__init__(valor, descricao)
        self.__codigo_barras: int = codigo_barras
        self.__vencimento: str = vencimento

    def processar(self):
        print(f"Boleto gerado (código {self.__codigo_barras}). Vencimento: {self.__vencimento}")
        print("Aguardando pagamento...")

def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        try:
            pag.validar_valor()
            print(pag.resumo())
            pag.processar()

            if isinstance(pag, CartaoCredito):
                print(f"Limite final do cartão: {pag.get_limite()}")

            print("-" * 40)

        except Exception as e:
            print(f"Erro ao processar pagamento: {e}")
            print("-" * 40)

pagamentos: list[Pagamento] = [
    Pix(79.99, "Camisa de Labirintos", "resenhadornoturno@gmail.com", "Banco Grêmio"),
    CartaoCredito(400, "Air Jordan", numero=123, nome_titular="Jonas Aguiar", limite=500),
    Boleto(89.90, "Ração para Rottweiler", 123456789000, "2025-01-10"),
    CartaoCredito(800, "Kit de limpeza do Machado", numero=999, nome_titular="Resenhador Noturno", limite=900)
]

processar_pagamentos(pagamentos)
