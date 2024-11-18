book="books/frankenstein.txt"
import string

def word_count(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    
    words=file_contents.split()
    return len(words)

def letter_count(filepath):
    with open(filepath) as f:
        file_contents=f.read()

    file_contents_lower= file_contents.lower()
    lowercase_letters_list = list(string.ascii_lowercase)

    dict={}

    for letter in lowercase_letters_list :
        count=0
        for char in file_contents_lower:
            if char == letter:
                count +=1
        dict[letter]=count
    
    return dict

def print_report(filepath):
    print(f'--- Begin report of {filepath} ---')
    print(f'{word_count(filepath)} words found in the document')
    print()
    dict = letter_count(filepath)
    for letter in dict:
        print(f'The {letter} character was found {dict[letter]} times')
    print('--- End report ---')

print_report(book)