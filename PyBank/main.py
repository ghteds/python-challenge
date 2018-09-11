import csv

file="../hw 3 py/budget_data.csv"


with open(file, newline='') as f:
    theReader = csv.reader(f,delimiter=',')
    theHeader=next(theReader)
    rowCounter=1
    theChanges=[]
    theGreatestI = 0
    theGreatestD = 0
    theChange=0
    theCellSum=0

    print('Financial Analyis')
    print('------------------------------')

    for row in theReader:
        theLabel=row[0]
        theCell=row[1]
        
        
        if int(theCell) > 0 and int(theCell) > int(theGreatestI):    
            theGreatestI=theCell
            theGreatestILabel=theLabel
        elif int(theCell) < 0 and int(theCell)< int(theGreatestD):            
            theGreatestD=theCell
            theGreatestDLabel=theLabel

        if rowCounter == 1:
            rowCounter = rowCounter + 1
            thePreviousCell = theCell
            theCellSum=theCellSum + int(theCell)
            #elif:
        else:
            theChange=int(theCell)-int(thePreviousCell)
            theChanges.append(theChange)
            #print(theLabel + ': ' + thePreviousCell + ' ' + theCell)
            #print(theChange)
            theCellSum=theCellSum + int(theCell)
            thePreviousCell=theCell    
            rowCounter = rowCounter + 1

        if int(theChange) > 0 and int(theChange) > int(theGreatestI):    
            theGreatestI=theChange 
            theGreatestILabel=theLabel
        elif int(theChange) < 0 and int(theChange)< int(theGreatestD):            
            theGreatestD=theChange
            theGreatestDLabel=theLabel

    
        #thePreviousCell=theCell    
        #rowCounter = rowCounter + 1
theSumOfChanges=sum(theChanges)
denominator=len(theChanges)
theAverageChange=int(theSumOfChanges)/int(denominator)
#print(denominator)

#print(theSumOfChanges)

print('Total Months: ' + str(rowCounter-1))
print('Total: ' + str(theCellSum))
print('Average Change: ' + str(theAverageChange))


print('The Greatest Increase in Profits: ' + str(theGreatestILabel) + ' (' + str(theGreatestI)+')')
print('The Greatest Decrease Profits: ' + str(theGreatestDLabel) + ' (' + str(theGreatestD)+ ')')

#write to file

outfile="../hw 3 py/python-challenge/PyBank/budgetOut.csv"

with open(outfile,'w',newline='') as csvFile:
    csvwriter=csv.writer(csvFile,delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months:',str(rowCounter-1)])
    csvwriter.writerow(['Total:',str(theCellSum)])
    csvwriter.writerow(['Average Change:',str(theAverageChange)])
    csvwriter.writerow(['The Greatest Increase in Profits: ',str(theGreatestILabel),str(theGreatestI)])
    csvwriter.writerow(['The Greatest Decrease Profits: ',str(theGreatestDLabel),str(theGreatestD)])

    