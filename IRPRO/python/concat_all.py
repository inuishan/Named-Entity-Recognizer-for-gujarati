from os import listdir
from os.path import isfile, join
mypath='../New_crfsuiteText_3Tags/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
file_name = "vipul_model_names_inc.txt"
f = open(file_name,"w")
for i in range(len(onlyfiles)):
	fd = open(mypath+onlyfiles[i],'r')
	for line in fd:
		f.write(line)
# f.close()

# f = open(file_name+2,"w")
# f2 = open(file_name,"r")
# for line in 		
