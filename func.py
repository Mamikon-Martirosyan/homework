# 1. Write a Python function to find the maximum of three numbers. 
# def x_y_max(x,y):
#     if x > y:
#         return x
#     else:
#         return y
# def x_y_z_max(x,y,z):
#     if z > x_y_max(x,y):
#         return z
#     else:
#         return x_y_max(x,y)
    
# print(x_y_z_max(9,6,1))    

# 2. Write a Python function to sum all the numbers in a list. 

# def my_sum(num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum  
# print(my_sum((4,5,1,10)))  

# 3. Write a Python function to multiply all the numbers in a list. 

# def my_multiply(num):  
#     multiply = 1
#     for i in num:
#         multiply *= i
#     return multiply
# print(my_multiply((2,4,2)))   


# 4. Write a Python program to reverse a string. 

# def str_reverse(mstr):
#     revStr = ""
#     index = len(mstr)
#     while index > 0:
#         revStr += mstr[index - 1]
#         index -= 1
#     return revStr
# print(str_reverse("hello"))   


# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 

# def fact(n):
#     fac = 1
#     if n == 0:
#         return 0
#     else:
#         for i in range(1,n +1):
#             fac *= i
#         return fac
# print(fact(4))   

# 6. Write a Python function to check whether a number falls within a given range. 

# def test_range(n):
#     if n in range(3,19):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(10)   

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters. 

# def str_test(mstr):
#     dic = {"Upper_Case":0, "Lower_Case":0}
#     for i in mstr:
#         if i.isupper():
#             dic["Upper_Case"]+=1
#         elif i.islower():
#             dic["Lower_Case"]+=1
#         else:
#             pass
#     print ("Original String : ", mstr)
#     print ("No. of Upper case characters : ", dic["Upper_Case"])
#     print ("No. of Lower case Characters : ", dic["Lower_Case"])    
# str_test('Hello')  

# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list. 


# def unique_list(l):
#     tmp = []
#     for i in l:
#         if i not in tmp:
#              tmp.append(i)
#     return tmp
# print(unique_list([1,1,2,2,3,3,3,]))   

# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not. 

# def prime_num(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 return False
#             return True
# prime_num(prime_num(11))   

# 10. Write a Python program to print the even numbers from a given list. 

# def even_numbers(ml):
#     even = []
#     for i in ml:
#         if i % 2 == 0:
#             even.append(i)
#     return even    
# print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))     

# 11. Write a Python function to check whether a number is "Perfect" or not.

# def perfect_num(n):
#     msum = 0
#     multiple = 1
#     for i in range(1,n):
#         if n % i == 0:
#             msum += i
#             multiple *= i
#     return msum == n == multiple  
# print(perfect_num(6))          
                 
# 12. Write a Python function that checks whether a passed string is a palindrome or not. 

# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('mad'))


# def isPalindrom(mstr):
#     return mstr == mstr[::-1]
# print(isPalindrom("qaxaq"))
    
        
# 13. Write a Python function that prints out the first n rows of Pascal's triangle.        

# n = int(input("Enter the number of rows:"))   
# for i in range(n):  
#     print(' '*(n-i), end='')    
#     print(' '.join(map(str, str(11**i))))  

# 14. Write a Python function to check whether a string is a pangram or not. 

# def pangram_check(str): 
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for char in alphabet: 
#         if char not in str.lower(): 
#             return False
  
#     return True
      
# def main():
#     str = 'The quick brown fox jumps over the lazy dog'
#     if(pangram_check(str) == True): 
#         print("Yes") 
#     else: 
#         print("No")
# main() 

# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
     
# def hyphen_separated(mstr):
#     lst=[n for n in mstr.split('-')]  
#     lst.sort()
#     return ('-'.join(lst))
# print(hyphen_separated("d-a-b-c"))    
      
# 1. Գրել ֆունկցիա, որը կվերդարձնի ստացած արգումենտներից թվերի գումարը։

# def mysum(*ml):
#     sum = 0
#     for i in ml:
#         if str(i).isdigit():
#             sum += i
#     return sum  
# print(mysum(1,2,5))       
        

# 2. Գրել ֆունկցիա, որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։

# def count_lines(text):
#     num_lines = 0
#     for line in text.splitlines():
#         num_lines += 1
#     return num_lines

