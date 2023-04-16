#Working on writing the current questions for sports & physics, code works smoothly with no value or text errors.
#To do: Write comments, document testing, finish flowchart

correct = 0
physics = ["Physics", "physics"]
sports = ["Sports", "sports"]
countries = ["Countries", "countries"]
valid_answers = ["A", "a", "B", "b", "C", "c", "D", "d"]
a = ["A", "a"]
b = ["B", "b"]
c = ["C", "c"]
d = ["D", "d"]

while True:
 theme = str(input("Welcome to this Multi Choice quiz, we have 3 themes available, \n\t1. Countries \n\t2. Sports \n\t3. Physics \nWhich Theme would you like to play? "))
 if theme in countries:
   while True:
    c1 = str(input("Which country has the largest area in meters squared? \n\ta) USA \n\tb) New Zealand  \n\tc) Canada  \n\td) Russia  \nAnswer: "))
    if c1 in valid_answers:
      if c1 in d:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 1 answer correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 1 answer correct so far.")
       break
    else:
      print("That is not one of the options. Try Again.")
   while True:
    c2 = str(input("Which country has the largest population? \n\ta) Brazil \n\tb) India \n\tc) China  \n\td) Nigeria  \nAnswer: "))
    if c2 in valid_answers:
      if c2 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 2 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 2 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c3 = str(input("Which country has the largest GDP? (2020) \n\ta) China \n\tb) USA  \n\tc) Japan \n\td) Germany  \nAnswer: "))
    if c3 in valid_answers:
      if c3 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 3 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 3 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c4 = str(input("Which country has the smallest area in meters squared? \n\ta) Monaco \n\tb) Vatican City  \n\tc) Nauru \n\td) Marshall Islands \nAnswer: "))
    if c4 in valid_answers:
      if c4 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 4 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 4 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c5 = str(input("Which Country has won the most gold medals? \n\ta) USA \n\tb) Germany \n\tc) Italy \n\td) France \nAnswer: "))
    if c5 in valid_answers:
      if c5 in a:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 5 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 5 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c6 = str(input("Which country has the strongest military? \n\ta) Israel  \n\tb) China \n\tc) Russia  \n\td) Iran  \nAnswer: "))
    if c6 in valid_answers:
      if c6 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 6 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 6 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c7 = str(input("Which country is home to the Eiffel Tower? \n\ta) France \n\tb) Italy  \n\tc) Germany \n\td) Japan \nAnswer: "))
    if c7 in valid_answers:
      if c7 in a:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 7 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 7 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c8 = str(input("Which country has the largest nuclear arsenal? \n\ta) USA \n\tb) Russia \n\tc) United Kingdom  \n\td) China  \nAnswer: "))
    if c8 in valid_answers:
      if c8 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 8 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 8 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c9 = str(input("Which country is home to the Great Wall? \n\ta) New Zealand \n\tb) Australia  \n\tc) China  \n\td) Denmark  \nAnswer: "))
    if c9 in valid_answers:
      if c9 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 9 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 9 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    c10 = str(input("Which country is the best to live in based on the quality of life? \n\ta) Demark \n\tb) Sweden \n\tc) Australia \n\td) Finland \nAnswer: "))
    if c10 in valid_answers:
      if c10 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 10 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 10 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")


 elif theme in sports:
   while True:
    s1 = str(input(""))
    if s1 in valid_answers:
      if s1 in d:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 1 answer correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 1 answer correct so far.")
       break
    else:
      print("That is not one of the options. Try Again.")
   while True:
    s2 = str(input(""))
    if s2 in valid_answers:
      if s2 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 2 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 2 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s3 = str(input(""))
    if s3 in valid_answers:
      if s3 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 3 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 3 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s4 = str(input(""))
    if s4 in valid_answers:
      if s4 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 4 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 4 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s5 = str(input(""))
    if s5 in valid_answers:
      if s5 in a:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 5 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 5 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s6 = str(input(""))
    if s6 in valid_answers:
      if s6 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 6 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 6 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s7 = str(input(""))
    if s7 in valid_answers:
      if s7 in a:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 7 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 7 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s8 = str(input(""))
    if s8 in valid_answers:
      if s8 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 8 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 8 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s9 = str(input(""))
    if s9 in valid_answers:
      if s9 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 9 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 9 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    s10 = str(input(""))
    if s10 in valid_answers:
      if s10 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 10 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 10 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")

 elif theme in physics:
   while True:
    p1 = str(input(""))
    if p1 in valid_answers:
      if p1 in d:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 1 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 1 answers correct so far.")
       break
    else:
      print("That is not one of the options. Try Again.")
   while True:
    p2 = str(input(""))
    if p2 in valid_answers:
      if p2 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 2 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 2 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p3 = str(input(""))
    if p3 in valid_answers:
      if p3 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 3 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 3 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p4 = str(input(""))
    if p4 in valid_answers:
      if p4 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 4 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 4 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p5 = str(input(""))
    if p5 in valid_answers:
      if p5 in a:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 5 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 5 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p6 = str(input(""))
    if p6 in valid_answers:
      if p6 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 6 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 6 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p7 = str(input(""))
    if p7 in valid_answers:
      if p7 in a:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 7 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 7 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p8 = str(input(""))
    if p8 in valid_answers:
      if p8 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 8 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 8 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p9 = str(input(""))
    if p9 in valid_answers:
      if p9 in c:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 9 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 9 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")
   while True:
    p10 = str(input(""))
    if p10 in valid_answers:
      if p10 in b:
        correct = correct + 1
        print("Correct! You have ",correct,"out of 10 answers correct so far.")
        break
      else:
       print("Incorrect! You have ",correct,"out of 10 answers correct so far.")
       break
    else:
     print("That is not one of the options. Try Again.")

 else:
   print("That is not one of the themes. Try again.")
