import os
ph = input("Enter Path :- ")
files  = os.listdir(ph)
for i in range(0,len(files)):
	source = ph + files[i]
	desti = ph + str(i)
	os.rename(source,desti)

