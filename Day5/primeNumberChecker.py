#Write your code below this line ๐
def prime_checker(number):
    is_Prime = True
    for i in range(2, number // 2):
        if number % i == 0:
            is_Prime = False
            print("It's not a prime number.")
            break
    if is_Prime:
        print("It's a prime number.")

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
