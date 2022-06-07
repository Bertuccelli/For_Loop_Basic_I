# Basics
for x in range(0, 151):
    print(x)
# Multiples of Five
for x in range(5, 1001, 5):
    print(x)
# Counting, the Dojo Way
for x in range(1, 101):
    if x%5 == 0 and x%10 !=0:
        print("Coding")
    elif x%10 == 0:
        print("Coding Dojo")
    else: print(x)
# Whoa. That Sucker's Huge
final_sum = 0
for x in range(0, 500001):
    if x%2 != 0:
        final_sum += x
print(final_sum)
# Countdown by Fours
for x in range(2018, 0, -4):
    print(x)
# Flexible Counter
low_num = 2
high_num = 9
mult = 3
for x in range(low_num, high_num+1):
    if x%mult == 0:
        print(x)