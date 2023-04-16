#These variables that follow define important sections of the programme
correct = 0
#correct contains the amount of correct answers the user has
physics = ["Physics", "physics"]
sports = ["Sports", "sports"]
countries = ["Countries", "countries"]
valid_answers = ["A", "a", "B", "b", "C", "c", "D", "d"]
yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]
a = ["A", "a"]
b = ["B", "b"]
c = ["C", "c"]
d = ["D", "d"]
#the following is a list in order to accept both capital and lowercase
#Also is is much easier to use on a larger scale than having to use .capitalise() for each variable
play = "Yes"
#play is defined to see if user wants to play programme, it starts as yes in order to run the code
border = "***************************************************************"
#border
def play_again():
  while True:
      play = str(input("That was fun... Play again? y/n: "))
      if play in yes:
        break
      elif play in no:
        print("Thanks for playing!")
        exit() 
      else:
        print("That is not one of the options. Try y or n.")
#play agin function is defined in order to give the user an ability to replay the programme after finishing
while play in yes:
  while True:
   print(border)
   theme = str(input("Welcome to this Multi Choice quiz, we have 3 themes available, \n\t1. Countries \n\t2. Sports \n\t3. Physics \nWhich Theme would you like to play? \nAnswer: "))
   print(border)
   if theme in countries or theme == "1":
     while True:
      c1 = str(input("Which country has the largest area in meters squared? \n\ta) USA \n\tb) New Zealand  \n\tc) Canada  \n\td) Russia  \nAnswer: "))
      print(border)
      if c1 in valid_answers:
        if c1 in d:
          correct += 1
          print("Correct! You have ",correct,"out of 1 answer correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 1 answer correct so far.")
         print(border)
         break
      else:
        print("That is not one of the options. Try a,b,c or d.")
        print(border)
     while True:
      c2 = str(input("Which country has the largest population? \n\ta) Brazil \n\tb) India \n\tc) China  \n\td) Nigeria  \nAnswer: "))
      print(border)
      if c2 in valid_answers:
        if c2 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 2 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 2 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c3 = str(input("Which country has the largest GDP? (2020) \n\ta) China \n\tb) USA  \n\tc) Japan \n\td) Germany  \nAnswer: "))
      print(border)
      if c3 in valid_answers:
        if c3 in b:
          correct += 1
          print("Correct! You have ",correct,"out of 3 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 3 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c4 = str(input("Which country has the smallest area in meters squared? \n\ta) Monaco \n\tb) Vatican City  \n\tc) Nauru \n\td) Marshall Islands \nAnswer: "))
      print(border)
      if c4 in valid_answers:
        if c4 in b:
          correct += 1
          print("Correct! You have ",correct,"out of 4 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 4 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c5 = str(input("Which Country has won the most gold medals? \n\ta) USA \n\tb) Germany \n\tc) Italy \n\td) France \nAnswer: "))
      print(border)
      if c5 in valid_answers:
        if c5 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 5 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 5 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c6 = str(input("Which country has the strongest military? \n\ta) Israel  \n\tb) China \n\tc) Russia  \n\td) Iran  \nAnswer: "))
      print(border)
      if c6 in valid_answers:
        if c6 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 6 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 6 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c7 = str(input("Which country is home to the Eiffel Tower? \n\ta) France \n\tb) Italy  \n\tc) Germany \n\td) Japan \nAnswer: "))
      print(border)
      if c7 in valid_answers:
        if c7 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 7 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 7 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c8 = str(input("Which country has the largest nuclear arsenal? \n\ta) USA \n\tb) Russia \n\tc) United Kingdom  \n\td) China  \nAnswer: "))
      print(border)
      if c8 in valid_answers:
        if c8 in b:
          correct += 1
          print("Correct! You have ",correct,"out of 8 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 8 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c9 = str(input("Which country is home to the Great Wall? \n\ta) New Zealand \n\tb) Australia  \n\tc) China  \n\td) Denmark  \nAnswer: "))
      print(border)
      if c9 in valid_answers:
        if c9 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 9 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 9 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      c10 = str(input("Which country is the best to live in based on the quality of life? \n\ta) Demark \n\tb) Sweden \n\tc) Australia \n\td) Finland \nAnswer: "))
      print(border)
      if c10 in valid_answers:
        if c10 in b:
          correct += 1
          print("Correct! You have ",correct,"out of 10 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 10 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
       
     play_again()
       
     
   elif theme in sports or theme == "2":
     while True:
      s1 = str(input("Which team won the FIFA world cup in 2022? \n\ta) Portugal \n\tb) Brazil \n\tc) Argentina \n\td) USA \nAnswer: "))
      print(border)
      if s1 in valid_answers:
        if s1 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 1 answer correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 1 answer correct so far.")
         print(border)
         break
      else:
        print("That is not one of the options. Try a,b,c or d.")
        print(border)
     while True:
      s2 = str(input("Which team won the NBA Championship in 2022? \n\ta) Golden State Warriors \n\tb) Los Angeles Lakers \n\tc) Toronto Raptors \n\td) Memphis Grizzlies \nAnswer: "))
      print(border)
      if s2 in valid_answers:
        if s2 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 2 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 2 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s3 = str(input("Who has the world record for the 100m sprint? \n\ta) Usain Bolt \n\tb) Micheal Phelps \n\tc) LeBron James \n\td) Cristiano Ronaldo  \nAnswer: "))
      print(border)
      if s3 in valid_answers:
        if s3 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 3 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 3 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s4 = str(input("When did Usain Bolt set the world record of 9.58s in the 100m sprint? \n\ta) 2007 \n\tb) 2008 \n\tc) 2009 \n\td) 2010 \nAnswer: "))
      print(border)
      if s4 in valid_answers:
        if s4 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 4 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 4 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s5 = str(input("Which person has the most Olympic gold medals? \n\ta) Usain Bolt \n\tb) Mark Spitz \n\tc) Micheal Phelps \n\td) Ian Thorpe \nAnswer: "))
      print(border)
      if s5 in valid_answers:
        if s5 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 5 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 5 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s6 = str(input("Who has the most goals scored in their career? \n\ta)Cristiano Ronaldo \n\tb)Lionel Messi \n\tc)Pele \n\td)LeBron James \nAnswer: "))
      print(border)
      if s6 in valid_answers:
        if s6 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 6 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 6 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s7 = str(input("Which NFL player has the most touchdowns in NFL history? \n\ta) Tom Brady \n\tb) Jerry Rice \n\tc) Aaron Rodgers \n\td) Jalen Ramsey \nAnswer: "))
      print(border)
      if s7 in valid_answers:
        if s7 in b:
          correct += 1
          print("Correct! You have ",correct,"out of 7 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 7 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s8 = str(input("Who won the Men's Tennis Wimbledon in 2022? \n\ta) Serena Williams \n\tb) Rafael Nadal \n\tc) Roger Federer \n\td) Novak Djokovic \nAnswer: "))
      print(border)
      if s8 in valid_answers:
        if s8 in d:
          correct += 1
          print("Correct! You have ",correct,"out of 8 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 8 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s9 = str(input("Who won the Women's Tennis Wimbledon in 2022? \n\ta) Serena Williams \n\tb) Ons Jabeur \n\tc) Elena Rybakina \n\td) Coco Gauff \nAnswer: "))
      print(border)
      if s9 in valid_answers:
        if s9 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 9 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 9 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      s10 = str(input("What does NBA stand for? \n\ta) New Balance Association \n\tb) North Boulders Alliance \n\tc) National Basketball Association \n\td) Northern Belarus Armies \nAnswer: "))
      print(border)
      if s10 in valid_answers:
        if s10 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 10 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 10 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
       
     play_again()
  
   elif theme in physics or theme == "3":
     while True:
      p1 = str(input("What is velocity measured in? \n\ta) Meters Per Second \n\tb) Kilometers Per Hour \n\tc) Meter Per Hour \n\td) Kilometers Per Second \nAnswer: "))
      print(border)
      if p1 in valid_answers:
        if p1 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 1 answer correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 1 answer correct so far.")
         print(border)
         break
      else:
        print("That is not one of the options. Try a,b,c or d.")
        print(border)
     while True:
      p2 = str(input("What is distance measured in? \n\ta) Meters \n\tb) Yards \n\tc) Kilometers \n\td) Centimeters \nAnswer: "))
      print(border)
      if p2 in valid_answers:
        if p2 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 2 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 2 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p3 = str(input("What is time measured in? \n\ta) Hours \n\tb) Minutes \n\tc) Seconds \n\td) Nanoseconds \nAnswer: "))
      print(border)
      if p3 in valid_answers:
        if p3 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 3 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 3 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p4 = str(input("Which particle/ray is the best penetrator, alpha, beta, or gamma? \n\ta) Alpha \n\tb) Beta \n\tc) Gamma \n\td) I don't know \nAnswer: "))
      print(border)
      if p4 in valid_answers:
        if p4 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 4 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 4 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p5 = str(input("Which particle/ray is the best ioniser, alpha, beta or gamma? \n\ta) Alpha \n\tb) Beta \n\tc) Gamma \n\td) I don't know \nAnswer: "))
      print(border)
      if p5 in valid_answers:
        if p5 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 5 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 5 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p6 = str(input("What is force measured in? \n\ta) Newtons \n\tb) Pascals \n\tc) Hertz \n\td) Watts \nAnswer: "))
      print(border)
      if p6 in valid_answers:
        if p6 in a:
          correct += 1
          print("Correct! You have ",correct,"out of 6 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 6 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p7 = str(input("What is power measured in? \n\ta) Kilos \n\tb) Newtons \n\tc) Joules \n\td) Watts \nAnswer: "))
      print(border)
      if p7 in valid_answers:
        if p7 in d:
          correct += 1
          print("Correct! You have ",correct,"out of 7 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 7 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p8 = str(input("What is work measured in? \n\ta) Hours \n\tb) Joules \n\tc) Newtons \n\td) Pascals \nAnswer: "))
      print(border)
      if p8 in valid_answers:
        if p8 in b:
          correct += 1
          print("Correct! You have ",correct,"out of 8 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 8 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p9 = str(input("If a car was travelling 10 meters per second for 4 seconds, how far did it travel? \n\ta) 0.4m \n\tb) 4m \n\tc) 40m \n\td) 400m \nAnswer: "))
      print(border)
      if p9 in valid_answers:
        if p9 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 9 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 9 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
     while True:
      p10 = str(input("If a plane travelled 1000m in 5 seconds, what was its velocity? \n\ta) 20 m/s \n\tb) 400m/s \n\tc) 200 m/s \n\td) 100m/s \nAnswer: "))
      print(border)
      if p10 in valid_answers:
        if p10 in c:
          correct += 1
          print("Correct! You have ",correct,"out of 10 answers correct so far.")
          print(border)
          break
        else:
         print("Incorrect! You have ",correct,"out of 10 answers correct so far.")
         print(border)
         break
      else:
       print("That is not one of the options. Try a,b,c or d.")
       print(border)
       
     play_again()
  
   else:
     print("That is not one of the themes. Try 1, 2 or 3.")
