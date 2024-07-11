"""
Created on Wed Mar 27 23:53:26 2024

@author: JussJaeyy
"""

import random
import sqlite3



def marley():
      print("🌟 *❯─「WELCOME TO MARLEY333」─❮* 🌟")
      print("👋 *Hi JussJaεyy*! 🍃")
      print("🔰 *Prefix*: !")
      print("⚙️ *Visit our Website:No official website yet...")
      print("___________________________________________________")
      print("This help menu is designed to help you get started with the bot.")
      print("⟾ *🎁ＣＯＭＭＡＮＤ ＬＩＳＴ🎁*")
      print("*❯── 「Fun」──❮* ➪")
      print("```joke, truth_dare, tictactoe, Word game, A week in paradise ```")
      print("*❯── 「General」──❮* ➪")
      print("```help, hi, info, mods, ping, profile, rank, support```")
      print("*❯── 「Media」──❮* ➪")
      print("```play, spotify```")
      print("*❯── 「Moderation」──❮* ➪")
      print("```disable, enable, close, open, promote, tagall```")


      while True:                   
          user_input = input("User: ").lower()
          if user_input == "!hello":
              print("Marley: Hello! How can I assist you today?")
          
          elif user_input == "!help":
              print("🌟 *❯─「Marley」─❮* 🌟")
              print("👋 *Hi JussJaεyy* Senpai! 🍃")
              print("🔰 *Prefix*: !")
              print("⚙️ *Visit our Website:No official website yet...")
              print("___________________________________________________")
              print("This help menu is designed to help you get started with the bot.")
              print("⟾ *🎁ＣＯＭＭＡＮＤ ＬＩＳＴ🎁*")
              print("*❯── 「Games」──❮* ➪")
              print("```joke, riddles```")
              print("*❯── 「Fun」──❮* ➪")
              print("```word chain, truth_dare, tictactoe, Word game, A week in paradise, hangman, 20 Questions, rock paper scissors, trivia, ```")
              print("*❯── 「Fun Facts」──❮* ➪")
              print("```quotes```")
              print("*❯── 「General」──❮* ➪")
              print("```help, hi, info, mods, ping, profile, rank, support```")
              print("*❯── 「Media」──❮* ➪")
              print("```play, spotify```")
              print("*❯── 「Moderation」──❮* ➪")
              print("```disable, enable, close, open, promote, tagall```")
              print("*❯── 「Information」──❮* ➪")
              print("```dictionary, weather, news, wikipedia summary```")
              print("*❯── 「Social」──❮* ➪")
              print("```chat, debate, two truths and a lie```")
              print("*❯── 「Personalized」──❮* ➪")
              print("```birthday calculator, horoscope, career quiz, personality quiz```")
              print("*❯── 「Tools」──❮* ➪")
              print("```calculator, converter, password generator, random number generator```")
          
          elif user_input == "!":
              print("Marley: No such command, Retry!")

          elif user_input == "!quit":
              print("Marley: Goodbye! It was nice chatting with you.")
              break
          elif user_input == "!wikipedia summary":
               wikipedia_summary()
          elif user_input == "!slot":
              start_game()
          elif user_input == "!hangman":
              hangman()
          elif user_input == "!wordgame":
              wordgame()
          elif user_input == "!password generator":
              password_generator()
          elif user_input == "!chat":
              chat()
          elif user_input == "!news":
              news()
          elif user_input == "!wikipedia summary":
               wikipedia_summary()
          elif user_input == "!truth or dare":
               truth_or_dare()
          elif user_input == "!tictactoe":
              tictactoe()
          elif user_input == "!wordgame":
              wordgame()
          elif user_input == "!promote":
              promote()
          elif user_input == "!song":
              song()
          elif user_input == "!makeadmin":
              makeadmin()
          elif user_input == "!makemod":
              makemod()
          elif user_input == "!calculator":
              calculator()
          elif user_input == "!converter":
              converter()
          elif user_input == "!hangman":
              hangman()
          elif user_input == "!birthday calculator":
              birthday_calculator()
          elif user_input == "!random number generator":
              random_number_generator()
          elif user_input == "!joke":
              joke()    
          elif user_input == "!quote":
              quotes()
          elif user_input == "!wordchain":
              joke()    
          elif user_input == "!dictionary":
              dictionary()
          elif user_input == "!wordscramble":
              word_scramble()
          elif user_input == "t2truthslie":
              two_truths_and_a_lie()
          elif user_input == "rockpaperscissors":
              rock_paper_scissors()
          
              
              
           
            
      else:
          print("Marley: No such command, Retry!")
          
