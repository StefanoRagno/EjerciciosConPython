import random

game = ["roca", "papel", "tijera"]

index = random.randrange(3)

play = False

while True:
  usuario = input("Ingrese una opcion (Piedra / Papel / Tijera) ó Salir: ").lower()
  if usuario not in ["piedra", "papel", "tijera", "salir"]:
    print("Algo salió mal, porfavor ingrese una opción valida")
    continue
  elif usuario == "salir":
    print("Bye!!!")
    break
  else:
    play = True
    break

print("--------------")
if play:
  print(usuario, "VS", game[index])

while play:
  # Usuario ingresa Rock
  if usuario == game[0]:
    if usuario == game[index]:
      print("empate")
      break
    elif usuario != game[index]:
      if game[index] == game[1]:
        print(f"Gana PC porque el {game[1]} envuelve a la {usuario}")
        break
      elif game[index] == game[2]:
        print(f"Gana Usuario porque la {usuario} aplasta a las {game[2]}")
        break
  # Usuario ingresa Paper
  elif usuario == game[1]:
    if usuario == game[index]:
      print("empate")
      break
    elif usuario != game[index]:
      if game[index] == game[0]:
        print(f"Gana Usuario porque la {usuario} envuelve a la {game[0]}")
        break
      elif game[index] == game[2]:
        print(f"Gana PC porque la {game[2]} corta al {usuario}")
        break
  # Usuario ingresa Tijera
  else:
    if usuario == game[index]:
      print("empate")
      break
    elif usuario != game[index]:
      if game[index] == game[0]:
        print(f"Gana PC porque la {game[0]} aplasta a {usuario}")
        break
      elif game[index] == game[2]:
        print(f"Gana Usuario porque la {usuario} corta al {game[1]}")
        break

print("--------------")

# >>> ChatGPT solution <<<

# Definimos las opciones del juego
juego = ["roca", "papel", "tijera"]

# Seleccionamos una opción aleaoria para la computadora
computer_choice = random.choice(game)

# Pedimos al usuario que ingrese su elección
user_choice = input("Ingrese roca, papel o tijera: ").lower()

print(f"Computadora eligío: {computer_choice}")

# Definimos las reglas del juego en un diccionario
rules = {
  'roca': {'gana_a': 'tijera', 'pierde_contra': 'papel'},
  'papel': {'gana_a': 'roca', 'pierde_contra': 'tijera'},
  'tijera': {'gana_a': 'papel', 'pierde_contra': 'roca'}
}

# Comprobamos el resultado del juego
if user_choice == computer_choice:
  print("Empate")
elif rules[user_choice]['gana_a'] == computer_choice:
  print(f"Gana Usuario porque {user_choice} gana a {computer_choice}")
elif rules[user_choice]['pierde_contra'] == computer_choice:
  print(f"Gana PC porque {computer_choice} gana a {user_choice}")
else:
  print("Opción no válida. Por favor ingrese roca, papel o tijera.")
