# Notions:
#   - print
#   - script
#   - variable
#   - type 
#   - loop
#   - method
#   - list
#   - length of a list
#   - comment

fname = "text1"

num_words = 0
num_characters = 0

for line in open(fname).readlines():
    line = line.rstrip('\n')

    words = line.split(' ')

print("the text has",num_words,"words")
print("the text has",num_characters,"characters")
