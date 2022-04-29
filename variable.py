# variables file

number = 5  #* integer
text = 'j'  #* String
fnumber = 5.1   #* float
complex_number = 1+5j #? j² = -1
logic = True    #* boolean

#* multi word variable

# snacke case
multi_word_variable = None

# Cammel Case
multiWordVariable = None

# pascal case
MultiWordVariable = None

#! Variable are case sensitive word != Word

# * declare multi var's per line with same value
test = test2 = 5

test = 4
test3 = 6

# print variables
print(test)
print(test3)


print(
    f"""
    {type(number)}
    {type(text)}
    {type(fnumber)}
    {type(logic)}
    {multi_word_variable}
    """
)


#! exe:
# ? switch the value of two variable

a, b = 1, 2
b,a = a, b

print(a ,b )
