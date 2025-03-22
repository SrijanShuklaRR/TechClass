s=input()
s.lower()
vowels=['a','e','i','o','u']
for i in s:
    if i in vowels:
        print("vowel")
    else:
        print("consonant")

