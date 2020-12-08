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
Process data file into lines and split 80:20 for train:test
"""
# author_data = pd.read_csv('author_data.txt', sep=r' - (?={)', engine='python', header=None, names=['Line'])
# author_lines = author_data['Line'].tolist()
# train_cutoff_author = int(len(author_lines) * 0.8)

# with open('author_specific_train.txt', 'w') as f:
#   for line in author_lines[:-train_cutoff_author]:
#     f.writelines(line + '\n') 

# with open('author_specific_test.txt', 'w') as f:
#   for line in author_lines[-train_cutoff_author:]:
#     f.writelines(line + '\n') 

"""
Concatenate author-specific data set with general fairy tale data. 
"""

# author = "grimms"
# authors_to_data = {"grimms": 'data/grimms.txt', "andersen": 'data/andersen.txt', "perrault": 'data/perrault.txt'}
# authors_to_data.pop(author)

# with open('bfb.txt', 'a') as outfile:
#     for author in authors_to_data.values():
#         with open(author) as infile:
#             outfile.write(infile.read())