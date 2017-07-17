import shutil
import string

shutil.copyfile("leicaraw.txt", "leicaontest.txt")
fr = open("leicaontest.txt", "r")
fw = open("leicaontest_temp.txt", "w")
content = fr.readlines()
i=0
#print(content)

#print(content[0].replace("*", "@"))

for line in range(len(content)):
	if i==0:
		newline = content[line].replace("*", "case ")
		fw.write(newline)
		i+=1
	elif i==1:
		newline = content[line].replace("*", "<=SN && SN<=")
		fw.write(newline)
		i+=1
	elif i==2:
		newline = content[line].replace("*", ": {type=\"")
		fw.write(newline)
		i+=1
	elif i==3:
		newline = content[line].replace("*", "\";year=\"")
		fw.write(newline)
		i+=1
	elif i==4:
		newline = content[line].replace("*", "\";pa=\"")
		fw.write(newline)
		i+=1
	elif i==5:
		newline = content[line].replace("*", "\";}")
		fw.write(newline)
		i=0
fr.close()
fw.close()
#	newline = content[line].replace("*", "@")
#	print(newline)
#	fw.write(newline)
#for line in f.readlines():
#	print(line)