class Data:
    def __init__(self,dia:str,mes:str,ano:str) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formata_data(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}")

print()
