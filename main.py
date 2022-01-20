print("hello welcome to the game! ")

answer = input("would you like to play this game? ")
playing = "yes"

if answer.lower() != "yes":
    if answer.lower() != "ok":
        quit()
else:
    print("let's go")

score = 0
score_limit = 1
n = 0
n_limit = 1


while score != score_limit:
    answer1 = input("What is banana? ")
    if answer1.lower() == "yellow fruit":
        print("correct")
        score += 1
    else:
        print("false")

while n != n_limit:
    answer2 = input("what is an orange? ")
    if answer2.lower() == "orange fruit":
        print("correct")
        n += 1
    else:
        print("false")

#print (f"you got {str((score + n)} right, Good Job!")
print("you got " + str(((score + n)/2)*100) + "%")