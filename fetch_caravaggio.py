import wikipedia  # interacts with wikipedia pages
import requests  # downloads html
import os
import random


caravaggio = wikipedia.page('List of paintings by Caravaggio')  # get metadata associated with all known caravaggio paintings

# make separate folders for what will be test and training data
if not os.path.exists("test"):
    os.makedirs("test")
if not os.path.exists("training"):
    os.makedirs("training")

total_caravaggio = len(caravaggio.images)  # gets total number of paintings
total_test = int(total_caravaggio * 0.8)  # determines number that will be allocated to 80% test set


# randomly decides what paintings are in test set so not to bias by particular career phase
random.seed(100)
test_set = random.sample(range(total_caravaggio), total_test)


# downloads and assigns painting to test or training set
for i, painting in enumerate(caravaggio.images):

    if i in test_set:
        f = open("test/" + "Caravaggio_" + str(i) + ".jpg", 'wb')

    else:
        f = open("training/" + "Caravaggio_" + str(i) + ".jpg", 'wb')

    f.write(requests.get(painting).content)
    f.close()

