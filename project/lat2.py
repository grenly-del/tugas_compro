import re

# ===== REVERSE STRING =====
string = "Grantly Sorongan"
reverse = string[::-1]
print(reverse)
print("================ Grantly Sorongan ==================")

# ===== PALINDROME STRING =====
string1 = "malam"
plin = string1[::-1]
if string1 == plin:
    print('Palindrome')
else: 
    print("Is Not Palindrome")
print("================ Grantly Sorongan ==================")

# ====== LENGTH STRING ======
string2 = "Hello, World!"
count = len(string2)
print(count)
print("================ Grantly Sorongan ==================")

# ====== ANAGRAMS STRING =======
string3 = "listen"
string4 = "silent"
sorted_string3 = sorted(string3)
sorted_string4 = sorted(string4)
if sorted_string3 == sorted_string4:
 print("Anagrams")
else:
 print("Not anagrams")
print("================ Grantly Sorongan ==================")


# ========= LOWERCASE STRING ==========
string5 = "Hello, World!"
lowercase_string5 = string5.lower()
print(lowercase_string5)
print("================ Grantly Sorongan ==================")


# ============ REPLACE STRING ============
string6 = " Hello, World! "
trimmed_string6 = string6.replace(" ", "")
print(trimmed_string6)
print("================ Grantly Sorongan ==================")

# =========== LONGEST WORD STRING =============
sentence = "Python is a versatile programming language"
words = sentence.split()
longest_word = max(words, key=len)
print(longest_word)
print("================ Grantly Sorongan ==================")

# ========== COUNT STRING ============
string7 = "Hello, World!"
character = "W"
count1 = string7.count(character)
print(count1)
print("================ Grantly Sorongan ==================")

# =========== CAPITAL STRING ============

sentence1 = "python programming is fun"
capitalized_sentence1 = sentence1.title()
print(capitalized_sentence1)
print("================ Grantly Sorongan ==================")


# =========== REPLACE STRING ============
string8 = "Hello, World!"
character2 = "o"
replacement = "a"
new_string8 = string8.replace(character2, replacement)
print(new_string8)
print("================ Grantly Sorongan ==================")

# ========= CONTAINS ONLY DIGITS STRING ===========
string9 = "12345"
if string9.isdigit():
 print("Contains only digits")
else:
 print("Does not contain only digits")
print("================ Grantly Sorongan ==================")

# =========== CHECK STARS CHARACTER STRING ============
string10 = "Hello, World!"
character3 = "e"
if string10.startswith(character3):
 print("Starts with", character3)
else:
 print("Does not start with", character3)
print("================ Grantly Sorongan ==================")

# =========== CHECK STARS CHARACTER STRING ============
string11 = "Hello, World!"
character4 = "d"
if string11.endswith(character4):
    print("Ends with", character4)
else:
    print("Does not end with", character4)
print("================ Grantly Sorongan ==================")

# ============ CHECH IMAIL VALID ==================
email = "john.doe@example.com"
pattern = r"[^@]+@[^@]+\.[^@]+"
if re.match(pattern, email):
 print("Valid email address")
else:
 print("Invalid email address")
print("================ Grantly Sorongan ==================")

# ============ DUPLIKAT REMOVE STRING ============
string12 = "Hello, World!"
unique_characters = "".join(set(string12))
print(unique_characters)
print("================ Grantly Sorongan ==================")

# ============== STRING =============
string13 = "Hello, World!"
sorted_string13 = "".join(sorted(string13))
print(sorted_string13)
print("================ Grantly Sorongan ==================")

# =============== STRING =============
sentence5 = "Python programming is fun"
words2 = sentence5.split()
count5 = len(words)
print(count5)
print("================ Grantly Sorongan ==================")


# ============= STRING =================
string14 = "Hello, World!"
character5 = "o"
index = string14.index(character5)
print(index)
print("================ Grantly Sorongan ==================")

# ============= STRING =================
string15 = "Python programming is fun"
words6 = string15.split()
print(words6)
print("================ Grantly Sorongan ==================")

# ================ STRING ===================
name = "Grantly Sorongan"
age = 25
formatted_string = "My name is {} and I am {} years old".format(name, age)
print(formatted_string)
print("================ Grantly Sorongan ==================")
