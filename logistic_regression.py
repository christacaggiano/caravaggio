from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, precision_recall_fscore_support
import numpy as np
from PIL import Image
import glob


def get_data_labels(directory):
    labels = []
    data = []
    filenames = []

    for filename in glob.glob(directory + "/*_bw_64x64.png"):
        filenames.append(filename)
        im = Image.open(filename)
        img_vals = list(im.getdata())
        data.append(img_vals)

        if "Caravaggio" in filename:
            labels.append(1)
        else:
            labels.append(0)

    labels = np.array(labels)
    data = np.array(data)

    return labels.reshape(labels.shape[0], ), data.reshape(data.shape[0], data.shape[1] * data.shape[2]), filenames


training_labels, training_data, training_filenames = get_data_labels("training_bw")
test_labels, test_data, test_filenames = get_data_labels("test_bw")

logisticRegr = LogisticRegression(solver="lbfgs", max_iter=1000)
logisticRegr.fit(training_data, training_labels)

predictions = logisticRegr.predict(test_data)
score = logisticRegr.score(test_data, test_labels)

print(precision_score(predictions, test_labels, pos_label=1))
print(precision_recall_fscore_support(predictions, test_labels, pos_label=1))
print(accuracy_score(predictions, test_labels))

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)
# print(score)
