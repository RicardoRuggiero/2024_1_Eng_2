class GeoForm():
    def __init__(self, nome):
        self.nome = nome
    
    def calc_a(self):
        pass
    def calc_p(self):
        pass

    def __str__(self):
        return f"Forma: {self.nome}"

class Quadrado(GeoForm):
    def __init__(self, lado):
        super().__init__("Quadrado")
        self.lado = lado

    def calc_a(self):
        return self.lado ** 2

    def calc_p(self):
        return 4* self.lado

class Circulo(GeoForm):
    def __init__(self, raio):
        super().__init__("Circulo")
        self.raio = raio
    
    def calc_a(self):
        return 3.14 * self.raio ** 2

    def calc_p(self):
        return 2 * 3.14 * self.raio


quadrado = Quadrado(10)
print(quadrado.calc_a())
