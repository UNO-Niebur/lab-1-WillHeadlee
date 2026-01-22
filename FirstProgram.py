#FirstProgram.py
#Name: William Headlee
#Date: 1/22/2026
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello")
  #Ask for the user's name
  username = input("What is your name? ")
  #Use the user's name in the program.
  print("Nice to meet you, " + username)
  #Ask the user for their age.
  age = input("Please enter your age: ")
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  print("You were most likely born in " + str(2025 - int(age)))

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
