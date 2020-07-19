
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Args:
        string (str): The encoded string
        alphabet (str): The alphabet to use for encoding

    Returns:
        num: The Decoded string
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num