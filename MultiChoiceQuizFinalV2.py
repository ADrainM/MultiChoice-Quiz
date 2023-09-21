def cquestions():
  global correct
  correct = 0
  q = 0
  cq = {"You have chosen the country theme. \n\nWhich country has the largest area in meters squared? \n\ta) USA \n\tb) New Zealand  \n\tc) Canada  \n\td) Russia  \nAnswer: ": "d", "Which country has the largest population? \n\ta) Brazil \n\tb) India \n\tc) China  \n\td) Nigeria  \nAnswer: " : "c", "Which country has the largest GDP? (2020) \n\ta) China \n\tb) USA  \n\tc) Japan \n\td) Germany  \nAnswer: " : "b", "Which country has the smallest area in meters squared? \n\ta) Monaco \n\tb) Vatican City  \n\tc) Nauru \n\td) Marshall Islands \nAnswer: " : "b", "Which Country has won the most gold medals? \n\ta) USA \n\tb) Germany \n\tc) Italy \n\td) France \nAnswer: " : "a", "Which country has the strongest military? \n\ta) Israel  \n\tb) China \n\tc) Russia  \n\td) Iran  \nAnswer: " : "c", "Which country is home to the Eiffel Tower? \n\ta) France \n\tb) Italy  \n\tc) Germany \n\td) Japan \nAnswer: " : "a", "Which country has the largest nuclear arsenal? \n\ta) USA \n\tb) Russia \n\tc) United Kingdom  \n\td) China  \nAnswer: " : "b", "Which country is home to the Great Wall? \n\ta) New Zealand \n\tb) Australia  \n\tc) China  \n\td) Denmark  \nAnswer: " : "c", "Which country is the best to live in based on the quality of life? \n\ta) Demark \n\tb) Sweden \n\tc) Australia \n\td) Finland \nAnswer: " : "b"}
  while q<10:
    for key in cq:
      user_answer=input(key).lower().strip()
      if cq.get(key)==user_answer and user_answer in valid_ans:
          print("Correct!")
          print(border)
          correct+=1
          q+=1
          break
      elif cq.get(key)!=user_answer and user_answer in valid_ans:
          print("Incorrect!")
          print(border)
          q+=1
          break
      else:
          print("That is not one of the options. Try a,b,c or d.")

def squestions():
  global correct
  correct = 0
  q = 0
  sq = {"You have chosen the sports theme. \n\nWhich team won the FIFA world cup in 2022? \n\ta) Portugal \n\tb) Brazil \n\tc) Argentina \n\td) USA \nAnswer: " : "c", "Which team won the NBA Championship in 2022? \n\ta) Golden State Warriors \n\tb) Los Angeles Lakers \n\tc) Toronto Raptors \n\td) Memphis Grizzlies \nAnswer: " : "a", "Who has the world record for the 100m sprint? \n\ta) Usain Bolt \n\tb) Micheal Phelps \n\tc) LeBron James \n\td) Cristiano Ronaldo  \nAnswer: " : "a", "When did Usain Bolt set the world record of 9.58s in the 100m sprint? \n\ta) 2007 \n\tb) 2008 \n\tc) 2009 \n\td) 2010 \nAnswer: " : "c", "Which person has the most Olympic gold medals? \n\ta) Usain Bolt \n\tb) Mark Spitz \n\tc) Micheal Phelps \n\td) Ian Thorpe \nAnswer: " : "a", "Who has the most goals scored in their career? \n\ta)Cristiano Ronaldo \n\tb)Lionel Messi \n\tc)Pele \n\td)LeBron James \nAnswer: " : "a", "Which NFL player has the most touchdowns in NFL history? \n\ta) Tom Brady \n\tb) Jerry Rice \n\tc) Aaron Rodgers \n\td) Jalen Ramsey \nAnswer: " : "b", "Who won the Men's Tennis Wimbledon in 2022? \n\ta) Serena Williams \n\tb) Rafael Nadal \n\tc) Roger Federer \n\td) Novak Djokovic \nAnswer: " : "d", "Who won the Women's Tennis Wimbledon in 2022? \n\ta) Serena Williams \n\tb) Ons Jabeur \n\tc) Elena Rybakina \n\td) Coco Gauff \nAnswer: " : "c", "What does NBA stand for? \n\ta) New Balance Association \n\tb) North Boulders Alliance \n\tc) National Basketball Association \n\td) Northern Belarus Armies \nAnswer: " : "c"}
  while q<10:
    for key in sq.keys():
      while True:
        user_answer=input(key).lower().strip()
        if sq.get(key)==user_answer and user_answer in valid_ans:
            print("Correct!")
            print(border)
            correct+=1
            q+=1
            break
        elif sq.get(key)!=user_answer and user_answer in valid_ans:
            print("Incorrect!")
            print(border)
            q+=1
            break
        else:
            print("That is not one of the options. Try a,b,c or d.")

