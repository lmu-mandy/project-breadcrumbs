# -*- coding: utf-8 -*-
"""NLP Model Fine-tuned on Specific Authors

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U3G-2k66gX1T3SAyfZtGNoZXXbhuZxtG

This notebook uses GPT-2 from simpletransformers to generate fairy tale text. 
For our author specific fine-tuned model, the model is fine-tuned on different authors, depending on user choice, and tested on fairy tale data from that specific author. Adjustments to training and testing data are up to user preference.
"""

!pip install simpletransformers

import torch
if torch.cuda.is_available():    
    device = torch.device('cuda')
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device('cpu')

"""Select which author you would like to create the model based on."""

valid_authors = ["grimms", "andersen", "perrault"]

while True:
  author = input("Please select 'Andersen', 'Grimms', or 'Perrault'. ").lower()
  if author in valid_authors:
    break
  print("Please enter a valid author.")

authors_to_file = {"grimms": 'grimms.txt', "andersen": 'andersen.txt', "perrault": 'perrault.txt'}
author_file = authors_to_file[author]

"""Preprocess author specific fairy tale data and split data into 80% training and 20% testing."""

import pandas as pd

author_data = pd.read_csv(author_file, sep=r' - (?={)', engine='python', header=None, names=['Line'])
author_lines = author_data['Line'].tolist()
train_cutoff_author = int(len(author_lines) * 0.8)

# Training data is the first 80% of the fairy tale data, testing is the last 20%
with open('author_specific_train.txt', 'w') as f:
  for line in author_lines[:-train_cutoff_author]:
    f.writelines(line + '\n') 

with open('author_specific_test.txt', 'w') as f:
  for line in author_lines[-train_cutoff_author:]:
    f.writelines(line + '\n')

"""Define GPT-2 model that is fine-tuned on fairy tales of a specific author style and evaluate it on the test data.

"""

from simpletransformers.language_modeling import LanguageModelingModel
import logging

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger('transformers')
transformers_logger.setLevel(logging.WARNING)

train_args = {
    'reprocess_input_data': True,
    'overwrite_output_dir': True,
    'train_batch_size': 32,
    'num_train_epochs': 15,
    'mlm': False,
}

# Create a GPT-2 model that is fine-tuned and evaluated on fairy tale data of the specific author.
author_specific_fine_tuned_model = LanguageModelingModel('gpt2', 'gpt2', args=train_args)

author_specific_fine_tuned_model.train_model('author_specific_train.txt', eval_file='author_specific_test.txt')

author_specific_fine_tuned_model.eval_model('author_specific_test.txt')

"""Generate some fairy tale text from fine-tuned GPT-2 model."""

from simpletransformers.language_generation import LanguageGenerationModel

# Generate fairy tale on fine-tuned model.
generator = LanguageGenerationModel('gpt2', './outputs', args={'max_length': 256})

# Prompts based on fairy tales!
prompts = [
    "Far underneath the sea, there lives a young princess who has seven sisters.",
    "Once upon a time there was a young girl who was the fairest of them all. Her sisters were jealous of her beauty.",
    "Alone in the woods was a small girl in a red cape. She was on her way to bring bread to her grandmother.",
    "A long time ago, there was a couple who wanted more than anything to have a child of their own.",
    "Out in a cave, there lived a horrible beast. Nobody dared go near it, and the cave remained untouched by the nearby village for thousands of years.",
]

for prompt in prompts:
    generated = generator.generate(prompt, verbose=False)

    generated = '.\n'.join(generated[0].split('.')[:-1]) + '.'
    print('\n\n' + generated)