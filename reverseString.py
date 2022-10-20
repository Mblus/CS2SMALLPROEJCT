def reverseString(data1, length1, start1):
    temp_list = list(data1[(start1-1):(start1+(length1-1))])
    temp_list.reverse()
    final = ((data1[:(start1-1)]) + ''.join(temp_list) + (data1[(start1 + length1-1):]))
    return final

data1 = input(str("give word"))
start1 = input('give number')
length1 = input('give length')
start1 = int(start1)
length1 = int(length1)
final = reverseString(data1, length1, start1)

print(final)