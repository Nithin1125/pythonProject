# \n is used for new line
# \t is ued for tab
# \b is used for backspace it will delete one character
print("hello\nworld")
print("hello\tworld")
print("hello\bworld")

#esacape sequence part 2

# if we give the path in directory  path if it contains \n  or \t then
# it will consider as "new line or tab" so python as given 'r' to reslove issue raw
dir = r'C:\nithin\n.txt'
dir1 = r'C:\nithin\t.txt'
print(dir)
print(dir1)

