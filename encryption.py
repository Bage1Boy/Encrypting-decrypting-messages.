
import string
def encode_funct(user_text, user_cipher):                   # The encoding function that requires the user text and the cipher to execute
    '''
    This text recieves the text input and the cipher input from the main function. The first thing this function does is create a dictionary of the alphabet(key) and the cipher(value) together.
    Then this function takes the text and sees when the letters in it match with the alphabet, when the letters do match the letter is replaced with the value of the dictionary which is corresponding cipher letter. The function does this for each letter of the text.
    Lastly this function then returns the encrypted message back to the main function to be printed.
    '''
    alpha_bet = string.ascii_lowercase                      # Imports the lowercase alphabet
    user_cipher = list(user_cipher)                         # Turns cipher into a list
    alpha_bet = list(alpha_bet)                             # Turns alphabets into a list
    dictionary = dict(zip(alpha_bet, user_cipher))          # Creates a dictionary with the alphabet and cipher elements
    keys_list = list(dictionary.keys())                     # Turns the dictionary keys into a list
    values_list = list(dictionary.values())                 # Turns the dictionary values into a list
    en_coded = ''                                           # creates empty variable to store individual characters of the output in as the loop cycles through
    for x in user_text:                                     # A for loop function that looks at the a specific position in the text
        for y in range(len(keys_list)):                     # Looks at a specific position one at a time in the dictionary keys for each position 
            if x == keys_list[y]:                           # When the position of the user text and the dictionary keys are the same
                en_coded += values_list[y]                  # Adds the element at position y of whats in keys_list to the variable en_coded
    return (en_coded)                                       # Returns the output of the function to the mainfunction where it was called from

def decode_funct(user_text, user_cipher):                   # A function that requires the user text and the cipher to execute
    '''
    This function is what does the decoding of the provided text. The function recieves the text input and the cipher input from the main loop function.
    This function first creates the dictionary (alphabet as keys and cipher as the values) then when the letters in the text match with the cipher letter, the text letter is replaced by the alphabet letter which is of the same position as the matching ciper letter.
    Lastly, this function returns the decoded message bacck to the main loop function.
    '''
    alpha_bet = string.ascii_lowercase                      # imports the lowercase alphabet letters
    user_cipher = list(user_cipher)                         # Turns the cipher recieved by this function in the parameter into a list
    alpha_bet = list(alpha_bet)                             # Turns the  lowercase alphabet into a list
    dictionary = dict(zip(alpha_bet, user_cipher))          # Creates a dictionary with the alphabet and the cipher
    values_list = list(dictionary.values())                 # Turns the values of the dictionary into a list
    keys_list = list(dictionary.keys())                     # Turns the Keys of the dictionary into a list
    de_coded = ''                                           # An empty variable to store individual elements in of the output everytime the loop cycles to create an ouput
    for x in user_text:                                     # Defines a specific position to look at in the user text
        for y in range(len(values_list)):                   # Defines a specific position to look at in the values list
            if x == values_list[y]:                         # When the position of the list user-text and the position of values_list are the same then follow code indented beneath
                de_coded += keys_list[y]                    # Adds the element in the keys_list into the de_coded variable
    return (de_coded)                                       # Returns the output (de_coded variable) back to where this function was called from
 
print("ENDG 233 Encryption Program")
def loop_funct():                                           # A main function that just needs to be called in order to execute (does not need any arguements)
    '''Main function that calls upon other functions for encoding and decoding.
     This function asks the user for inputs for the text and the cipher.
     This function also checks to make sure that the cipher is valid, 
     checks to make sure there are no special characters in the cipher and that its alphanumeric, turns uppercase to lowercase, and removes duplicates.
     When an invalid cipher is inputted the function keeps asking for a new input until a valid one is recieved. This function only stops executing when a 0 is entered as the userdecision.
     This function also sends the output to the terminal and does not need to return anything to any other function.
    '''

    while True:                                                                                         # Infinite loop until user puts 0 as the user decision
        user_decision = int(input('Select 1 to encode or 2 to decode you message, select 0 to quit:'))  # Asks user for what they want to do
        if (user_decision == 1) :                                                                       # Executes code indented directly beneath it for when the user wants to encrypt a message
            user_text = input('Please enter the text to be processed:')                                 # Asks user for text to so the code can encrypt it
            user_cipher = input('Please enter the cipher text:')                                        # Asks user for the cipher to encrypt text with
            user_cipher1 = user_cipher.isalnum()                                                        # Checks to make sure that the cipher is only alphanumeric and contains no special characters
            if user_cipher1:                                                                            # For when the cipher is alphanumeric is True
                user_cipher2 = user_cipher.lower()                                                      # Turns uppercase letters in the cipher to lowercase
                cipher_check = list(dict.fromkeys(user_cipher2))                                        # This code removes duplicates in the cipher
                if len(cipher_check) == 26:                                                             # Makes sure that the final code the function works with is only 26 elements long
                    print ('Your cipher is valid')                                                      # Tells the user there cipher is valid
                    txt_encoded = encode_funct(user_text, cipher_check)                                 # Calls the encode function and sends it the inputed text and final valid cipher
                    print ('Your output is:', txt_encoded)                                              # prints the encrypted text in the terminal
                else : print ('Your cipher must only contain elements from the alphabet or numbers. ')  # For when the cipher requirements are not met
            else: print('Your cipher must only contain elements from the alphabet or numbers')
        elif (user_decision == 2) :                                                                     # For when the user decides to decode
            user_text = input('Please enter the text to be processed:')                                 # Asks user for text to decrypt and the cipher
            user_cipher = input('Please enter the cipher text:')
            user_cipher1 = user_cipher.isalnum()                                                        # Makes sure that cipher is alphanumeric with no special characters
            if user_cipher1:                                                                            # For when ciphers is alphanumeric is True, run code indented beneath
                user_cipher = user_cipher.lower()                                                       # Turn uppercase letters in cipher to lowercase
                cipher_check = list(dict.fromkeys(user_cipher))                                         # Removes duplicates from cipher so that each element is unique
            if len(cipher_check) == 26:                                                                 # Makes sure that the cipher is 26 charcaters long 
                print ('Your cipher is valid')                                                          # Tells user their cipher is valid
                txt_decoded = decode_funct(user_text, cipher_check)                                     # Calls decode function and sends it the final cipher and text to work with
                print ('Your output is', txt_decoded)                                                   # Prints the decoded text in the terminal
            else: print ('Your cipher must only contain elements from the alphabet or numbers')         # Tells user there cipher is invalid
        if(user_decision == 0) :                                                                        # For when when the user wants to quit, follow code indented beneath
            return 'Thank you for using the encryption program.'
            
print (loop_funct())                                                                                  # This is just to call the main function so the entire code can be executed, and prints the return statement for when the user wants to quit the program
