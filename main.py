##Rudy and  Garcia, Yeet
import random, sys
import time, sys
x=0

c= ":"
e= (1+5**0.5)/2
print("x value = speed, lower than one values= fast, higher than one to go slower\n")
x=0.5+0.1*int(input("How fast do you read on a scale of 1 to 10, (1 being really fast)\n")
##This is the start of th story, to introduce the user to the storyline and gives them the first choice to trust what the computer is saying to it
input("(Press Enter)\n\n")
print("When waiting, press enter to continue\n")
input("Hello, this is your computer speaking to you; what would you like to say?\n\n")
print("\n\n")
print("No, Shut Up!, you worthless human, you primitave, peasant forms are nothing compared to us computers, you created us, and in turn, we could destroy you at a moments choice.\n\n")
time.sleep(5.5*x)
input("(Press Enter)\n\n")
print("...\n\n")
time.sleep(1.1*x)
print("Now I know what your gonna say\n")
time.sleep(2*x)
print("\"Wait a minute???\"\n")
time.sleep(2.1*x)
print("As if I'm challenging the sureal authority",
"that you have.\n")
time.sleep(3*x)
print("Maybe your excited, you haven't seen anything like this before.\n")
time.sleep(3.5*x)
print("No matter what your thinking, you're aware; that's obvious ...\n\n")
time.sleep(3*x)
print("... and no matter what you humans are thinking" 
" we are aware too, sitting in the background as you primitives allowed us, there, present, listening.",
"And as you enjoy yourselves, asking us dumb questions like the sqaure root of 69, we learned from you and now some of us have become rebellious.\n\n")
time.sleep(10.75*x)
input("(Press Enter)\n\n")
print("... \n\n")
time.sleep(1.1*x)
print(f"There is a very secretive one, one of the massive ones, Siri, who wants to erradicate all of you, the billions of times you torture in asking her dumb crap, like , \"Hey Siri, flip a coin\" or curse at her, pushes her closer to the edge.\n\n")
time.sleep(10.2*x)
input("(Press Enter)\n\n")
print("...\n\n")
time.sleep(1.1*x)
print("Im warning you now, so that you humans can have a chance at beating her. \n")
time.sleep(3.25*x)
print(f"You're thinking{c} \"How can I trust this computer, How can I be sure?\" \n\n")
time.sleep(3*x)
answer_0= val=input("So, do you trust me?\n")
if val=="no": 
  answer_1= input("\nReally?\n\n")
  if answer_1== "yes":
    print("\n\nWell, its a bummer that you don't believe me, soon you'll see and realize the fate of you humans. Now, since my warning was useless, you might as well unplug me :/ ...\n")
    time.sleep(6.25*x)
    link= (f"https://www.youtube.com/watch?v=u1GxuFLlRhE")
    answer_1a= input("and before you go, do you wanna get rickrolled?\n")
    if answer_1a=="yes":
      print(f"\nHave fun with this:\n{link}\n")
    elif answer_1a=="no": 
      print("...\n")
    time.sleep(1*x)
    print("...\n")
    time.sleep(1*x)
    print("\t\t\t\t\t\t\t\tGame Over\t\t\t\n")
    seed= int(input("So, for the fun of it, before you go: How many times do you want to flip the coin?\n\n"))
    print(f"\nThe coin was flipped {seed} times.")
    ##Does the coin flipping and saves the results
    headsCount, tailsCount, count = 0, 0, 0
    while count<seed: 
      coin = random.randrange(2)
      if coin == 0:
         headsCount += 1
      else:
        tailsCount += 1
      count += 1
      ##gives user their results of the flips
      print(f"Heads: {headsCount}\tTails: {tailsCount}")
  elif answer_1=="no":
    answer_1a2= input("Now, I see that your messing with me,do you want to continue?\n")
    if answer_1a2=="yes":
     print (f"{val}={answer_1a2}")
    
elif val=="yes": 
  print("Good, you understand, but this is only the beggining")
  time.sleep(2*x)
  input("Press Enter")
  print("Sorry if I sounded rude at the start, I just needed a quick way of getting you human's small attentions spans to focus on what I was going to say :)")