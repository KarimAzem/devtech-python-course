# Create a number guesser program 
# 1 - the user has 5 chance to guess the number 
# 2 - the number is random but can be set
# 3 - the number is in range(100)


# ! solution

from random import randint



def number_guesser(number, chances):
    
    print('#### number guesser ####\n')
    
    

    while chances >= 0:
        print(f"{chances} left ! ")
        answer = input("try to geuss the hidden number\n(is between 0 and 50) :")
        
        if answer == '':
            print("barka ma tejya7 jaweb")
            continue
            
        if int(answer) == number:
            print(f"\nyou won!! the number was {number}")
            break            
        
        elif int(answer) < number:
            print('\nthe number is higher than your answer')
        
        elif int(answer) > number:
            print('\nthe number is lower than your answer')
            
       
                
        if chances == 0 :
            print("\nno more chances you lost")
            
        chances -= 1

# ? for method 

def number_guesser_for(number, chances):

    print('#### number guesser ####\n')

    for i in range(chances+1) :
        
        if  i == chances:
            print("\nno more chances you lost")
            break
        
        answer = int(
            input("try to geuss the hidden number\n(is between 0 and 50) :")+"\n")

        if answer == number:
            print(f"\nyou won!! the number was {number}")
            break        
            
        elif answer < number:
            print('\nthe number is higher than your answer')

        elif answer > number:
            print('\nthe number is lower than your answer') 

        

        




number_guesser(randint(0, 50), 5)    
    
    
    
    
    
    