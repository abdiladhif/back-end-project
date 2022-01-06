# handle = open("loremm.txt","r")
# data = handle.read()
# print(data)
# handle.close()







# wordd = open("loremm.txt","r")
# d = dict()
# for line in wordd :
#     line = line.strip()
#     line = line.lower()
#     words = line.split(" ")
#     for word in words:
#         if word in d :
#             d[word] = d[word] +1
#         else:
#             d[word] = 1
# for key in list(d.keys()):
#     print(key, ":", d[key])
#




# file = open("loremm.txt", "r")
# line_count = 0
# for line in file:
#     if line != "\n":
#         line_count += 1
# file.close()
#
# print(line_count)



def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('loremm.txt'))
