
#------------------------------------------Defining the ditionary to store the morse code-----------------------------------------------------------------

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

#-----------------------------------------------------------------------------------------------------------------



#-----------------------------------------Defining a function to convert the given message to morse code----------------------------------------------------------------

def to_morse_code(message):
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code
  
#---------------------------------------------------------------------------------------------------------



# ---------------Defining a function to convert morse code to text--------------------------------------

def from_morse_code(morse_code):
        
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
    return message
#-------------------------------------------------------------------------------------------------------



# Defining the main function
#---------------------------------------------------------------------------------------------------------------------
def main():
    while True:
        choice = input("Choose an option:\nPress 1 to convert text to Morse code\nPress 2 to convert Morse code to text\nPress -1 to quit\n")
        if choice == '1':
            message = input("Enter a message to convert to Morse code: ")
            morse_code = to_morse_code(message)
            print(morse_code)
        
        elif choice == '2':
            morse_code = input("Enter a Morse code sequence to convert to text: ")
            message = from_morse_code(morse_code)
            print(message)
        
        elif choice == '-1':
            print("Quitted successfully")
            break
            
        else:
            print("Invalid choice, please choose from the available options.")
#------------------------------------------------------------------------------------------------------------------

#Calling out the main finction 


if __name__ == "__main__":
    main()
