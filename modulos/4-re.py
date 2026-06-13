import re

text = "Udemy - uma plataforma com muitos cursos online"

# 1 - Índice inicial e final das palavras
# O r significa uma string raw, ou seja, sem caracteres de escape
match = re.search(r'uma plataforma', text)
if match:
    print(f"Índice inicial: {match.start()}")
    print(f"Índice final: {match.end()}")
else:
    print("Padrão não encontrado: uma plataforma")
# 2 - Substituir palavras
new_text = re.sub(r'Udemy', 'Coursera', text)   
print(new_text)
# 3 - Encontrar todas as palavras que começam com 'c' e terminam com 'o'
matches = re.findall(r'\bc\w*o\b', text)  
print(matches)
# 4 - Verificar se a string começa com 'Udemy'
if re.match(r'^Udemy', text):
    print("A string começa com 'Udemy'")
# 5 - Buscando o índice que possui o ponto 
site = 'https://udemy.com'
match = re.search(r'\.', site)
if match:
    print(f"Índice do ponto: {match.start()}")
else:
    print("Ponto não encontrado no site")
# 6 - Verificando  o início de uma string
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'A vida é bela', 'Vamos passar']
for f in phrases:
    if re.match(rule, f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não Corresponde: {f}')
