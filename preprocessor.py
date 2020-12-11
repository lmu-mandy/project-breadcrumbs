import pandas as pd
import re

"""
Pre-process Charles Perrault data, basically gets rid of lines with image annotations.
"""

# perrault_raw = open('data/perrault_raw.txt', 'r')
# perrault_lines = ''.join(perrault_raw.readlines())
# perrault_lines = re.sub(r'(?m)^\[\d+\]', '', perrault_lines).split('\n')
# with open('data/perrault.txt', 'w') as f:
#     for line in perrault_lines:
#         if line: f.writelines(line + '\n')

"""
Programatically create author file based on selected author. 
Also process data file into lines and split 80:20 for train:test.
"""
# author = "grimms"
# author = "andersen"
# author = "perrault"

# authors_to_file = {"grimms": 'grimms.txt', "andersen": 'andersen.txt', "perrault": 'perrault.txt'}
# author_file = authors_to_file[author]

# author_data = pd.read_csv(author_file, sep=r' - (?={)', engine='python', header=None, names=['Line'])
# author_lines = author_data['Line'].tolist()
# train_cutoff_author = int(len(author_lines) * 0.8)

# with open('author_specific_train.txt', 'w') as f:
#   for line in author_lines[:-train_cutoff_author]:
#     f.writelines(line + '\n') 

# with open('author_specific_test.txt', 'w') as f:
#   for line in author_lines[-train_cutoff_author:]:
#     f.writelines(line + '\n') 

"""
Concatenate fairy tale datasets into one combined text file. 
"""

# files = ["data/bfb.txt", "data/japanese_tales.txt"]
# with open('data/combined.txt', 'w') as outfile:
#     for file in files:
#         with open(file) as infile:
#             outfile.write(infile.read())

# Making sure parser works for combined.txt:
# data = pd.read_csv('data/combined.txt', sep=r' - (?={)', engine='python', header=None, names=['Line'])
# lines = data['Line'].tolist()
# with open('temp.txt', 'w') as f:
#   for line in lines:
#     f.writelines(line + '\n') 

"""
Concatenate author-specific data set with general fairy tale data. 
"""

# author = "grimms"
# authors_to_file = {"grimms": 'data/grimms.txt', "andersen": 'data/andersen.txt', "perrault": 'data/perrault.txt'}
# authors_to_file.pop(author)

# files = ['data/combined.txt']
# files.extend(authors_to_file.values())

# with open('combined-with-authors.txt', 'w') as outfile:
#     for file in files:
#         with open(file) as infile:
#             outfile.write(infile.read())

"""
Calculate vocab size for each author.
"""

from collections import Counter

perrault_text = open('data/perrault.txt', 'r')
andersen_text = open('data/andersen.txt', 'r')
grimms_text = open('data/grimms.txt', 'r')

perrault_lines = ''.join(perrault_text.readlines()).split()
andersen_lines = ''.join(andersen_text.readlines()).split()
grimms_lines = ''.join(grimms_text.readlines()).split()

perrault_text.close()
andersen_text.close()
grimms_text.close()

perrault_vocab_size = len(Counter(perrault_lines))
print("Perrault vocab size: " + str(perrault_vocab_size))
andersen_vocab_size = len(Counter(andersen_lines))
print("Andersen vocab size: " + str(andersen_vocab_size))
grimms_vocab_size = len(Counter(grimms_lines))
print("Grimms vocab size: " + str(grimms_vocab_size))