width = 19
height = int(input())

if height > 19 or height < 3:
    print("not valid input")
    quit()
    
print("*" * 19)
for i in range(height - 2):
    print("*", end='')
    for i in range(17):
         print(' ', end='')
    print("*")
         
     

print("*" * 19)
