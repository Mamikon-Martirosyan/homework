

def longest_rightmost_sequence(list):
    
    longest_sequence = []
    current_sequence = []

    for i in range(len(list)):
         if len(current_sequence) == 0 or list[i] >= current_sequence[-1]:
             current_sequence.append(list[i])
         else:
             if len(current_sequence) > len(longest_sequence):
                 longest_sequence = current_sequence
                 current_sequence = [list[i]]

    if len(current_sequence) > len(longest_sequence):
         longest_sequence = current_sequence

    return longest_sequence

def check_brackets_correctness(input_str):
    stack = []
    
    for char in input_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    return len(stack) == 0 and '()' not in input_str 
def main():
    listStr = input("Enter alist: ").split(',')
    numbers = [int(num) for num in listStr if num.strip()]
    print(longest_rightmost_sequence(numbers))
    input_str = input("Enter : ")
    print(check_brackets_correctness(input_str))
main()

