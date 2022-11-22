import csv 

#create a contacts folder in this directory and add the csv file with your filename 

input=list(csv.reader(open('contacts/13.11.22.csv','r'))) 
output=open('vcf/con_13.11.22.vcf','w') 
for row in input: 
	output.write("BEGIN:VCARD\n") 
	output.write("VERSION:3.0\n")
	output.write("FN:"+row[0]+'.'+row[1]+'.NECF '+ row[2]+"\n") 
	output.write("N:"+"NECF "+row[2]+";"+row[0]+'.'+row[1]+";;;\n") 
	output.write("TEL;TYPE=CELL:"+row[3]+"\n")
	output.write("CATEGORIES:"+'Imported on 30/10,myContacts'+"\n") 
	output.write("END:VCARD\n") 
output.close()


#use google doc to convert the googledoc/excel table to csv
