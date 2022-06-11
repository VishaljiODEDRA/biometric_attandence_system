import numpy as np


#knn algorithm code
def distance(v1, v2):
    #Eucedian
    return np.sqrt(((v1 - v2)**2).sum())


def knn(train, test, k=5):
    dist = []

    for i in range(train.shape[0]):
        #this will get the vector and the label
        ix = train[i, :-1]
        iy = train[i, -1]
        #computing the distance from the test point.
        d = distance(test, ix)
        dist.append([d, iy])

    #sorting the algorithm based on distance and getting top k
    dk = sorted(dist, key=lambda x: x[0])[:k]
    #getting back only the labels(retiving)
    labels = np.array(dk)[:, -1]

    #getting frequencies of each label based on retrived label
    output = np.unique(labels, return_counts=True)
    #finding the maximum frequency and associated labels
    index = np.argmax(output[1])
    return output[0][index]
