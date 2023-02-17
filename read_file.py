import os
import json

#read a json file into a dictionary

def read_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

bg = read_file('books/gita-main/data/verse.json')
bgen = read_file('books/gita-main/data/translation.json')

def get_verse(externalId):
    verse = next((verse for verse in bg if verse['externalId'] == externalId), None)
    return verse['text']


def get_translation(externalId):
    translation = next((description for description in bgen if description['verse_id'] == externalId and description['lang'] == 'english'), None)
    translation = '\n'.join(translation['description'][i:i+20] for i in range(0, len(translation['description']), 20))
    return translation


def latin_number_to_indian_numbers(number):
    indian_numbers = {
        '0': '०',
        '1': '१',
        '2': '२',
        '3': '३',
        '4': '४',
        '5': '५',
        '6': '६',
        '7': '७',
        '8': '८',
        '9': '९'
    }
    return ''.join([indian_numbers[i] for i in str(number)])

def latin_to_indian(stri):
    #1.1
    chapter = stri.split('.')[0]
    verse = stri.split('.')[1]
    return latin_number_to_indian_numbers(chapter) + '.' + latin_number_to_indian_numbers(verse)