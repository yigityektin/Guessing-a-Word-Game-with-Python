import random

word_list_animals = ["elephant", "snake", "giraffe", "cat", "dog", "bee", "mosquito", "turtle", "ant", "horse",
                     "squirrel", "bird", "hamster", "fish", "sheep", "lamb", "goose", "turkey", "rabbit",
                     "tiger", "monkey", "wolf", "fox", "bear", "deer", "camel", "rhino", "mouse", "shark",
                     "zebra", "hedgehog", "frog", "lizard", "crocodile", "penguin", "dolphin", "iguana",
                     "chicken", "cow", "bull", "goat", "pig", "lion", "whale", "kangaroo", "owl", "parrot",
                     "eagle", "dove", "seagull", "falcon", "swan", "cobra", "phyton", "donkey", "ostrich",
                     "pelican", "woodpecker", "ox", "hippopotamus", "rat", "badger", "leopard", "panda",
                     "cheetah", "octopus", "mussel", "crab", "lobster", "shrimp", "eel", "squid",
                     "worm", "butterfly", "caterpillar", "flea", "fly", "scorpion", "slug"]
word_list_plants = ["acacia", "azalea", "begonia", "bergamot", "bush", "celosia", "daffodil", "jasmine",
                    "lilac", "lily", "lotus", "magnolia", "orchid", "poppy", "rose", "sunflower", "tulip",
                    "violet", "basil", "bracken", "brambles", "cactus", "cardamom", "chicory", "coriander",
                    "corn", "cumin", "dandelion", "fennel", "fern", "mushroom", "garlic", "ginger", "heather",
                    "herb", "ivy", "moss", "nettle", "parsley", "pimenta", "plantain", "rosemary", "thistle",
                    "vanilla", "wheat", "birch", "pine", "plane", "willow"]
print("WELCOME TO THE WORD GUESSING GAME")
print("---------------------------------")
print("YOU HAVE 11 ATTEND TO GUESS")
print("---------------------------")
print("THE GAME STARTS WITH 1100 POINTS AND IF YOU MADE MISTAKE IT GETS DOWN 100 POINTS")
print("--------------------------------------------------------------------------------")
category_choice = input("Which category you want to compete in (Animal or Plant)? ")
category_choice = category_choice.lower()

all_words = word_list_animals.extend(word_list_plants)

starting_point = 1100
current_point = ""
random_word = ""
choice_limit = 5
current_choice_number = 0
guess = ""
guess_limit = 11
guess_count = 0
continue_ask = ""
attend_counter = 0
category_ask = ""
th_add = ""
else_of_category_ask = ""
else_limit_of_category_ask = 3
else_of_category_ask_counter = 0
else_of_continue_ask = ""
else_limit_of_continue_ask = 3
else_of_continue_ask_counter = 0

if category_choice == "animal":
    random_word = random.choice(word_list_animals)
elif category_choice == "plant":
    random_word = random.choice(word_list_plants)
else:
    print("Choose Animal or Plant")
    current_choice_number += 1
    if current_choice_number < choice_limit:
        category_choice = input("Which category you want to compete in (Animal or Plant)? ")
        category_choice = category_choice.lower()
    else:
        exit()

word_length = len(random_word)

