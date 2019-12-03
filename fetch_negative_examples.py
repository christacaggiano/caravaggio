import glob
import random
import os

negative_examples = glob.glob("*.j*g")  # all jpgs and jpegs

total_neg_examples = len(negative_examples)
training_neg_examples = int(total_neg_examples*0.8)  # 80% of data in the training set

training_set = random.sample(range(total_neg_examples), training_neg_examples)

# move all downloaded files to the appropriate folder
for i, jpg in enumerate(negative_examples):
    if i in training_set:
        os.rename(jpg, "training/" + jpg)
    else:
        os.rename(jpg, "test/" + jpg)
