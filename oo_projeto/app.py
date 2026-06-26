from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca('Biblioteca da Cidade')
biblioteca_shopping = Biblioteca('Biblioteca do Shopping')

livro1 = Livro('1984', 'George Orwel', 30.0, '084-3245')
revista1 = Revista('National Geographic', 'John Doe', 15, "Quinta")
livro2 = Livro('Brave New World', "Aldos Huxley", 25.0, '084-321564')

livro1.aplicar_desconto()

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_cidade.adicionar_item(livro2)

# biblioteca_cidade.alterna_estado()
# biblioteca_shopping.alterna_estado()

# biblioteca_cidade.receber_avaliacao('Fulano', 8.5)
# biblioteca_cidade.receber_avaliacao('Cicrano', 7.5)

def main():
   # Biblioteca.listar_bibliotecas() 
   print(vars(livro1))
   biblioteca_cidade.exibir_itens()

if __name__ == "__main__":
   main()
