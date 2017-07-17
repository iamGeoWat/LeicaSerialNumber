import shutil
import string

shutil.copyfile("leicaontest.txt", "leicaontest_temp.txt")
f = open("leicaontest_temp.txt", "r")
content = f.readlines()
print(content)
for lines in content:
	
#for line in f.readlines():
#	print(line)