# -- Function Area

def find_who_goes_first():
  """Returns who goes first"""
  # Returns a string for better readability
  if total_beans % divisor == 0:
    return "Player"
  else:
    return "Python"

def take_beans(beans):
  """Calculates the beans Python will take"""
  return beans % divisor

def print_out_beans(beans):
  """Prints out the white beans left"""
  print("\nBeans:  ", end="")
  for i in range(0, beans):
    print("O", end=" ")
  print("8\n")

def check_number(number, minimum, maximum):
  """Makes sure a number input is correct"""
  # Returns a string for better readability
  if not number.isdigit():
    return("Invalid Input")
  number = int(number)
  if number <= maximum and number >= minimum and (type(number) == int or number % 1 == 0):
    return("Valid Input")
  else:
    return("Invalid Input")

# -- Setup Area

name = input("What is your name?: ")
print("Welcome to the bean game, " + name + "!\n")
print("Instructions: The goal is to NOT be stuck with the black bean. The white beans are represented by zeros, and the black bean is represented by an eight. Each turn, you will take some white beans. See if you can beat me! You cannot set it up so you can take more than 20 white beans per turn, and you cannot have more than 150 total white beans. The total white beans also has to be bigger than the max you can take per turn\n")

GAME_DONE = False
#Game loop
while not GAME_DONE:
  # -- Setup Area
  #The following makes sure the correct kind of number is entered for the two inputs
  while True:
    max_beans_you_can_take = input("Max white beans you can take per turn: ")
    if check_number(max_beans_you_can_take,1,20) == "Invalid Input":
      print("Invalid Input")
    else:
      break
  max_beans_you_can_take = int(max_beans_you_can_take)
  print("")

  while True:
    total_beans = input("Total white beans: ")
    if check_number(total_beans,1,150) == "Invalid Input" or int(total_beans) < max_beans_you_can_take:
      print("Invalid Input")
    else:
      break
  total_beans = int(total_beans)

  divisor = max_beans_you_can_take + 1

  print_out_beans(total_beans)

  #Decides who goes first
  goes_next = find_who_goes_first()
  if goes_next == "Python":
    print("I will go first.")
  else:
    print("You can go first.")
  completed = False
  while not completed:
    # -- Game Area
    #This part is executed when Python goes first
    if goes_next == "Python":
      if take_beans(total_beans) > 1:
        print("I take " + str(take_beans(total_beans)) + " beans.")
      else:
        print("I take 1 bean.")
      total_beans -= take_beans(total_beans)

      if total_beans == 0:
        print("\nYou got stuck with the black bean! Better luck next time!\n")
        play_again = input("Do you want to play again (y/n)?: ")
        if play_again == "y":
          print("\nOkay, if you want to see the instructions, scroll up!\n")
        else:
          GAME_DONE = True
        completed = True
      goes_next = "Player"
    #This part is executed when the player goes first
    else:
      #This part checks that the player enters a valid number
        while True:
          player_takes = input("How many beans do you want to take?: ")
          if check_number(player_takes,1,max_beans_you_can_take) == "Invalid Input":
            print("Invalid Input")
          else:
            break
        #When the player checks a valid number, it just takes the beans
        player_takes = int(player_takes)
        if player_takes > 1:
          print("You take " + str(player_takes) + " beans.")
        else:
          print("You take 1 bean.")
        total_beans -= player_takes
        goes_next = "Python"
    if not completed == True:
      print_out_beans(total_beans)
print("Okay, thanks for playing!")
