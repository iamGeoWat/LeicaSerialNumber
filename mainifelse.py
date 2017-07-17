import shutil
import string

shutil.copyfile("leicaraw.txt", "leicaontest.txt")
fr = open("leicaontest.txt", "r")
fw = open("leicaontest_temp.txt", "w")
content = fr.readlines()
i=0
newline = ""

for line in range(len(content)):
	newline = content[line].replace("*", "else if (", 1).replace("*", "<=SN && SN<=", 1).replace("*", ") {type=\"", 1).replace("*", "\";year=\"", 1).replace("*", "\";pa=\"", 1).replace("*", "\";}", 1)
	print(newline)
	fw.write(newline)
fr.close()
fw.close()
