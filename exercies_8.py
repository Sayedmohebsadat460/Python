# even or odd project checking
Q_1 = input("what is 10 even or odd: ")
Q_2 = input("what is 3 even or odd: ")
Q_3 = input("Where is AFG Capital: ")
Score = 0

if Q_1.lower() == "even":
    Score += 1

if Q_2.lower() == "odd":
    Score += 1

if Q_3.lower() == "kabul":
    Score += 1

print(f"Your score is: {Score}")
