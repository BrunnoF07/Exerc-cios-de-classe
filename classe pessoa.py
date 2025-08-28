class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola meu nome é {self.nome} e tenho {self.idade} anos.")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversario hoje, agora tem {self.idade} anos.")

p1 = Pessoa("Ana", 25)
p2 = Pessoa("Brunno", 20)

p1.apresentar()
p2.apresentar()

p1.fazer_aniversario()
p2.fazer_aniversario()

p1.apresentar()
p2.apresentar()