#/usr/local/bin/python3

passfile = "4.passphrases.txt"

def countDupes(line):
    line = line.strip().split(" ")
    for i, word in enumerate(line):
        if line.count(word) > 1:
            return False
    return True

def countDupes2(line):
    line = line.strip().split(" ")
    words = []
    for _, word in enumerate(line):
        words.append(''.join(sorted(word)))
    for _, word in enumerate(words):
        if words.count(word) > 1:
            return False
    return True

if __name__ == '__main__':
    count = 0
    count2 = 0
    with open(passfile) as file:
        for line in file:
            if countDupes(line):
                count += 1
            if countDupes2(line):
                count2 += 1

    print("Valid phassphrases: {}\t{}".format(count, count2))