#simple methode 
# a=input("enter your string")
# b=a[::-1]

# if a==b:
#     print("palindrom")
# else:
#     print("not")


#without using any slising 

# a=input("enetr your word:")
# reverse=""

# for char in a:
#     reverse=char+reverse
# if a==reverse:
#     print("palindrom")
# else:
#     print("not palindrom")


# def is_palindrom(text):
#     reverse_text=""

#     for char in text:
#         reverse_text=char+reverse_text

#     return text==reverse_text


# word=input("enter your word")
# if is_palindrom(word):
#     print("yes")
# else:
#     print("no")


# with interger value
def is_palindrom(n):
    n_str=str(n)
    reverse_str=""
    
    for ch in n_str:
        reverse_str=ch+reverse_str
    return n_str==reverse_str

num=(input("enter your number"))

if is_palindrom(num):
    print("yes")
else:
    print("no")