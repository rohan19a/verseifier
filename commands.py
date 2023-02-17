import os
from read_file import bg, bgen

def verse_name_to_dict(verse_name):
    #bg 1.1
    book = verse_name.split(' ')[0]
    chapter = verse_name.split(' ')[1].split('.')[0]
    verse = verse_name.split(' ')[1].split('.')[1]

    verse_id = {'book': book, 'chapter': chapter, 'verse': verse}
    return verse_id

def verse_to_id(dict):
    #bg 1.1
    book = dict['book']
    book = which_book(book)
    chapter = dict['chapter']
    verse = dict['verse']

    #find where the chapterId in the book is equal to the chapter, and the verseId is equal to the verse
    verse_id = next((verse['externalId'] for verse in book if verse['book'] == book and verse['chapterId'] == chapter and verse['verseId'] == verse), None)

    return verse_id

verse_name_to_dict('bg 1.1')
x = verse_to_id(verse_name_to_dict('bg 1.1'))

print(x)

def which_book(book):
    case = {
        'bg': bg,
        'bgen': bgen
    }
    return case.get(book, 'Invalid book')
