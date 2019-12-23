import sys
import openpyxl

excelFile = "17_ug_19EXJob-3.xlsx"
count = 0;
multiLine = "";
multiGrant = ""
multiFlag = 0;
slNo = 0 ; givName=0 ;strtAddress = 0 ; city=0
state =0 ;zipCode = 0;postalCode=0;emlAdrs = 0
prncplInvestgtr = 0 ;cirn = 0;birthday=0
ccnum = 0 ;ccexp = 0 ;ntnlId=0;occupsn = 0
organsn =0;vhcl = 0;grntNum=0;grntTitle=0
nih=0
row = {'SLNo':'','Given Name':'','StreetAddress':'',
'City':'','State':'','ZipCode':'','Postal Code':'',
'EmailAddress':'','Principal Investigator':'',
'CIRN':'','Birthday':'','CCNumber':'','CCExpires':'',
'NationallD':'','Occupation':'','Organization':'',
'Vehicle':'','Grant Number':'','Grant Title':'','NIH/INS':''}

present_text = "";
with open(sys.argv[1], 'r') as my_file:
    my_lines = my_file.readlines()
    for my_line in my_lines:
        if(not my_line.strip()):
            if(len(multiLine)>0 and multiFlag==1 and strtAddress==0 and 
                givName==1 ):   # multiline breaks at next empty line
                row['StreetAddress'] = multiLine.strip()
                multiFlag =0
                strtAddress =1
                multiline = ""
            if(len(multiLine)>0 and multiFlag==1 and grntTitle==0 and 
                grntNum==1):
                row['Grant Title'] = multiGrant.strip()
                multiFlag =0
                grntTitle =1
                multiGrant = ""

        else:
            if(slNo==0):
                row['SLNo'] = my_line.strip()
                slNo = 1
            elif(slNo==1 and givName==0):
                row['Given Name'] = my_line.strip()
                givName=1;
            elif(givName==1 and strtAddress==0):  #this multiline approach. 
                multiFlag = 1
                multiLine = multiLine + my_line
            elif(strtAddress==1 and city ==0):
                row['City'] = my_line.strip()
                city=1
            elif(city==1 and state==0):
                row['State']= my_line.strip()
                state = 1
            elif(state==1 and zipCode==0):
                row['ZipCode']= my_line.strip()
                zipCode=1
            elif(zipCode==1 and postalCode==0):
                row['Postal Code']= my_line.strip()
                postalCode = 1
            elif(postalCode==1 and emlAdrs==0):
                row['EmailAddress']= my_line.strip()
                emlAdrs = 1
            elif(emlAdrs==1 and prncplInvestgtr==0):
                prncplInvestgtr=1
                row['Principal Investigator']= my_line.strip()
            elif(prncplInvestgtr==1 and cirn==0):
                row['CIRN']= my_line.strip()
                cirn =1
            elif(cirn==1 and birthday==0):
                birthday =1
                row['Birthday']= my_line.strip()
            elif(birthday==1 and ccnum==0):
                ccnum = 1
                row['CCNumber']= my_line.strip()
            elif(ccnum==1 and ccexp==0):
                ccexp=1
                row['CCExpires']= my_line.strip()
            elif(ccexp==1 and ntnlId==0):
                ntnlId=1
                row['NationallD']= my_line.strip()
            elif(ntnlId==1 and occupsn ==0):
                occupsn =1
                row['Occupation']= my_line.strip()
            elif(organsn==0 and occupsn==1):
                organsn=1
                row['Organization']= my_line.strip()
            elif(vhcl==0 and organsn==1):
                vhcl=1
                row['Vehicle']= my_line.strip()
            elif(vhcl==1 and grntNum==0):
                grntNum=1
                row['Grant Number']= my_line.strip()
            elif(grntTitle==0 and grntNum==1):
                multiFlag = 1
                multiGrant = multiGrant + my_line
            elif(grntTitle==1 and nih==0):
                nih=1
                row['NIH/INS']= my_line.strip()

xfile = openpyxl.load_workbook(excelFile)
sheet = xfile.get_sheet_by_name('Sheet1')
row_num = int(row['SLNo'])-1201+2
sheet['B'+str(row_num)] = row['Given Name'].strip("',")
sheet['C'+str(row_num)] = row['StreetAddress'].strip("',")
sheet['D'+str(row_num)] = row['City'].strip("',")
sheet['E'+str(row_num)] = row['State'].strip("',")
sheet['F'+str(row_num)] = row['ZipCode'].strip("',")
sheet['G'+str(row_num)] = row['Postal Code'].strip("',")
sheet['H'+str(row_num)] = row['EmailAddress'].strip("',")
sheet['I'+str(row_num)] = row['Principal Investigator'].strip("',")
sheet['J'+str(row_num)] = row['CIRN'].strip("',")
sheet['K'+str(row_num)] = row['Birthday'].strip("',")
sheet['L'+str(row_num)] = row['CCNumber'].strip("',")
sheet['M'+str(row_num)] = row['CCExpires'].strip("',")
sheet['N'+str(row_num)] = row['NationallD'].strip("',")
sheet['O'+str(row_num)] = row['Occupation'].strip("',")
sheet['P'+str(row_num)] = row['Organization'].strip("',")
sheet['Q'+str(row_num)] = row['Vehicle'].strip("',")
sheet['R'+str(row_num)] = row['Grant Number'].strip("',")
sheet['S'+str(row_num)] = row['Grant Title'].strip("',")
sheet['T'+str(row_num)] = row['NIH/INS'].strip("',")
xfile.save(excelFile)




