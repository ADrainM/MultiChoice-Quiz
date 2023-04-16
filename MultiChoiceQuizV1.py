#Working on line 198 Don't know where to put:  
#correct_countries()
#print("You got",correct,"questions correct!")

correct = 0
physics = ["Physics", "physics"]
sports = ["Sports", "sports"]
countries = ["Countries", "countries"]
valid_answers = ["A", "a", "B", "b", "C", "c", "D", "d"]
def correct_countries():
  if c1 == "a":
    correct = correct + 1
  else:
    pass
  if c2 == "a":
    correct = correct + 1
  else:
    pass
  if c3 == "":
    correct = correct + 1
  else:
    pass
  if c4 == "":
    correct = correct + 1
  else:
    pass
  if c5 == "":
    correct = correct + 1
  else:
    pass
  if c6 == "":
    correct = correct + 1
  else:
    pass
  if c7 == "":
    correct = correct + 1
  else:
    pass
  if c8 == "":
    correct = correct + 1
  else:
    pass
  if c9 == "":
    correct = correct + 1
  else:
    pass
  if c10 == "":
    correct = correct + 1
  else:
    pass
def correct_sports():
  if s1 == "":
    correct = correct + 1
  else:
    pass
  if s2 == "":
    correct = correct + 1
  else:
    pass
  if s3 == "":
    correct = correct + 1
  else:
    pass
  if s4 == "":
    correct = correct + 1
  else:
    pass
  if s5 == "":
    correct = correct + 1
  else:
    pass
  if s6 == "":
    correct = correct + 1
  else:
    pass
  if s7 == "":
    correct = correct + 1
  else:
    pass
  if s8 == "":
    correct = correct + 1
  else:
    pass
  if s9 == "":
    correct = correct + 1
  else:
    pass
  if s10 == "":
    correct = correct + 1
  else:
    pass
def correct_physics():
  if p1 == "":
    correct = correct + 1
  else:
    pass
  if p2 == "":
    correct = correct + 1
  else:
    pass
  if p3 == "":
    correct = correct + 1
  else:
    pass
  if p4 == "":
    correct = correct + 1
  else:
    pass
  if p5 == "":
    correct = correct + 1
  else:
    pass
  if p6 == "":
    correct = correct + 1
  else:
    pass
  if p7 == "":
    correct = correct + 1
  else:
    pass
  if p8 == "":
    correct = correct + 1
  else:
    pass
  if p9 == "":
    correct = correct + 1
  else:
    pass
  if p10 == "":
    correct = correct + 1
  else:
    pass


  while True:
   theme = str(input("Welcome to this Multi Choice quiz, we have 3 themes available, \n\t1. Countries \n\t2. Sports \n\t3. Physics \nWhich Theme would you like to play? "))
   if theme in countries:
     while True:
      c1 = str(input("Which country has the largest area in meters squared? \n\ta) USA \n\tb) New Zealand  \n\tc) Canada  \n\td) Russia  \nAnswer: "))
      if c1 in valid_answers:
        break
      else:
        print("That is not one of the options. Try Again.")
     while True:
      c2 = str(input("Which country has the largest population? \n\ta) Brazil \n\tb) India \n\tc) China  \n\td) Nigeria  \nAnswer: "))
      if c2 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c3 = str(input("Whcih country has the largest GDP? (2020) \n\ta) China \n\tb) USA  \n\tc) Japan \n\td) Germany  \nAnswer: "))
      if c3 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c4 = str(input("Which country has the smallest area in meters squared? \n\ta) Monaco \n\tb) Vatican City  \n\tc) Nauru \n\td) Marshall Islands \nAnswer: "))
      if c4 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c5 = str(input("Which Country has won the most gold medals? \n\ta) USA \n\tb) Germany \n\tc) Italy \n\td) France \nAnswer: "))
      if c5 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c6 = str(input("Which country has the strongest military? \n\ta) Israel  \n\tb) China \n\tc) Russia  \n\td) Iran  \nAnswer: "))
      if c6 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c7 = str(input("Which country is home to the Eiffel Tower? \n\ta) France \n\tb) Italy  \n\tc) Germany \n\td) Japan \nAnswer: "))
      if c7 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c8 = str(input("Which country has the largest nuclear arsenal? \n\ta) USA \n\tb) Russia \n\tc) United Kingdom  \n\td) China  \nAnswer: "))
      if c8 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c9 = str(input("Which country is home to the Great Wall? \n\ta) New Zealand \n\tb) Australia  \n\tc) China  \n\td) Denmark  \nAnswer: "))
      if c9 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")
     while True:
      c10 = str(input("Which country is the best to live in based on the quality of life? \n\ta) Demark \n\tb) Sweden \n\tc) Australia \n\td) Finland \nAnswer: "))
      if c10 in valid_answers:
       break
      else:
       print("That is not one of the options. Try Again.")

 
       
 
     
   elif theme in sports:
     print("No sports quiz yet")
     break
  
   elif theme in physics:
     print("No physics quiz yet")
     break
  
   else:
     print("That is not one of the themes. Try again.")
