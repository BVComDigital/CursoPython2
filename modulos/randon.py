import random

list1 = [7, 6, 4, 3, 2, 11]
print(random.choice(list1))

r1 = random.randint(1, 10)
print(r1)

name = "Curso de Python"
r2 = random.choice(name)
print(r2)

print(random.sample(list1, 2))
print(random.sample(list1, 3))

done = False

while not done:
   print("Oque você deseja fazer?")
   print("1. Advinhar número.")
   print("2. Sair.")

   choice = input(">")
   if choice == "1":
      print("====================Adivinhe o número ====================\n")
      number = int(input("Digite um número entre 1 e 10: \n"))
      result = random.randint(1, 10)
      if number == result:
         print("Parabéns, você acertou o número!")
      else:    
         print(f"Que pena, o número era {result}. Tente novamente!")
   elif choice == "2":
      done = True
   else:
      print("Opção inválida. Tente novamente.")
