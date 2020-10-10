'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # empty string
    if word == "":
        return 0
    # check if the first letters are th
    elif word[0:2] == 'th':
    # recurse after th
        return 1 + count_th(word[2:])
    else:
    # recurse after non th
        return count_th(word[1:])