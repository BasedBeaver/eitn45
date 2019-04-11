from collections import Counter

str_alice = open('alice29.txt', 'r').read()


def char_frequency(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    dist = Counter(dict).most_common()
    return dist


print(char_frequency(str_alice))
