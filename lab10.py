import time
from adafruit_circuitplayground.express import cpx
# Morse Code Dictionary:
morsecodedict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def input_string():
    s = input("Enter a string: ")
    s = s.split()
    s = ' '.join(s)
    s = s.lower() 
    #print("The cleaned up string is: ", s)
    new_s = ''
    for char in s:
        if (char.upper() in morsecodedict) or (char == ' '):
            new_s += char
    return new_s

def encode_string(s):
    encoded_string = ''
    for char in s:
        if char == ' ':
            encoded_string += '/'
        else:
            encoded_string += morsecodedict[char.upper()] + ' '
    return encoded_string

def set_unit_time():
    while True:
        try:
            unit_time = float(input("Enter the unit time 0~1 : "))
            if unit_time > 0 and unit_time < 1:
                break
            else:
                print("Please enter a positive number.")
                raise ValueError
        except ValueError:
            print("Please enter a number.")                        
    return unit_time

def set_color_rgb():
    while True:
        try:
            r = int(input("Enter the red value 0~255: "))
            if r >= 0 and r <= 255:
                break
            else:
                print("Please enter a number between 0 and 255.")
                raise ValueError
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            g = int(input("Enter the green value 0~255: "))
            if g >= 0 and g <= 255:
                break
            else:
                print("Please enter a number between 0 and 255.")
                raise ValueError
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            b = int(input("Enter the blue value 0~255: "))
            if b >= 0 and b <= 255:
                break
            else:
                print("Please enter a number between 0 and 255.")
                raise ValueError
        except ValueError:
            print("Please enter a number.")
    return (r, g, b)


def play_morse_code(encoded_string, unit_time, color):
    for char in encoded_string:
        if char == '.':
            cpx.pixels.fill(color)
            time.sleep(unit_time)
            cpx.pixels.fill((0, 0, 0))
            time.sleep(unit_time)
        elif char == '-':
            cpx.pixels.fill(color)
            time.sleep(unit_time * 3)
            cpx.pixels.fill((0, 0, 0))
            time.sleep(unit_time)
        elif char == ' ':
            time.sleep(unit_time * 3)
        elif char == '/':
            time.sleep(unit_time * 7)
        else:
            time.sleep(unit_time * 3)

def play_morse_code_sound(encoded_string, unit_time):
    for char in encoded_string:
        if char == '.':
            cpx.play_tone(440, unit_time)
        elif char == '-':
            cpx.play_tone(440, unit_time * 3)
        elif char == ' ':
            time.sleep(unit_time * 3)
        elif char == '/':
            time.sleep(unit_time * 7)
        else:
            time.sleep(unit_time * 3)


def main():
    s = input_string()
    encoded_string = encode_string(s)
    print("The encoded string is: ", encoded_string)
    unit_time = set_unit_time()
    color = set_color_rgb()
    play_morse_code(encoded_string, unit_time, color)
    play_morse_code_sound(encoded_string, unit_time)

if __name__ == "__main__":
    while True:
        main()
