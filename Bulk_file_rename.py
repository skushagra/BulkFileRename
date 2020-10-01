import os
ph = input("Enter Path :- ")
files  = os.listdir(ph)
for i in range(len(files)):
	source = ph + files[i]
	desti = ph + str(i+1)
	os.rename(source,desti)