def get_profile(user_id):
  profiles = {
    "1": {"name": "John", "age": 25},
    "2": {"name": "Jane", "age": 30}
  }
  return profiles.get(user_id, {})

def get_married_characters():
  married_characters = {
    "1": ["1", "2"],
    "2": ["3", "4"]
  }
  return married_characters

def get_gallery(user_id):
  gallery = {
    "1": ["1", "2", "3"],
    "2": ["4", "5", "6"]
  }
  return gallery.get(user_id, [])

def get_rank(user_id):
  ranks = {
    "1": "Beginner",
    "2": "Intermediate",
    "3": "Advanced"
  }
  return ranks.get(user_id, "Unknown")
def rules():
              print("No Rukes") 
                            


def guess_the_number():
  number = random.randint(1, 100)
  attempts = 0
  while True:
    user_input = input("Guess the number (type 'quit' to quit, 'help' for help): ")
    if user_input.lower() == 'quit':
      print("Goodbye!")
      break
    elif user_input.lower() == 'help':
      print("Type a number between 1 and 100 to guess the number.")
      print("Type 'quit' to quit the game.")
      print("Type 'help' to show this help message again.")
    else:
      try:
        guess = int(user_input)
        attempts += 1
        if guess < number:
          print("Too low!")
        elif guess > number:
          print("Too high!")
        else:
          print(f"Congratulations! You guessed the number in {attempts} attempts.")
          break
      except ValueError:
        print("Invalid input. Please type a number.")
 
def truth_or_dare():
    print("Welcome to Truth or Dare!")
    print("It begins")
    players = []
    num_players = int(input("How many players? "))

    for i in range(num_players):
        player_name = input(f"Enter name of player {i+1}: ")
        players.append({"name": player_name, "score": 0, "alive": True})

    turn = 0
    while True:
        current_player = players[turn % num_players]
        if not current_player["alive"]:
            turn += 1
            continue

        print(f"\n{current_player['name']}'s turn!")
    

        choice = input("Enter 'T' for Truth or 'D' for Dare: ").upper()
        if choice == 'T':
            truth_question = random.choice(truth_questions)
            print(f"{current_player['name']}, {truth_question}")
            answer = input("Answer: ")
            if answer.lower() == "pass":
                current_player["alive"] = False
                print(f"{current_player['name']} has been eliminated!")
            else:
                current_player["score"] += 1
            
        elif choice == 'D':
            dare_task = random.choice(dare_tasks)
            print(f"{current_player['name']}, {dare_task}")
            response = input("Response (yes/no): ")
            if response.lower() == "yes":
                current_player["score"] += 2
            else:
                current_player["alive"] = False
                print(f"{current_player['name']} has been eliminated!")
                
                
        else:
            print("Invalid choice! Please try again")

        turn += 1

        if len([player for player in players if player["alive"]]) == 1:
            winner = [player for player in players if player["alive"]][0]
            print(f"\n{winner['name']} wins with a score of {winner['score']}!")
            break

truth_questions = [
    "What is your biggest fear?",
    "What is your favorite hobby?",
    "What is your favorite food?",
    "What is your favorite movie?",
    "What is your favorite book?",
]

dare_tasks = [
    "Do 10 jumping jacks.",
    "Sing a silly song out loud.",
    "Do a funny dance.",
    "Tell a joke.",
    "Draw a silly picture.",
]

                                                            
truth_or_dare()


