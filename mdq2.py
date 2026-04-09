morse_code_dict={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '/': ' '}

def translator(message):
    message1=message.split()
    converted=""
    for code in message1:
        converted=converted+morse_code_dict[code]
    return converted

message=input("enter the message in morse code: ")
final_message=translator(message)
print(final_message)
