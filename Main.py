MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/' 
}

def text_to_morse(text):
    text = text.upper()
    morse = []
    for char in text:
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
        else:
            morse.append('?')
    return ' '.join(morse)

user_text = input("Enter your text to be converted: ")
morse_code = text_to_morse(user_text)

print(f"The code converted: {morse_code}")