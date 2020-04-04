"""
Main program to test the hash map program

Garrett Matthews

"""


from hashmap import HashMap


def clean_line(raw_line):
    """ removes all punctuation from input string and returns a list of all words which have a
    length greater than one """
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)):  # pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words


def main():
    """Runs the main program"""
    hash_map = HashMap()

    def count(key):
        """Function to return the value attached to the key given"""
        number = hash_map.get(key, 0)
        return number

    with open("AliceInWonderland.txt", 'r') as alice:
        for line in alice:
            words = clean_line(line)
            for i in words:
                hash_map.set(i, count(i) + 1)

    ranking = []
    position = 0
    while hash_map.lyst[position] is not None:
        ranking.append(hash_map.lyst[position])
        position += 1
    ranking.sort(key=lambda x: x[1], reverse=True)

    top_15 = []
    for i in range(15):
        top_15.append(ranking[i])

    print("The most common words are:")
    for i in top_15:
        if len(i[0]) >= 3:
            print(i[0], '\t', '\t', '\t', '\t', i[1])
        else:
            print(i[0], '\t', '\t', '\t', '\t', '\t', i[1])


if __name__ == '__main__':
    main()
