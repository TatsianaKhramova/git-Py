def main():
    with open("text.txt", "r") as f:
        string = f.read()
    f.close()

    string = string.lower()
    data = [x for x in string if x.isalpha()]
    max_count = 0
    result = []
    for letter in set(data):
        counts = data.count(letter)
        result.append((letter, counts))
        if counts > max_count:
            max_count = counts

    print(sorted([letters for letters, counts in result if counts == max_count])[0],
          sorted([counts for letters, counts in result if counts == max_count])[0])

    print(string.count(' python'))
#
if __name__ == '__main__':
    main()
