#finds a word hidden within another word. Example: donor exists within
  #nabucodonosor because d, o, n, o and r are found in the second word in that order. So it will return true.


def findAWord(first, second):
    found = True
    previousPos = 0
    for ch in first:
        currentPos = second.find(ch, previousPos)
        if currentPos == -1:
            found = False
            break
        else:
            previousPos = currentPos
    return found 
first = input()
second = input()
if(findAWord(first, second)):
    print("Yes")
else:
    print("No")