
def mean(*args):
    """arithmetic mean, also known as the average of a sequence of numbers is the sum of the
        individual numeral divided by the number of values"""
    sumres = 0
    for x in args:
        sumres += x
    return sumres / len(args)




