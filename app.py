from restaurantes import Restaurante

from cardapio.bebida import Bebida

from cardapio.prato import Prato


restaurante_praca = Restaurante('Restaurante da Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 10.9, 'Grande')
prato_cafedamanha = Prato('Pão com manteiga', 8.99,'O melhor pão na manteiga')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_cafedamanha)
bebida_suco.aplicar_desconto()
prato_cafedamanha.aplicar_desconto()

def main():
    restaurante_praca.exibir_items_cardapio


if __name__ == '__main__':
    main()