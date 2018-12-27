def unpickle(file):
    """
    Open the file and create a dictionary

    :param file: file path name 
    :type  file: str
    :return: Dictionary of the file
    :rtype:  dict
    """

    import pickle

    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def decode_list(meta, b_key):
    """
    Decode items in a list.

    :param meta: a dictionary of type of label (superclass or class) as key 
                 and list of labels as the value
    :type  meta: dict
    :param b_key: string of a key in bytes
    :type  b_key: bytes
    :return: list of decoded items
    :rtype:  list
    """

    to_utf = [item.decode("utf-8") for item in meta[b_key]]
    return to_utf