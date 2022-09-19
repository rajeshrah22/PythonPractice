#prints out seven segment display number

digits = ["""###
# #
# #
# #
###""",

"""  #
  #
  #
  #
  #""", """###
  #
###
#  
###""","""###
  #
###
  #
###""",
"""# #
# #
###
  #
  #""",
"""###
#  
###
  #
###""",
"""###
#  
###
# #
###""",
"""###
  #
  #
  #
  #""",
"""###
# #
###
# #
###""",
"""###
# #
###
  #
  #"""
]

numIn = int(input())
numList = []
while numIn > 0:
    numList.insert(0,numIn % 10)
    numIn//=10

for k in range(0,17,4):
  for num in numList:
    print(digits[num][0+k] + digits[num][1+k] + digits[num][2+k] , end = " " )
  print("")

    
