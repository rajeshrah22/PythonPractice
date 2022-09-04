def mysplit(strng):
    list = []
    i,j = 0,0
    while(i < len(strng)):
        while(i < len(strng) and strng[i].isspace()):
            i+=1
        if(i == len(strng)):
            break
        j = i 
        i += 1

        while(i < len(strng) and not(strng[i].isspace())):
            i += 1
        list.append(strng[j:i])
        if(j == 0 and i == len(strng)):
            break
    return list

print(mysplit("    To behhj or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
