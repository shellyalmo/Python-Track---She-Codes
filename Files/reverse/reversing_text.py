"""In this program I'm reading a text file, and writing a new file that contains each line reversed as well as each original line."""

with open('input.txt','r') as reader:
    animals = reader.readlines()

with open('output.txt','w') as writer:
    for animal in animals:
        writer.write(animal[::-1])
    for animal in animals:
        writer.write(animal)