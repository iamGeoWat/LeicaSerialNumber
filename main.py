import shutil
import string

shutil.copyfile("leicaraw.txt", "leicaontest.txt")
fr = open("leicaontest.txt", "r")
fw = open("leicaontest_temp.txt", "w")
content = fr.readlines()
i=0
newline = ""
#print(content)

#print(content[0].replace("*", "@"))

for line in range(len(content)):
	newline = content[line].replace("*", "case ", 1).replace("*", "<=SN && SN<=", 1).replace("*", ": {type=\"", 1).replace("*", "\";year=\"", 1).replace("*", "\";pa=\"", 1).replace("*", "\";}", 1)
	print(newline)
	fw.write(newline)
		
#	if i==0:
#		newline = content[line].replace("*", "case ")
#		print(newline)
#		fw.write(newline)
#		i+=1
#	elif i==1:
#		newline = content[line].replace("*", "<=SN && SN<=")
#		print(newline)
#		fw.write(newline)
#		i+=1
#	elif i==2:
#		newline = content[line].replace("*", ": {type=\"")
#		print(newline)
#		fw.write(newline)
#		i+=1
#	elif i==3:
#		newline = content[line].replace("*", "\";year=\"")
#		print(newline)
#		fw.write(newline)
#		i+=1
#	elif i==4:
#		newline = content[line].replace("*", "\";pa=\"")
#		print(newline)
#		fw.write(newline)
#		i+=1
#	elif i==5:
#		newline = content[line].replace("*", "\";}")
#		print(newline)
#		fw.write(newline)
#		i=0
fr.close()
fw.close()
#	newline = content[line].replace("*", "@")
#	print(newline)
#	fw.write(newline)
#for line in f.readlines():
#	print(line)