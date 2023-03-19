" Тут будут решения задач с литкода(medium, hard) и кодварса(6-5-4 kuy)"

def alphabet_position(text):
    """
                          Codewars 6 kuy
                          Name : Replace With Alphabet Position
    In this kata you are required to, given a string, replace every letter with its position in the alphabet.
    If anything in the text isn't a letter, ignore it and don't return it.
    "a" = 1, "b" = 2, etc.
    :param text: string
    :return: string
    """

    alp = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alp.find(c) + 1) for c in text.lower() if c in alp])

