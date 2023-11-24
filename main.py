with open('text.txt') as f:
    code_list = f.readlines()

code_dict = {line.split('$')[0]: line.split('$')[1].strip() for line in code_list}
running = True

while running:
    text = input('Enter the text you would like to convert (quit! to exit):\n').upper()
    if text == 'QUIT!':
        print('Bye')
        running = False
    else:
        morse = ''
        for char in text:
            try:
                morse += code_dict[char]
            except KeyError:
                morse = 'there is no ' + char + ' in morse code!'
                break

        print(morse)
