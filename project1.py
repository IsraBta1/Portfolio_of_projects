import textwrap
# welcome everyone.
print("\nHi, Welcome to the game Mad Libs. ")
welcome = ("In this game, you must fill in the blanks where a word is missing. Use your imagination to solve this fun story. ")
print(textwrap.fill(welcome, width=70))
print("\nThis is the story to solve, I hope you enjoy it and have lots of fun: ")  
# solve story
story = ("\nThe ______, if it will be _______, it could ______ without stopping until the next _______. "
"That's why ______ birds love to go there to look for _______. ")
adjusted_text = textwrap.fill(story, width= 70)
print(adjusted_text)

print("\nPlease enter the following: ")
print("---------------------------------")
animal = input("1. An animal: ")  # example: bird, dog, cat.
adjective = input("2. An adjective: ") # example: blue, yellow, green, black.
verb_1 = input("3. A verb: ") # example: flies, runs, walks.
noun_1 = input("4. A noun: ") # example: continent.
article_1 = input("5. An article: ") # example: some, a, an.
noun_2 = input("6. A noun (food): ") # example: food, meal.
print("---------------------------------")
# end of the game
print("\n--- YOUR COMPLETED STORY ---")
final_story = (f"The {animal}, if it will be {adjective}, it could {verb_1} without stopping until the next {noun_1}. "
               f"That's why {article_1} birds love to go there to look for {noun_2}. ")
print(textwrap.fill(final_story, width=70))