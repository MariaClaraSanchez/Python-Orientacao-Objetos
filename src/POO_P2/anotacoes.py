# Métodos de classe
class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'

# Métodos estáticos

class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'

print()
