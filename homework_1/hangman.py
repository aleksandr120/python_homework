# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word=set(''.join(secret_word.split(' ')))
    letters_guessed=set(letters_guessed)
    if secret_word.intersection(letters_guessed)==secret_word:
      return True
    else:
      return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    final_str=''
    secret_word_list=list(secret_word)
    secret_word_set=set(''.join(secret_word.split(' ')))
    letters_guessed_set=set(letters_guessed)
    if len(secret_word_set.intersection(letters_guessed_set))!=0:
      for i in secret_word_list:
        if i in secret_word_set.intersection(letters_guessed_set):
          final_str=final_str+i 
        else:
          final_str=final_str+'_ '
      return final_str.rstrip()
    else:
      final_str="_ "*len(secret_word)
      return final_str.rstrip()



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    final_str=string.ascii_lowercase
    for i in letters_guessed:
      final_str=final_str.replace(i,'')
    return final_str

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    string_lenght=len(secret_word)
    guesses_remaining=6
    letters_guessed=''
    warnings_remaining=3
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {string_lenght} letters long.")
    print('You have 3 warnings left.')
    while guesses_remaining>-1:
      print("-"*12)
      print(f"You have {guesses_remaining} guesses left.")
      print('Available letters: ',get_available_letters(list(letters_guessed)))
      letter_entered=input('Please guess a letter:').lower()
      if letter_entered.isalpha():
        if len(letter_entered)>1:
          warnings_remaining=warnings_remaining-1
          if warnings_remaining>-1:
            print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left:",get_guessed_word(secret_word,letters_guessed))
          else:
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
          if warnings_remaining==-1:
            guesses_remaining=guesses_remaining-1
            warnings_remaining=3
            continue
          continue
        if len(set(letter_entered).intersection(set(get_available_letters(list(letters_guessed)))))==0:
          warnings=warnings-1
          if warnings>-1:
            print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left:",get_guessed_word(secret_word,letters_guessed))
          else:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
          if warnings_remaining==-1:
            guesses_remaining=guesses_remaining-1
            warnings_remaining=3
            continue
          continue
        pass
      else:
        warnings_remaining=warnings_remaining-1
        if warnings_remaining>-1:
          print(f"Oops! That is not a valid letter. You have {warnings} warnings left:",get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
        if warnings_remaining==-1:
            guesses_remaining=guesses_remaining-1
            warnings_remaining=3
            continue
        continue
      letters_guessed=letters_guessed+letter_entered
      if len(set(letter_entered).intersection(secret_word))!=0:
        print("Good guess:",get_guessed_word(secret_word,letters_guessed))
      else:
        if letter_entered=='a'or letter_entered=='e'or letter_entered=='i'or letter_entered=='o'or letter_entered=='u':
          print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
          guesses_remaining=guesses_remaining-2
        else:
          print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
          guesses_remaining=guesses_remaining-1
      if is_word_guessed(secret_word, list(letters_guessed))==True:
        print('-'*12)
        print(f'Congratulations, you won! Your total score for this game is: {guesses_remaining*len(set(secret_word))}')
        break
      if guesses_remaining==0:
        print('-'*12)
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')
        break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    def check(my_word,other_word):
      my_word=my_word.replace('_','')
      my_word=list(my_word)
      other_word=list(other_word)
      for i in my_word:
        if my_word.count(i)<other_word.count(i):
          return False
        else:
          pass
    my_word=''.join(my_word.split())
    other_word=''.join(other_word.split())
    counter=0
    check(my_word,other_word)
    if check(my_word,other_word)==False:
      return check(my_word,other_word)
    elif len(my_word)==len(other_word):
      indexes=[i for i,c in enumerate(my_word) if c=='_']
      for i in indexes:
        other_word=other_word[:i-counter]+other_word[i+1-counter:]
        counter=counter+1
      my_word=my_word.replace('_','')
      if my_word==other_word:
        return True
      else:
        return False
    else:
      return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    long_wordlist=len(wordlist)
    final_list=[]
    i=0
    for i in range(i,long_wordlist):
      if match_with_gaps(my_word,wordlist[i])==True:
        final_list.append(wordlist[i])
    if len(final_list)==0:
      print('No matches found')
    else:
      print(' '.join(final_list))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    string_lenght=len(secret_word)
    guesses_remaining=6
    misspelled_letters=''
    letters_guessed=''
    warnings_remaining=3
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {string_lenght} letters long.")
    print('You have 3 warnings left.')
    while guesses_remaining>-1:
      print("-"*12)
      print(f"You have {guesses_remaining} guesses left.")
      print('Available letters: ',get_available_letters(list(letters_guessed)))
      letter_entered=input('Please guess a letter:').lower()
      if letter_entered=='*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      else:
        if letter_entered.isalpha():
          if len(letter_entered)>1:
            warnings_remaining=warnings_remaining-1
            if warnings_remaining>-1:
              print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left:",get_guessed_word(secret_word,letters_guessed))
            else:
              print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
            if warnings_remaining==-1:
              guesses_remaining=guesses_remaining-1
              warnings_remaining=3
              continue
            continue
          if len(set(letter_entered).intersection(set(get_available_letters(list(letters_guessed)))))==0:
            warnings=warnings-1
            if warnings>-1:
              print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left:",get_guessed_word(secret_word,letters_guessed))
            else:
              print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
            if warnings_remaining==-1:
              guesses_remaining=guesses_remaining-1
              warnings_remaining=3
              continue
            continue
          pass
        else:
          warnings_remaining=warnings_remaining-1
          if warnings_remaining>-1:
            print(f"Oops! That is not a valid letter. You have {warnings} warnings left:",get_guessed_word(secret_word,letters_guessed))
          else:
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
          if warnings_remaining==-1:
              guesses_remaining=guesses_remaining-1
              warnings_remaining=3
              continue
          continue
        letters_guessed=letters_guessed+letter_entered
        if len(set(letter_entered).intersection(secret_word))!=0:
          print("Good guess:",get_guessed_word(secret_word,letters_guessed))
        else:
          if letter_entered=='a'or letter_entered=='e'or letter_entered=='i'or letter_entered=='o'or letter_entered=='u':
            print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
            guesses_remaining=guesses_remaining-2
            misspelled_letters=misspelled_letters+letter_entered
          else:
            print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
            guesses_remaining=guesses_remaining-1
            misspelled_letters=misspelled_letters+letter_entered
        if is_word_guessed(secret_word, list(letters_guessed))==True:
          print('-'*12)
          print(f'Congratulations, you won! Your total score for this game is: {guesses_remaining*len(set(secret_word))}')
          break
        if guesses_remaining==0:
          print('-'*12)
          print(f'Sorry, you ran out of guesses. The word was {secret_word}')
          break
        
        



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
