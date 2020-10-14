def run():
  # Ask user for information about Beep
  print("Please enter the number of lives:")
  lives = int(input())
  print("Please enter the energy level:")
  energy = int(input())
  print("Please enter the shield level:")
  shield = int(input())
  print("Lives: " + "❤ " * lives)
  print("Energy Level: " + "✦ " * energy)
  print("Shield level: " + "✶ " * shield)