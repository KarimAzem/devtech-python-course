""" The "for" statement is used to iterate over the elements of a sequence
(such as a string, tuple or list) or other iterable object:

   for_stmt: := "for" target_list "in" expression_list ":" suite
   ["else" ":" suite] """
 
for i in range(0):
   # print('hi')
   pass


""" The "while" statement is used for repeated execution as long as an
expression is true:

   while_stmt: := "while" assignment_expression ":" suite
   ["else" ":" suite] """


i = 0 
while i <= 10 :
    i+=1
    #print(i)time to go
    break
else:
   print("while loop can use else statement")
#! break stop the loop 

    
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
else:
   print("while loop can use else statement") 
#! continue cancel the current step and go to the next
  