def pquestions():
  global correct
  correct = 0
  q=0
  pq = {"You have chosen the physics theme. \n\nWhat is velocity measured in? \n\ta) Meters Per Second \n\tb) Kilometers Per Hour \n\tc) Meter Per Hour \n\td) Kilometers Per Second \nAnswer: " : "a", "What is distance measured in? \n\ta) Meters \n\tb) Yards \n\tc) Kilometers \n\td) Centimeters \nAnswer: " : "a", "What is time measured in? \n\ta) Hours \n\tb) Minutes \n\tc) Seconds \n\td) Nanoseconds \nAnswer: " : "c", "Which particle/ray is the best penetrator, alpha, beta, or gamma? \n\ta) Alpha \n\tb) Beta \n\tc) Gamma \n\td) I don't know \nAnswer: " : "c", "Which particle/ray is the best ioniser, alpha, beta or gamma? \n\ta) Alpha \n\tb) Beta \n\tc) Gamma \n\td) I don't know \nAnswer: " : "a", "What is force measured in? \n\ta) Newtons \n\tb) Pascals \n\tc) Hertz \n\td) Watts \nAnswer: " : "a", "What is power measured in? \n\ta) Kilos \n\tb) Newtons \n\tc) Joules \n\td) Watts \nAnswer: " : "d", "What is work measured in? \n\ta) Hours \n\tb) Joules \n\tc) Newtons \n\td) Pascals \nAnswer: " : "b", "If a car was travelling 10 meters per second for 4 seconds, how far did it travel? \n\ta) 0.4m \n\tb) 4m \n\tc) 40m \n\td) 400m \nAnswer: " : "c", "If a plane travelled 1000m in 5 seconds, what was its velocity? \n\ta) 20 m/s \n\tb) 400m/s \n\tc) 200 m/s \n\td) 100m/s \nAnswer: " : "c"}
  while q<10:
    for key in pq.keys():
      while True:
        user_answer=input(key).lower().strip()
        if pq.get(key)==user_answer and user_answer in valid_ans:
            print("Correct!")
            print(border)
            correct+=1
            q+=1
            break
        elif pq.get(key)!=user_answer and user_answer in valid_ans:
            print("Incorrect!")
            print(border)
            q+=1
            break
        else:
            print("That is not one of the options. Try a,b,c or d.")

def play_again():
  while True:
      play = str(input("That was fun... Play again? y/n: ")).lower().strip()
      if play in yes:
        break
      elif play in no:
        print("Thanks for playing!")
        exit() 
      else:
        print("That is not one of the options. Try y or n.")

def intro():
  while True:
    instructions = str(input("Hello and welcome to this Multi Choice Quiz! \n\nDo you need instructions to play, y/n? ")).lower().strip()
    if instructions in yes:
      print("\nWelcome to this MultiChoice quiz, before the quiz begins you will be asked which theme you want to play, either type which theme or enter a number between 1 and 3. \n\nOnce you have chosen a theme questions will be asked, then you will have 4 options to choose from, type a, b, c or d to answer. \n\nHave fun!")
      print(border)
      break
    elif instructions in no:
      print(border)
      break
    else:
      print("That's not one of the options. Try y or n.")

border = "***************************************************************"
valid_ans = ["a", "b", "c", "d"]
yes = ["y","yes"]
no = ["n","no"]
play = "y"



intro()
while play in yes:
  while True:
    theme = str(input("\n\nWelcome to this Multi Choice quiz, we have 3 themes available, \n\t1. Countries \n\t2. Sports \n\t3. Physics \nWhich Theme would you like to play? \nAnswer: "))
    if theme == "1":
      print(border)
      cquestions()
      break
    elif theme == "2":
      print(border)
      squestions()
      break
    elif theme == "3":
      print(border)
      pquestions()
      break
    else:
      print("That is not one of the themes. Try 1, 2 or 3.")
  
  #print score
  print("You got "+str(correct)+" right!")
  play_again()
