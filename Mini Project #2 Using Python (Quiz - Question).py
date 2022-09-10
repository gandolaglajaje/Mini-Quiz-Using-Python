print("Welcome to my Mini Quiz!")

score = 0

# Asking the player if they want to play
player = input("Do you want to play? ")

# Prayer input must be in lower case for formality 
if player.lower() != "yes":
    quit()

print("Let's begin!")

# Question no.1
print("Question No.1")
Answer = input("What Is the Closest Planet to Earth in the Solar System?: ")

if Answer == "Venus":
    print("You're Correct!")
    score += 1
else:
    print("Incorrect")

# Question no.2
print("Question no.2")
Answer = input("What Is The Largest Planet In The Solar System?: ")

if Answer == "Jupiter":
    print("You're Correct!")
    score += 1
else:
    print("Incorrect")

print("Your overall score " + " is " + str(score))