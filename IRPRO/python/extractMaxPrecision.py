import sys
filename = sys.argv[1]
f = open(filename,'r')
maxi = 0
for line in f:
	if (line.split(" "))[0]=="Macro-average":
		value = line.split(" ")[-1]
		value = value.replace("(","")
		value = value.replace(")","")
		value = value.replace("\n","")
		# value = value.replace("\'","")
		
		# value = value.replace("'","")
		value = value.split(",")[-1]
		value = value[2:]
		# print len(value)

		f1 = int(value)
		if f1>maxi:
			maxi = f1
print maxi			