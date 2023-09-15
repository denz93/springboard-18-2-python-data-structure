def is_palindrome(phrase:str):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lower_phrase = phrase.lower().replace(" ", "")
    size = len(lower_phrase)
    idx = 0
    while idx < int(size / 2):
        if lower_phrase[idx] != lower_phrase[size - idx - 1]:
            return False
        idx += 1
    return True
    
