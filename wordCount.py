import sys  # command line arguments

text = sys.argv[1]
output = sys.argv[2]

list_ = []
with open(text, 'r') as reader:
    # read the contents and split the contents by space and save them in words list
    words = reader.read().strip().split(' ')

for word in words:
    # separating words like "new-line;" or "open\ndoor", "it's", etc. in the words list and then split them
    word = word.replace('--', '\n').replace('-', '\n').replace('\'', '\n').replace(',', '').replace('.', '').replace(';', '').replace(':', '').lower().split('\n')
    # add each word to the list
    list_ = list_ + word

# remove an empty string that i found in the list
while "" in list_: list_.remove("")

# loop through the list, add each word to the dictionary and its count
dictionary = {}
for word in list_:
    count = list_.count(word)  # count how many occurrences have each word in the list, then add it to the dictionary
    dictionary[word] = count   

# open file to write to it
with open(output, 'w') as file:
    for key in sorted(dictionary):
        file.write(key + ' ' + str(dictionary[key]) + '\n')