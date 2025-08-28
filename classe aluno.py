class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self, valor):
        self.notas.append(valor)
    
    def media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        return 0.0
    
    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
        
aluno1 = Aluno("Brunno")

aluno1.adicionar_nota(8.0)
aluno1.adicionar_nota(6.0)
aluno1.adicionar_nota(10.0)

print(f"Media de {aluno1.nome}: {aluno1.media():.2f}")
print(f"Situação: {aluno1.situacao()}")