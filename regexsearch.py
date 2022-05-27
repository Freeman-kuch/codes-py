#! Python 3
# Regex search
# Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression

from pathlib import Path
import re, pyperclip

# write the regex of the pattern in the .txt to be searched
RegexSearch = re.compile(r'Freeman')  # the text can be anything, depending on the user

# write the path to the folder to be scanned for .txt files
p = Path('C://Users//opara//PycharmProjects')  # Path of the files to be opened and searched
files = list(p.glob('*.txt'))

# code to open all the files in the folder with the match
for file in files:
    print(f'OPENING {file}...')
    shit = open(file, 'r')
    result = RegexSearch.findall(shit.read())
    print(result)