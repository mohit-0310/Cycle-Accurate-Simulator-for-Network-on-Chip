inputFile = open("input.txt", "r+")
# inputFile = inputFile.read()
list_of_instructions = []
# temp = ""
# for i in inputFile:
#     if i != '\n':
        
#         temp += i
#         # print(temp)
#     else:

#         list_of_instructions.append(temp)
#         temp=""

while True : 
    f = inputFile.readline() 
    if (len(f) == 0 ): 
        break 
    if(f[-1] == '\n') : 
        f1 = f[:-1]
    else : 
        f1 = f 
    list_of_instructions.append(f1) 


# print(list_of_instructions)

# for i in list_of_instructions:
#     print(i)
# print(list_of_instructions)