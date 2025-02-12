def return_evens(sequence):
    """
    Returns a list of all even integers from the input sequence.
    """
    return [n for n in sequence if n % 2 == 0]

def make_exclamation(sentences):
    """
    Appends an exclamation mark to each string in the input list.
    """
    return [sentence + "!" for sentence in sentences]