##defines vowels in a list
vowels = ['a', 'e', 'i', 'o', 'u']

##takes user input
phrase = input('Enter a phrase:\n ')

##converts phrase to a list
convert_phrase = list(phrase)

##converts phrase to individual words
split_phrase = phrase.split()

##checks if the first letter is a vowel and adds "way" to the end, and if not, moves the first letter to the end and adds "ay"
for word in split_phrase:
    if word[0] in vowels:
        word += 'way'
    else:
        word = word[1:] + word[0] + 'ay'
    print(word, end=' ')
        


