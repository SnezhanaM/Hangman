from random import choice

print('H A N G M A N')
while True:
    game = input('Type "play" to play the game, "exit" to quit: ')

    if game == 'play':
        words = ['python', 'java', 'kotlin', 'javascript']
        computer_word = choice(words)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        output_word = '-' * len(computer_word)
        sett = set()

        x = 8
        while x > 0:
            print('\n' + output_word)
            input_letter = input("Input a letter: ")

            if input_letter in computer_word and input_letter not in output_word and input_letter in alphabet:
                for j in range(len(computer_word)):
                    if input_letter == computer_word[j]:
                        output_word = output_word[:j] + input_letter + output_word[j+1:]

            elif len(input_letter) != 1:
                print('You should input a single letter')

            elif input_letter not in alphabet:
                print('It is not an ASCII lowercase letter')

            elif input_letter in sett:
                print('You already typed this letter')

            elif input_letter not in computer_word:
                x -= 1
                print('No such letter in the word')

            sett.add(input_letter)

            if output_word == computer_word:
                print('You guessed the word!\nYou survived!\n')
                break

            if x == 0:
                print('You are hanged!\n')

    else:
        break
