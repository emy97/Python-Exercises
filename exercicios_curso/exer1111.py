text = int(input('Enter the number of paragraphs: '))
comp_text = ''

for i in range(text):
    print(f'Enter paragraph {i + 1}: ')
    paragraph = input()
    comp_text += paragraph + '\n'

replacement_count = 1

for i in range(1, text + 1):
    comp_text = comp_text.replace('#', str(replacement_count), 1)
    replacement_count += 1
print(comp_text)

