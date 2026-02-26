# Sistema de Gestão Agrícola
# Módulo: Cadastro de Agricultor

class Agricultor:
    def __init__(self, nome, propriedade, area_plantada):
        self.nome = nome
        self.propriedade = propriedade
        self.area_plantada = area_plantada
    
    def exibir_dados(self):
        return f"Agricultor: {self.nome} | Propriedade: {self.propriedade} | Área: {self.area_plantada}ha"

# Exemplo de uso
if __name__ == "__main__":
    agricultor = Agricultor("João Silva", "Fazenda Esperança", 120)
    print(agricultor.exibir_dados())