# text = "This is a string \n with multiple \n lines."
# print(text)
# print("The number of lines in the string is: ",count_lines(text))  
        
# 3. Գրել ֆունկցիա, որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։

# def arithmetic_mean(numbers):
#   sum_of_numbers = 0
#   for number in numbers:
#     sum_of_numbers += number
#   return sum_of_numbers / len(numbers)

# numbers = [1,2,5,10,7]
# print(arithmetic_mean(numbers))
# 4. Գրել ֆունկցիա, որը կստանա 2 արգումենտ և կվերադարձնի այդ
# արգումենտերի հետ կատարած մաթեմատիկական գործողությունների արդյունքները։

# def mathematical_operations(x, y):
#     results = {}
#     results["addition"] = x + y
#     results["subtraction"] = x - y
#     results["multiplication"] = x * y
#     results["division"] = x / y
#     results["remainder"] = x % y
#     return results
# print(mathematical_operations(5,2))  
# 5. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ մեծատառ (upper ֆունկցիան օգտագործել չի կարելի)։
# def to_uppercase(string):
#   uppercase_letters = ""
#   for character in string:
#     if character.islower():
#       uppercase_letter = chr(ord(character) - 32)
#     else:
#       uppercase_letter = character
#     uppercase_letters += uppercase_letter

#   return uppercase_letters
# string = "hello world"
# print(to_uppercase((string)))


# 6. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ փոքրատառ (lower ֆունկցիան օգտագործել չի կարելի)։

# def to_lowercase(string):
#   lowercase_letters = ""
#   for character in string:
#     if character.isupper():
#       lowercase_letter = chr(ord(character) + 32)
#     else:
#       lowercase_letter = character
#     lowercase_letters += lowercase_letter

#   return lowercase_letters
# print(to_lowercase("HELLO World"))


# 7. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված բոլոր բառերի առաջին տառերը մեծատառ (title ֆունկցիան օգտագործել չի կարելի)։


# def first_letters_uppercase(string):
#    words = string.split(" ")
#    uppercase_words = []
#    for word in words:
#       first_letter = word[0].upper()
#       remaining_letters = word[1:]
#       uppercase_word = first_letter + remaining_letters
#       uppercase_words.append(uppercase_word)

#    return " ".join(uppercase_words)
# print(first_letters_uppercase("hell world")) 


# 8. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված հակառակ։

# def reverse_string(string):
#    reversed_string = ""
#    for character in string[::-1]:
#       reversed_string += character

#    return reversed_string
# print(reverse_string("hello world")) 


# 9. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տող և 2 թիվ։ Այն պետք է
# վերադարձնի տրված 2 թվերի արանքում եղած ենթատողը։

# def substring_between_numbers(string, start_number, end_number):
   
#    start_index = string.find(str(start_number))
#    end_index = string.find(str(end_number))
#    if start_index == -1 or end_index == -1:
#       return ""
#    substring = string[start_index + len(str(start_number)):end_index]
#    return substring
# string = "The quick brown fox jumps over the lazy dog" 
# print(substring_between_numbers(string,2,4)) 

# 10. Գրել ֆունկցիա, որը կվերադարձնի նախադասության ամենաերկար բառը։

# def longest_word(sentence):
#   words = sentence.split(" ")
#   longest_word = ""
#   for word in words:
#     if len(word) > len(longest_word):
#       longest_word = word

#   return longest_word
# sentence = "The quick brown fox jumps over the lazy dog"
# print(longest_word(sentence))


# 11. Գրել ֆունկցիա, որը կվերադարձնի նախադասության ամենաշատ օգտագործված տառը։

# def most_used_letter(sentence):
#   letter_counts = {}
#   for letter in sentence:
#     if letter not in letter_counts:
#       letter_counts[letter] = 0
#     letter_counts[letter] += 1

#   most_used_letter = ""
#   max_count = 0
#   for letter, count in letter_counts.items():
#     if count > max_count:
#       max_count = count
#       most_used_letter = letter

#   return most_used_letter
# print(most_used_letter("hello"))

# 12. Գրել ֆունկցիա, որը կվերադարձնի նախադասության ամենաերկար
# բառում ամենաշատ օգտագործված տառը։

