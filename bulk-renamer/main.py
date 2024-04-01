import os

# Read the names from rename.txt
with open('rename.txt', 'r') as file:
    names = file.read().splitlines()

prefix = input('Enter the prefix of files until the number: ')

# Rename the files
for i, name in enumerate(names):
    old_name = f'{prefix}{i+1}.mp3'
    new_name = f'{name}.mp3'
    os.rename(old_name, new_name)