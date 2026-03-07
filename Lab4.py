def last_digit(n):
    d=n%10
    return d

def sum_digits(n):
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    return sum

def middle(a,b,c):
    mi=min(a,b,c)
    ma=max(a,b,c)
    return a+b+c-mi-ma

def nod(a,b):
    while b:
        a,b=b,a%b
    return a

def even(n):
  return (n % 2 == 0)

n=int(input("Enter a number: "))
print(last_digit(n))
print(sum_digits(n))
print(middle(7,4,9))
print(nod(12,16))
print(even(56))