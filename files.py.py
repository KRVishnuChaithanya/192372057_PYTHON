file_path = input("Enter the file path: ") 
strings_list = ["Hello", "World", "Python", "Programming"] 
with open("pali.py", 'w') as file: 
 for string in strings_list:
     file.write(string + "\n") 
print("List of strings has been written to the file successfully!")
file_path = input("Enter the file path: ") 
with open("tuple.py", 'r') as file: 
 line_count = 0 
 for line in file:
     line_count += 1 
print("Number of lines in the file:", line_count)
file_path = input("Enter the file path: ") 
with open("tuple.py", 'r') as file: 
 word_count = 0 
 for line in file:
     words = line.split()  
 word_count += len(words) 
print("Number of words in the file:", word_count)
file_path = input("Enter the file path: ") 
with open("pali.py", 'r') as file: 
 char_count = 0 
 for line in file:
     char_count += len(line)
 print("Number of characters in the file:", char_count)
 source_file_path = input("Enter the source file path: ") 
destination_file_path = input("Enter the destination file path: ") 
with open("pali.py", 'r') as source_file: 
 with open("pali.py", 'w') as destination_file:
     for line in source_file:
         destination_file.write(line) 
print("File copied successfully!")
file_path = input("Enter the file path: ") 
strings_list = ["Hello", "World", "Python", "Programming"] 
with open("pali.py", 'w') as file: 
 for string in strings_list:
     file.write(string + "\n") 
print("List of strings has been written to the file successfully!")
