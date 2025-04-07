var = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in var:
#     summary = 0
#     for element in i:
#         summary = summary + element
    
#     print(summary)

#deyteros tropos na diaperasoume th lista poy apoteleitai apo listes , me deiktkes sth loypa.

# for i in range(len(var)):
#     current = var[i]
#     for j in range(len(current)):
#         print(var[i][j], end="")
#     print()



#SETS

# #metatropi listas se set.... Ta set den periexoun diplotipta + exoyn tomh kai enwsh
# l = [12, 3, 5432, 654, 3]

# aset = set(l)

# print(aset)



#Dictionaries

# d = {"a":1, "b":2, "c":3}

# for i in d.keys():
#     print(d[i])


#askisi diafaneiwn

# #1 ME DEIKTES
# accounts = [[1,5], [7,3], [3,5]]

# sum = 0
# cus = 0
# for i in range(len(accounts)):
#     current = accounts[i]
#     sum2 = 0
#     for j in current:
#         sum2 = sum2 + j
#         if sum2>sum:
#             sum = sum2
#             cus = i

# print("O ", cus+1, "pelatis einai o pio plousios me plouto ", sum , "eurw")

# #2 ME STOIXEIA
# accounts = [[1,5], [7,3], [3,5]]

# count = -1
# maximum = -1
# for i in accounts:
#     p = 0
#     count = count + 1
#     for j in i:
#         p = p + j
#         if p > maximum:
#             maximum = p
#             max_count = count

# print(maximum, max_count + 1)


#ASKHSH 2
# l1 = [1, 4, 6, 7, 2]
# l2 = [5, 10, 7, 2, 1]
# l3 = []
# for i in l1:
#     for j in l2:
#         if i == j:
#             l3.append(i)

# l3.sort()
# print(l3)

# #ginetai kai me synola

# l1 = set(l1)
# l2 = set(l2)

# l3 = l1 & l2
# l3 = list(l3)
# l3.sort
# print(l3)



#ASKHSH 3

s = "52C3DC"

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
score = 0
add1 = 0
for i in range(len(s)):
    if s[i] in nums:
        x = int(s[i])
        score += x
        add1 = x
    elif s[i] == "C":
        score -= add1
    elif s[i] == "D":
        add1 = score
        score *= 2

print(score)

#askhsh 4 den prolavainoume alla tha ginei me dictionary 
#pairnoume kathe arithmo ths listas kai vlepoume an se kathe kleidi tou dictionary yparxei aytos o arithmos. 
#Dhladh to kleidi tha einai o arithmos kai h timh tou poses fores emfanizetai