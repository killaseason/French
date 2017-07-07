import urllib
import re

#Loop over a range of years/quarters
cik='1452922'

#For looping over all files in a company CIK directory
remoteFile=urllib.urlopen('https://www.sec.gov/Archives/edgar/data/'+cik)

#Below line for use in looping over years/quarters
#remoteFile=urllib.urlopen('https://www.sec.gov/Archives/edgar/full-index/1994/QTR1/master.idx')

#returns list of paths to subfolders containing filings
fileName1=re.compile(r'/Archives/edgar/data/'+re.escape(cik)+r'/([0-9]{10})([0-9]{2})([0-9]{6})')
subFolders=fileName1.findall(remoteFile.read())
#print subFolders

#This is the re to look for in the txt file
searchTerm=re.compile(r'.{1,100}Gould.{1,100}')

output=[]

#Loops through each folder and searches the txt file for terms.
for temp in subFolders[0:3]:
    path1='https://www.sec.gov/Archives/edgar/data/'
    path2=cik+'/'+temp[0]+temp[1]+temp[2]+'/'+temp[0]+'-'+temp[1]+'-'+temp[2]+'.txt'

    fileText=urllib.urlopen(path1+path2).read()
    hits=searchTerm.findall(fileText)
    output.append((path2,hits))
#    print hits


# Create an HTML file that provides information about the filing, hits from it, and a link to it.


print output

#remoteFile=urllib.urlopen('https://www.sec.gov/Archives/edgar/data/'+cik+'/'+subFolders[0])
#print remoteFile.read()

#fileName2=re.compile(r'/Archives/edgar/data/'+re.escape(cik)+r'/([0-9]{10})([0-9]{2})([0-9]{6})')
#fileName2=re.compile(r'[0-9]{18}')
#otherShit=fileName2.findall(remoteFile.read())
#print otherShit

#for line in remoteFile:
    #splitLine=line.split('|')
    #if (splitLine[0]=='1452922' or splitLine[0]=='92088'): print splitLine
#    print line


#Return all filings associated with a given company


#Retrieve a selection of documents

##Loop over selection of documents, search for a term in each, and return links to files with hits and
##the 10 words before and after the hits
