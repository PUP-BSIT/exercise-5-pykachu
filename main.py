score_counter = 0

print("(Bench Brian B. Bualat) 1. Which country dropped the Fat Man and Little Boy atomic bombs during World War II?")
print("A) Germany                       C) United States")
print("B) Soviet Union                  D) United Kingdom")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'C':
    print("Correct Answer: C) United States")
    score_counter += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is C")
   
print()

print("(Bench Brian B. Bualat) 2. On which two Japanese cities were the atomic bombs Little Boy and Fat Man dropped?")
print("A) Tokyo and Kyoto                     C) Osaka and Yokohama")
print("B) Hiroshima and Nagasaki              D) Sapporo and Fukuoka")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'B':
    print("Correct Answer: B) Hiroshima and Nagasaki")
    score_counter += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is B")

print()

print("(Michael Rua S. Maestre) 3. What event marked the official independence of the Philippines from the United States?")
print("A) Proclamation of Philippine Independence (1898)        C) Tydings-McDuffie Act (1934)")
print("B) Treaty of Paris (1898)                                D) Philippine Independence Day (1946)")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'D':
    print("Correct Answer: D) Philippine Independence Day (1946)")
    score_counter += 1
else:
     print(f"{user_answer} is incorrect. The correct answer is D")

print ()

print("(Michael Rua S. Maestre) 4. Who was the only Philippine president to serve during both the Commonwealth and the Third Republic?")
print("A) Sergio Osmeña                                C) Manuel L. Quezon")
print("B) Manuel Roxas                                 D) Elpidio Quirino")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'B':
    print("Correct Answer: B) Manuel Roxas")
    score_counter += 1
else:
     print(f"{user_answer} is incorrect. The correct answer is B")

print()

print("(Zcintilla R. Serquiña) 5. What color are the hottest stars?")
print("A) Red                               C) Yelllow") 
print("B) Blue                              D) White")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'B':
    print("Correct Answer: B) Blue")
    score_counter += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is B")
   
print()

print("(Zcintilla R. Serquiña) 6. What is the correct arrangement of the Sun, Moon, and Earth during a lunar eclipse?")
print("A) Sun - Moon - Earth             C) Earth - Sun - Moon")
print("B) Moon - Sun - Earth             D) Sun - Earth - Moon")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'D':
    print("Correct Answer: D) Sun - Earth - Moon")
    score_counter += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is D")  

print()

print("(Rica Genevive B. Salespara) 7. What was the name of the first smartphone released by IBM in 1994?") 
print("A) BlackBerry                        C) Simon Personal Communicator")
print("B) Nokia 9000 Communicator           D) Palm Pilot")

user_answer = input("Enter your answer: ").upper()
if user_answer == "C":
    print("Correct Answer: C) Simon Personal Communicator")
    score_counter += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is C) Simon Personal Communicator")

print ()

print("(Rica Genevive B. Salespara) 8. Who is often referred to as the 'Father of Computers'?") 
print("A) Charles Babbage                   C) Alan Turing")
print("B) Steve Jobs                        D) Thomas Edison")

user_answer = input("Enter your answer: ").upper()
if user_answer == "A":
    print("Correct Answer: A) Charles Babbage")
    score_counter += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is A) Charles Babbage")

print()
print(f"Congratulations! You got {score_counter} out of 10 items") 

