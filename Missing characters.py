import os

def missingCharacters(s):
    l = [0] * 123
    result = ""

    for ch in s:
        l[ord(ch)] += 1

    for i in range(48, 58):   # digits 0–9
        if l[i] == 0:
            result += chr(i)

    for i in range(97, 123):  # letters a–z
        if l[i] == 0:
            result += chr(i)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = missingCharacters(s)

    fptr.write(result + '\n')
    fptr.close()
