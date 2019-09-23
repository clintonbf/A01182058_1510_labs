#Circumstance A: each statement is its own program
#Circumstance B: all statements are included in one program
x = 1          #valid in A and B
x = y          #invalid in A and B: y has not been defined
x = y + 2      #invalid in A and B: y has not been defined
x + 1 = 3      #invalid in A and B: you can't do assignments like this (ie. this isn't a statement)
x + y = y + x  #invalid in A & B: y undefined and you can't do assignments like this (ie. this isn't a statement)