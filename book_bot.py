
with open("frankenstein") as f:
    file_contents = f.read()
    

def count_words(book):
    words_arr = book.split()
    return words_arr

def count_letters(book):
    word_list = count_words(book)
    letters_obj = {}
    for word in word_list:
        for letter in word:
            letter_lowered = letter.lower()
            if(letter_lowered.isalpha()):
                if(letter_lowered in letters_obj):
                    letters_obj[letter_lowered] = letters_obj[letter_lowered]+1
                else:
                    letters_obj[letter_lowered] = 1
    return letters_obj



letters_obj = count_letters(file_contents)
letters_list = []

for letter in letters_obj:
    letters_list.append((letter, letters_obj[letter]))



for letter in sorted(letters_list):
     print(f"the {letter[0]} character was found {letter[1]} times")