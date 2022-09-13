import random 

def snakeEyes():
  answer = input("Welcome! Do you want to play 'Snake Eyes'? ")
  counter = 1
  dieOne = 0
  dieTwo = 0
  list_of_valOne = []
  list_of_valTwo = []
  num_of_doubles = 0
  
  if answer.lower() == "yes":
    answerTwo = input("Great, let's play!\nType 'start' to begin! ")
    if answerTwo.lower() == "start":
   
      while dieOne + dieTwo != 2:
        dieOne = random.randint(1,6)
        dieTwo = random.randint(1,6)
        
        print(f'{counter}. Die 1:{dieOne} and Die 2:{dieTwo} ')
        list_of_valOne.append(dieOne)
        list_of_valTwo.append(dieTwo)
        counter += 1
        if dieOne == dieTwo:
          num_of_doubles += 1
  
      print(f'You got Snake Eyes!\nNumber of rolls:{counter - 1}\nNumber of doubles:{num_of_doubles}\nAvg roll for die #1:{round(sum(list_of_valOne) / len(list_of_valOne), 2)}\nAvg roll for die #2:{round(sum(list_of_valTwo) / len(list_of_valTwo), 2)}')
    else:
      print("Come back when you want to play!")
      
  else:
    print("Come back when you want to play!")
  
snakeEyes()
  