string = input("Enter a string: ")
string = string.replace(" ", "").lower()
is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
