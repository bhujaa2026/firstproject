# ⭐ **1. Left-Aligned Triangle**


for i in range(1, 6):
    print("*" * i)

# ⭐ **2. Right-Aligned Triangle**

 
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)
 

# ⭐ **3. Inverted Left Triangle**

 
for i in range(5, 0, -1):
    print("*" * i)
 

# ⭐ **4. Inverted Right Triangle**

 
for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * i)


# ⭐ **5. Centered Pyramid**

 
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2*i - 1))
 

# ⭐ **6. Inverted Pyramid**

 
for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * (2*i - 1))
 

# ⭐ **7. Number Triangle**

 
for i in range(1, 6):
    print(str(i) * i)
 

# ⭐ **8. Increasing Number Pattern**

 
for i in range(1, 6):
    line = ""
    for j in range(1, i+1):
        line += str(j) + " "
    print(line)

# ⭐ **9. Alphabet Triangle (A, AB, ABC...)**

 
for i in range(1, 6):
    print("".join(chr(64 + j) for j in range(1, i+1)))


# ⭐ **10. Hollow Triangle**

 
for i in range(1, 6):
    if i == 1 or i == 5:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")
 

# 🎁 BONUS — Diamond Pattern

 
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
    
    
    
    # ✅ **1. Print 1 to 5**

 
i = 1
while i <= 5:
    print(i)
    i += 1
 

 
# ✅ **2. Print even numbers up to 10**

 
i = 2
while i <= 10:
    print(i)
    i += 2
 

 
# ✅ **3. Print characters of a string**

 
text = "hello"
i = 0

while i < len(text):
    print(text[i])
    i += 1
 

 
# ✅ **4. Sum of first 5 numbers**

 
i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print(total)
 

 
# ✅ **5. Traverse a list using while**

 
fruits = ["apple", "banana", "mango"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
 

 
# ✅ **6. Countdown from 5 to 1**

 
i = 5
while i > 0:
    print(i)
    i -= 1
 

 
# ✅ **7. Print multiplication table of 3 (3,6,9...)**

 
i = 1
while i <= 10:
    print(3 * i)
    i += 1
 

 
# ✅ **8. Reverse a string**

 
text = "python"
i = len(text) - 1

while i >= 0:
    print(text[i])
    i -= 1
 

 
# ✅ **9. Find first 5 multiples of 7**

 
i = 1
count = 0

while count < 5:
    print(7 * i)
    i += 1
    count += 1
 

 
# ✅ **10. Keep adding until sum reaches 20**

 
sum_val = 0
i = 1

while sum_val < 20:
    sum_val += i
    print(sum_val)
    i += 1