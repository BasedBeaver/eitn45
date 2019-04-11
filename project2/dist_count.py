# Ugly code but easy to understand i think!

str_alice = open('alice29.txt', 'rb').read()  # Read in file.txt bytewise.


# Create a dict with every unique char found as a new key and value as occurrence.
def char_frequency(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


# Help method to change the representation of keys (int) to their char value according to ASCII
# as well as print the results.
def print_dist(dict):
    res = []
    for key, value in dict.items():
        res.append((chr(key), value))
    res.sort(key=lambda tup: tup[1], reverse=True)

    print(len(dict))  # Found 74 as according to project description.
    print(sum(dict.values()), res)  # 152 089 chars/bytes found, 'e' = 13381 as according to project description.


dict = char_frequency(str_alice)
print_dist(dict)