def rock_paper_scissors():
    
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    user = input("Enter your choice ('r' for Rock, 'p' for Paper, 's' for Scissors): ")
    computer = random.choice(list(choices.keys()))

    print(f"\nYou chose {choices[user]}, computer chose {choices[computer]}.\n")

    if user == computer:
        return 'It\'s a tie!'
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return 'You win!'
    return 'You lose!'
rock_paper_scissors()

def tictactoe():
                print("Marley: Let's play Tic Tac Toe!")


board = [' ' for _ in range(9)] 
player1_name = input("Enter Player 1's name: ")
player2_name = input("Enter Player 2's name: ")
player1_icon = 'X'
player2_icon = 'O'
player1_score = 0
player2_score = 0

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Your turn player {}".format(number))

    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move(player1_icon)
    print_board()
    if is_victory(player1_icon):
        print("{} Wins! Congratulations!".format(player1_name))
        player1_score += 1
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move(player2_icon)
    if is_victory(player2_icon):
        print_board()
        print("{} Wins! Congratulations!".format(player2_name))
        player2_score += 1
        break

print("Score - {} : {} vs {} : {}".format(player1_name, player1_score, player2_name, player2_score))

def hangman():
    word = random.choice(["apple", "banana", "cherry"])
    guesses = 6
    while guesses > 0:
        guess = input("Guess a letter: ")
        if guess in word:
            print("Correct!")
        else:
            guesses -= 1
            print(f"Incorrect! You have {guesses} guesses left.")
    print(f"The word was {word}.")

def twenty_questions():
    object = random.choice(["book", "chair", "car"])
    questions = 20
    while questions > 0:
        question = input("Ask a yes or no question: ")
        if question == "Is it a living thing?":
            print("No")
        elif question == "Is it something you can sit on?":
            print("Yes" if object == "chair" else "No")
        else:
            print("I don't know.")
        questions -= 1
    print(f"The object was a {object}.")

conn = sqlite3.connect("gold_coins_db.db")
c = conn.cursor()

def start_game():
  print("Welcome to the Slot Machine Game!")
  print("Type '!slot' to play.")
  while True:
    message = input("> ")
    if message == "!slot":
      response = slot_machine()
      print(response)
      gold_coins = get_gold_coins()
      winnings = get_winnings(response)
      new_gold_coins = min(gold_coins + winnings, 50000)
      save_gold_coins(new_gold_coins)
    else:
      print("Invalid command. Try !slot")

def slot_machine():
  reels = ["🥉", "🥈", "🥇"]
  rows = []
  for _ in range(3):
    row = [random.choice(reels) for _ in range(3)]
    rows.append(row)
  response = "You got:\n"
  for row in rows:
    response += " ".join(row) + "\n"
  for row in rows:
    if row[0] == row[1] == row[2]:
      response += "Congratulations, you won!"
      return response
  response += "Better luck next time!"
  return response

def get_gold_coins():
  c.execute("SELECT gold_coins FROM users WHERE id = 1")
  result = c.fetchone()
  return result[0] if result else 0

def get_winnings(response):
  if "Congratulations, you won!" in response:
    return random.randint(100, 1000)
  else:
    return 0

def save_gold_coins(gold_coins):
  c.execute("UPDATE users SET gold_coins = ? WHERE id = 1", (gold_coins,))
  conn.commit()

start_game()

def word_scramble():
    word = random.choice(["hello", "world", "python"])
    scrambled = "".join(random.sample(word, len(word)))
    print(f"Unscramble the word: {scrambled}")
    guess = input("Enter your guess: ")
    if guess == word:
        print("Correct!")
    else:
        print(f"Incorrect. The word was {word}.")


def calculator():
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Invalid operator.")

def converter():
    unit = input("Enter the unit to convert (length, mass, time): ")
    if unit == "length":
        value = float(input("Enter the value: "))
        print(f"{value} meters is equal to {value * 3.28084} feet.")
    elif unit == "mass":
        value = float(input("Enter the value: "))
        print(f"{value} kilograms is equal to {value * 2.20462} pounds.")
    elif unit == "time":
        value = float(input("Enter the value: "))
        print(f"{value} seconds is equal to {value / 60} minutes.")
    else:
        print("Invalid unit.")

