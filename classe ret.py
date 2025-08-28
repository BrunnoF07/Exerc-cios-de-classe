class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura * self.altura)
    
ret = Retangulo(7, 2)

print(f"Area: {ret.area()}")
print(f"Perimetro: {ret.perimetro()}")