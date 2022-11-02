class Conta:

    def __init__(self,numero:int,titular:str,saldo:float,limite:float) :
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} reais do titular {self.__titular}")
    
    def deposita(self, valor:float):
        self.__saldo += valor
    
    def __pode_sacar(self,valor_sacar):
        saldo_disponivel = self.__saldo + self.__limite
        return valor_sacar <= saldo_disponivel

    def saque(self, valor:float):
        if self.__pode_sacar(valor_sacar=valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite, que é de {self.limite}")
    
    def transfe(self, valor: float, destino:str):
        self.__saque(valor)
        destino.deposita(valor)

    ######### Métodos Get e Set #########

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite) :
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
    
        
print()