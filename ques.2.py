while input() != 'h':
    num=input("ENTER THE ALPABETS:")
    r=num[::-1]
    if r == num:
        print("It is a Palindrome String")
    else:
        print("It is not a Palindrome String")