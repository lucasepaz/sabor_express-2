from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Lucas', 5)
restaurante_praca.receber_avaliacao('Lais', 7)
restaurante_praca.receber_avaliacao('Leo', 1)

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('Gui', 3)
restaurante_mexicano.receber_avaliacao('Iago', 6)
restaurante_mexicano.receber_avaliacao('Nanda', 4)

restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avaliacao('Ricardo', 5)
restaurante_japones.receber_avaliacao('Duda', 8)
restaurante_japones.receber_avaliacao('Dani', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()