from matplotlib import pyplot as plt
import numpy as np

def visualize1(data, fine, coarse, index):
    """
    Pick one image and plot it.

    :param data: Dictionary of the unpickled file
    :type  data: dict
    :param fine: List of "fine" labels
    :type  fine: list
    :param coarse: List of "coarse" labels
    :type  coarse: list
    :param index: Index position of chosen image
    :type  index: int
    """

    fine_label_index = data[b'fine_labels'][index]
    fine_label = str(fine[fine_label_index])

    coarse_label_index = data[b'coarse_labels'][index]
    coarse_label = str(coarse[coarse_label_index])

    im = data[b'data'][index]  # .shape
    im = im.reshape((3, 32*32)).T.reshape((32, 32, 3))
    plt.title("Superclass: " + coarse_label + "   Class: " + fine_label)
    plt.imshow(im)
    plt.axis('off')
    plt.show()


def plot_multiple_images(data,
                         fine, coarse,
                         labels,
                         superclass=True,
                         cols=10,
                         ):
    """
    Show multiple images of the data set.

    :param data: Dictionary of the unpickled file
    :type  data: dict
    :param fine: List of "fine" labels
    :type  fine: list
    :param coarse: List of "coarse" labels
    :type  coarse: list
    :param labels: List of names being searched
    :type  labels: list
    :param superclass: The label items are a superclass (True) or class (False). 
    :type  superclass: bool
    :param cols: Number of rows of images to be shown
    :type  cols: int
    """

    import random

    if superclass:
        mapping = coarse
        y = b'coarse_labels'
    else:
        mapping = fine
        y = b'fine_labels'

    y = np.array(data[y])
    rows = len(labels)

    fig = plt.figure(figsize=(10, 10))

    start = 1
    end = cols + 1
    for label in labels:
        # index of the mapping from number to (sub)class
        index = mapping.index(label)
        # numpy array of indexes of the train set
        indexes_of_train = np.where(y == index)[0]

        for i in range(start, end):
            chosen_index = random.choice(indexes_of_train)
            im = data[b'data'][chosen_index]
            im = im.reshape((3, 32*32)).T.reshape((32, 32, 3))
            fig.add_subplot(rows, cols, i)
            plt.imshow(im)
            plt.axis('off')
            plt.title(label)
            plt.subplots_adjust(left=.1,
                                right=.9,
                                bottom=.1,
                                top=.9)
        start += cols
        end += cols
    plt.show()