while guess_count < guess_limit:
    if guess == random_word:
        print("YOU WIN!")
        current_point = current_point + 500
        print(f"You made {current_point} points.")
        attend_counter += 1
        continue_ask = input("Do you want to compete with another word? (Y/N): ")
        continue_ask = continue_ask.lower()
        if continue_ask == "yes":
            guess_count = 0
            starting_point = current_point + 1000
            category_ask = input("Do you want to choose your category? (Y/N): ")
            category_ask = category_ask.lower()
            if category_ask == "yes":
                category_choice = input("Which category do you want to compete in? (Animal or Plant): ")
                category_choice = category_choice.lower()
                if category_choice == "animal":
                    random_word = random.choice(word_list_animals)
                elif category_choice == "plant":
                    random_word = random.choice(word_list_plants)
                else:
                    print("Choose Animal or Plant")
                    current_choice_number += 1
                    if current_choice_number < choice_limit:
                        category_choice = input("Which category you want to compete in (Animal or Plant)? ")
                        category_choice = category_choice.lower()
                    else:
                        exit()

            elif category_ask == "no":
                random_word = random.choice.__get__(all_words)
                guess = input("Enter a guess: ")
                guess_count += 1
                print(f"You used {guess_count}. You have {guess_limit - guess_count}.")
                while guess_count + 1:
                    current_point = starting_point - 100 * guess_count
                    print(f"You have {current_point}")
                    break
                    if guess_count == 3:
                        print(f"There are {word_length} letters in the word.")
                    elif guess_count == 7:
                        changing_the_word = input("Do you want to change the word? (Y/N): ")
                        changing_the_word = changing_the_word.lower()
                        if changing_the_word == "yes":
                            guess_count = 0
                            random_word = random.choice.__get__(all_words)
                            if random_word in word_list_animals:
                                print("It is an animal")
                            else:
                                print("It is a plant")
                        elif changing_the_word == "no":
                            continue
                        elif guess_count == 9:
                            counter_of_letter = 0
                            random_letter = ""
                            while counter_of_letter < len(random_word):
                                letter_list = list(random_word[counter_of_letter])
                                counter_of_letter += 1
                                random_letter = random.choice(letter_list)
                                if counter_of_letter == 1:
                                    th_add = "st"
                                elif counter_of_letter == 2:
                                    th_add = "nd"
                                elif counter_of_letter == 3:
                                    th_add = "rd"
                                else:
                                    th_add = "th"
                            print(
                                f"One of the letter is: {random_letter} and it is {counter_of_letter}{th_add} in the "
                                f"word.")
                        else:
                            print("YOU LOSE!")
                            print(f"The word is {random_word}.")
                    else:
                        print("YES or NO.")
                        else_of_category_ask_counter += 1
                        if else_of_category_ask_counter < else_limit_of_category_ask:
                            else_of_category_ask = input("Choose: ")
                            else_of_category_ask = else_of_category_ask.lower()
                        else:
                            exit()
            elif continue_ask == "no":
                print(f"Congratulations you made {current_point} from {attend_counter} attend.")
                exit()
            else:
                print("Choose YES or No.")
                else_of_continue_ask_counter += 1
                if else_of_category_ask_counter < else_limit_of_continue_ask:
                    else_of_continue_ask = input("Choose: ")
                    else_of_continue_ask = else_of_continue_ask.lower()
                else:
                    exit()
    else:
        guess = input("Enter guess: ")
        guess_count += 1
        print(f"You used {guess_count}. You have {guess_limit - guess_count}.")
        while guess_count + 1:
            current_point = starting_point - 100 * guess_count
            print(f"You have {current_point}")
            break
        if guess_count == 3:
            print(f"There are {word_length} letters in the word.")
        elif guess_count == 7:
            changing_the_word = input("Do you want to change the word? (Y/N): ")
            changing_the_word = changing_the_word.lower()
            if changing_the_word == "yes":
                guess_count = 0
                random_word = random.choice.__get__(all_words)
                if random_word in word_list_animals:
                    print("It is an animal.")
                else:
                    print("It is a plant.")
            elif changing_the_word == "no":
                continue

        elif guess_count == 9:
            counter_of_letter = 0
            random_letter = ""
            while counter_of_letter < len(random_word):
                letter_list = list(random_word[counter_of_letter])
                counter_of_letter += 1
                random_letter = random.choice(letter_list)
            print(f"One of the letter is: {random_letter} and it is {counter_of_letter} in the word.")
    if guess_count == guess_limit and guess != random_word:
        print("Out of guesses, YOU LOSE!")
        print(f"The word is {random_word}")
