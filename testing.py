def print_diamond(n):
    letters = [chr(65 + i) for i in range(n)]

    for i in range(n):
        spaces = " " * (n - i - 1)
        print(spaces + "".join(letters[:i+1]))

    for i in range(n-2, -1, -1):
        spaces = " " * (n - i - 1)
        print(spaces + "".join(letters[:i+1]))

# Task 1
print_diamond(3)

# Task 2
print_diamond(5)

# Task 3

input  =  3
a = "_"
b = "A"
c = "B"
for i in range(input):
    if i == 0:print(f"{a}{b}{a}")
    if i == 1:print(f"{b} {c} ")
    if i == 2:print(f"{a}{b}{a}")
                
print('')

# Task 4
input  =  5
a = "_"
b = "A"
c = "B"
d = "C"
for i in range(input):
    if i == 0:print(f"{a}{a}{b}{a}{a}")
    if i == 1:print(f"{a}{b}{a}{c}{a}")
    if i == 2:print(f"{b}{a}{c}{a}{d}") 
    if i == 3:print(f"{a}{b}{a}{c}{a}")
    if i == 4:print(f"{a}{a}{b}{a}{a}")  
                 