"""
Author Specific Fine Tuned Model v1

File is located at:

    https://colab.research.google.com/drive/1U3G-2k66gX1T3SAyfZtGNoZXXbhuZxtG#scrollTo=8hwMAkvFRvg8

This notebook uses GPT-2 from simpletransformers to generate fairy tale text. 
For our author specific fine tuned model, the model is fine tuned on different authors,
depending on user choice, and tested on fairy tale data from that specific author. Adjustments
to training and testing data are up to user preference.
"""

!pip install simpletransformers

import torch
# If there's a GPU available...
if torch.cuda.is_available():    
    # Tell PyTorch to use the GPU.    
    device = torch.device('cuda')
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))
# If not...
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device('cpu')

"""
Preprocess author specific fairy tale data
"""
import pandas as pd

# TODO: Grimm and HCA work, just need to get perrault parsed and find regex to parse
# ftd_cp = pd.read_csv('charles-perrault.txt', sep=r'\s{2,}', engine='python', header=None, names=['Line'])
ftd_grimm = pd.read_csv('grimm.txt', sep=r' - (?={)', engine='python', header=None, names=['Line'])
# ftd_hca = pd.read_csv('hca.txt', sep=r' - (?={)', engine='python', header=None, names=['Line'])

# lines_cp = ftd_cp['Line'].tolist()
lines_grimm = ftd_grimm['Line'].tolist()
# lines_hca = ftd_hca['Line'].tolist()

"""
Split data into 80% training and 20% testing
"""

# train_cutoff_cp = int(len(lines_cp) * 0.8)
train_cutoff_grimm = int(len(lines_grimm) * 0.8)
# train_cutoff_hca = int(len(lines_hca) * 0.8)

# Uncomment which author style the user wants the model to use for training
with open('author_specific_train.txt', 'w') as f:
    # for line in lines_cp[:-train_cutoff_cp]:
    #    f.writelines(line + '\n')
    for line in lines_grimm[:-train_cutoff_grimm]:
       f.writelines(line + '\n') 
    # for line in lines_hca[:-train_cutoff_hca]:
    #    f.writelines(line + '\n')

with open('author_specific_test.txt', 'w') as f:
    # for line in lines_cp[-train_cutoff_cp:]:
    #    f.writelines(line + '\n')
    for line in lines_grimm[-train_cutoff_grimm:]:
       f.writelines(line + '\n') 
    # for line in lines_hca[-train_cutoff_hca:]:
    #    f.writelines(line + '\n')

"""
Define GPT-2 model that is fine-tuned on fairy tales of a specific author style and evaluate it on the test data.
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
    'num_train_epochs': 5,
    'mlm': False,
}

# Create a GPT-2 model that is fine-tuned on fairy tale data of the specific author.
author_specific_fine_tuned_model = LanguageModelingModel('gpt2', 'gpt2', args=train_args)

author_specific_fine_tuned_model.train_model('author_specific_train.txt', eval_file='author_specific_test.txt')

author_specific_fine_tuned_model.eval_model('author_specific_test.txt')


"""
Generate some fairy tale text from fine-tuned GPT-2 model.
"""

from simpletransformers.language_generation import LanguageGenerationModel

# Generate fairy tale on fine-tuned model.
generator = LanguageGenerationModel('gpt2', './outputs', args={'max_length': 256})

# Prompts based on fairy tales!
prompts = [
    "Once upon a time there was a young girl who was the fairest of them all. Her sisters were jealous of her beauty.",
    "Alone in the woods was a small girl in a red cape. She was on her way to bring bread to her grandmother.",
    "A long time ago, there was a couple who wanted more than anything to have a child of their own.",
    "Out in a cave, there lived a horrible beast. Nobody dared go near it, and the cave remained untouched by the nearby village for thousands of years.",
]

for prompt in prompts:
    generated = generator.generate(prompt, verbose=False)

    generated = '.'.join(generated[0].split('.')[:-1]) + '.'
    print('\n\n' + generated)

