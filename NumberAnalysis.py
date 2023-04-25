n = input()

count3 = 0
count_last = 0
count_even = 0
sum_five = 0
product_seven = 1

last_digit = n[len(n)-1]

for i in n:
    if i == '3':
        count3 += 1

for i in n:
    if i == last_digit:
        count_last += 1

for i in n:
     if int(i) % 2 == 0:
         count_even += 1

for i in n:
    if int(i) > 5:
        sum_five += int(i)

for i in n:
    if int(i) > 7:
         product_seven *= int(i)

print(count3)
print(count_last)
print(count_even)
print(sum_five)
print(product_seven)
