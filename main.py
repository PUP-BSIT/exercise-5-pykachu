score_counter = 0

print("(Bench Brian B. Bualat) 1. Which country dropped the Fat Man and Little Boy atomic bombs during World War II?")
print("A) Germany                       C) United States")
print("B) Soviet Union                  D) United Kingdom")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'C':
    print("Correct Answer: C) United States")
    score_counter += +1
else:
    print(f"{user_answer} is incorrect. The correct answer is C")
   
print()

print("(Bench Brian B. Bualat) 2. On which two Japanese cities were the atomic bombs Little Boy and Fat Man dropped?")
print("A) Tokyo and Kyoto                     C) Osaka and Yokohama")
print("B) Hiroshima and Nagasaki              D) Sapporo and Fukuoka")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'B':
    print("Correct Answer: B) Hiroshima and Nagasaki")
    score_counter += +1
else:
    print(f"{user_answer} is incorrect. The correct answer is B")
   
print()
print(f"Congratulations! You got {score_counter} out of 10 items")