def random_number_generator():
    print(random.randint(1, 100))

def password_generator():
    length = int(input("Enter the length of the password: "))
    print("".join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", length)))

def quotes():
    choices = ["Believe you can and you're halfway there. - Theodore Roosevelt", "The only way to do great work is to love what you do. - Steve Jobs", "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill", "Don't watch the clock; do what it does. Keep going. - Sam Levenson", "You miss 100% of the shots you don't take. - Wayne Gretzky"]
    quote = random.choices(choices)
    print(quote)
    
    

def would_you_rather():
    choice = random.choice(["Would you rather be able to fly or be able to breathe underwater?", "Would you rather have a million dollars or the ability to travel anywhere in the world for free?", "Would you rather be able to speak any language fluently or be able to play any musical instrument perfectly?", "Would you rather have a 10-minute conversation with a historical figure or spend 10 minutes in a place that no longer exists?", "Would you rather have the ability to take a picture of your dreams or be able to record your thoughts?"])
    print(choice)


def mad_libs():
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    print(f"There once was a {adjective} {noun} who loved to {verb}.")

def word_chain():
    word = input("Enter a word: ")
    print(f"The word that starts with the last letter of {word} is {word[-1]}.")

# Information
def news():
    print("Here are the latest news headlines:")

def weather_forecast():
    print("Here is the current weather forecast:")

def dictionary():
    word = input("Enter a word to define: ")
    print(f"The definition of {word} is...")

def wikipedia_summary():
    topic = input("Enter a topic to summarize: ")
    print(f"Here is a summary of {topic}:")

# Social
def chat():
    friend = input("Enter the name of your friend: ")
    print(f"Hello, {friend}!")

def debate():
    topic = input("Enter a topic to debate: ")
    print("Let's debate!")

def two_truths_and_a_lie():
    statement1 = input("Enter a true statement: ")
    statement2 = input("Enter a true statement: ")
    statement3 = input("Enter a false statement: ")
    print("1. + statement1")
    print("2. + statement2")
    print("3. + statement3")
    answer = input("enter '1', '2' or '3':")
    if answer == '1':
        print("You think the first statemant is a lie!. Correct, ")
    print("Can you guess which one is the lie?")

# Personalized
def horoscope():
    sign = input("Enter your zodiac sign: ")
    print(f"Here is your horoscope, {sign}!")

def personality_quiz():
    answer1 = input("Do you prefer introverted or extroverted activities? ")
    answer2 = input("Do you prefer logical or creative thinking? ")
    answer3 = input("Do you prefer planning or spontaneity? ")
    print("Here are your personality quiz results!")

def career_quiz():
    answer1 = input("Do you prefer working with people or alone? ")
    answer2 = input("Do you prefer creative or analytical work? ")
    answer3 = input("Do you prefer a structured or flexible work environment? ")
    print("Here are your career quiz results!")

def birthday_calculator():
    month = input("Enter your birth month: ")
    day = input("Enter your birth day: ")
    year = input("Enter your birth year: ")
    print(f"Your birthday is {month} {day}, {year}!")



def promote():
    
                    print("Marley: Which WhatsApp user would you like to make an admin?")
                    user_number = input("User: ")
                    print(f"Marley: Making {user_number} an admin...")
         
def wordgame():
                print("Marley: Let's play a word game!")


def song():
                print("Marley: Which song would you like to get?")
                song_name = input("User: ")
                print(f"Marley: Getting {song_name}...")
# Song downloading logic goes here

def makeadmin():
                print("Marley: Which WhatsApp user would you like to make an admin?")
                user_number = input("User: ")
                print(f"Marley: Making {user_number} an admin...")
# WhatsApp admin logic goes here

def makemod():
                print("Marley: Which WhatsApp user would you like to make a mod?")
                user_number = input("User: ")
                print(f"Marley: Making {user_number} a mod...")
# WhatsApp mod logic goes here
def joke():
    print("")
marley()
