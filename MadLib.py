#MadLib.py
#Name: William Headlee
#Date: 1/22/2026
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  word1 = input("Give me an adjective: ")
  word2 = input("Give me an animal: ")
  word3 = input("Give me a verb ending in -ing: ")
  word4 = input("Give me a noun: ")
  word5 = input("Give me something you shout: ")
  word6 = input("Give me an adverb (ending in -ly): ")
  #Print the story with the user supplied words.
  # Use an f-string (notice the 'f' before the quotes)
  print("\nYesterday, I decided to cook a " + word1 + " dinner for my family. \n" \
        "Everything was going well until a giant " + word2 + " burst into the kitchen! \n" \
          "It started " + word3 + " all over the counters. In the chaos, I accidentally \n" \
            "dropped a/an " + word4 + " into the soup. \"" + word5 + "\" ! I shouted. \n" \
              "My brother laughed " + word6 + ", and we ended up ordering pizza instead.\n")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
