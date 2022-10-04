def anagramChecker(input1, input2):
    set1 = set(())
    set2 = set(())
    for ch in input1.upper():
        if ch == " ":
            continue
        set1.add(ch)
    for ch in input2.upper():
        if ch == " ":
            continue
        set2.add(ch)
    if set1 == "" or set2 == "":
        return False
    if set1 == set2:
        return True
    else:
        return False
        
input1 = input("first string: ")
input2 = input("second string: ")

if anagramChecker(input1, input2):
    print("Anagrams")
else:
    print("Not anagrams")