# def most_frequently_used_letter_in_longest_word(mstr):
#   words = mstr.split(" ")
#   longest_word = ""
#   for word in words:
#     if len(word) > len(longest_word):
#       longest_word = word

#   letter_counts = {}
#   for letter in longest_word:
#     if letter not in letter_counts:
#       letter_counts[letter] = 0
#     letter_counts[letter] += 1

#   most_used_letter = ""
#   max_count = 0
#   for letter, count in letter_counts.items():
#     if count > max_count:
#       max_count = count
#       most_used_letter = letter

#   return most_used_letter
# print(most_frequently_used_letter_in_longest_word("hello worldd"))


# 13. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տող և թիվ։
# Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝
# սկզբից և վերջից։

# def elements_at_index(string, number):
#   elements = []
#   for i in range(number):
#     elements.append(string[i])
#   for i in range(len(string) - number, len(string)):
#     elements.append(string[i])

#   return elements
# string = "The quick brown fox jumps over the lazy dog"
# number = 5
# print(elements_at_index(string,number))

# 15․ Գրել ֆունկցիա, որը որպես արգումենտ կստանա թիվ և կստուգի
# պոլինդրոմ է այն, թե ոչ։

 


# 16․ Գրել ֆունկցիա, որը որպես արգումենտ կստանա թիվ և կվերադարձնի
# իրեն ամենամոտ պոլինդրոմ թիվը։


# 17․ Գրել ֆունկցիա, որը որպես արգումենտ կստանա թիվ և կվերադարձնի իր
# առաջին և վերջին թվանշանների արտադրյալը։


# def product_of_first_and_last_digits(number):

#   number_string = str(number)
#   first_digit = number_string[0]
#   last_digit = number_string[-1]

#   product = int(first_digit) * int(last_digit)

#   return product
# print(product_of_first_and_last_digits(2547))



# 18. Գրել ֆունկցիա, որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում եղած տողերի քանակությունը։

# def number_of_rows(list_of_rows):

#   number_of_rows = 0
#   for row in list_of_rows:
#       number_of_rows += 1
#   return number_of_rows
# list_of_rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(number_of_rows(list_of_rows))


# 19․ Գրել ֆունկցիա, որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա թվերից առավելագույնը։

# def maximum_number(list):
#     maximum_number = 0
#     for number in list:
#       if  number > maximum_number:
#           maximum_number = number

#     return maximum_number
# list = [1, 2, 3, 12, 5, 6, 7, 8, 9] 
# print(maximum_number(list)) 


# 20․ Գրել ֆունկցիա, որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# այդ լիստում առկա երկնիշ զույգ թվերը։

# def digit_even_numbers(list):

#     even_numbers = []
#     for number in list:
#         if number >= 10 and number <= 99 and number % 2 == 0:
#             even_numbers.append(number)

#     return even_numbers
# list = [1, 2, 3, 12, 5, 6, 7,24, 8, 9] 
# print(digit_even_numbers(list))   


# 21 Գրել ֆունկցիա, որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# այդ լիստում առկա թվերի միջին թվաբանականը։

# def arithmetic_mean(list_of_numbers):
#     sum_of_numbers = 0
#     number_of_numbers = len(list_of_numbers)
#     for number in list_of_numbers:
#         sum_of_numbers += number
#     arithmetic_mean = sum_of_numbers / number_of_numbers
#     return arithmetic_mean
# list_of_numbers = [1, 2, 3, 12, 5, 6, 7,24, 8, 9]
# print(arithmetic_mean(list_of_numbers))


# 22. Գրել ֆունկցիա, որը որպես առգումենտ կստանա տողերի լիստ և
# կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ։

# def lengths_of_strings(list_of_strings):

#     lengths_of_strings = []
#     for string in list_of_strings:
#         lengths_of_strings.append(len(string))

#     return lengths_of_strings

# list_of_strings = ["hello", "world", "this", "is", "a", "list"]
# print(lengths_of_strings(list_of_strings))


# 23. Գրել ֆունկցիա, որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա թվերը դասավորված նվազման կարգով։      
              
def descending_order(list_of_numbers):
    sorted_list_of_numbers = sorted(list_of_numbers, reverse=True)
    return sorted_list_of_numbers              
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(descending_order(list_of_numbers))