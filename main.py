a = float(input())
b = float(input())
c = float(input())

if a+b>=c and a+c>=b and b+c>+a:
    print("to jest trojkat")   
    if a**2 + b**2 == c**2 or c**2 + a**2 == b**2 or c**2 + b**2 == a**2:
        print("to jest trojkat prostokatny")
    elif a==b==c:
        print("to jest trojkat rownoboczny")
    else:
        print("to jest trojkat rownoramienny")
else:
    print("to nie jest trojkat")