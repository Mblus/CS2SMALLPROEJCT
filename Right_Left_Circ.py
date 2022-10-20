def leftCirc(data1, start1):
    string = data1[start1:] + data1[0:start1]
    return string


def rightCirc(data1, start1, length1):
    string2 = data1[-start1:] + data1[:(length1 - start1 + 1)]
    return string2


data1 = input(str("give word"))
start1 = input('give number')
length1 = (len(data1) - 1)
start1 = int(start1)
string = leftCirc(data1, start1)
string2 = rightCirc(data1, start1, length1)
print(string)
print(string2)
