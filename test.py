
# def palindrome(s):
    # return s == s[::-1]

# if __name__=='__main__':
    # s = input('enter the string: ')
    # if palindrome(s):
        # print('it is!')
    # else:
        # print('no!')
          
          
def apple(a):
    return a**a
    
list1 = [1,2,3,4]
print(list(map(apple,list1)))