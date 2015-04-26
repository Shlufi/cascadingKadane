#!/usr/bin/pyhton

# Globals
FILENAME     = 'FOO.txt'
NUM_FEATURES = 10


import cvs

class fileStruct:
        def __init__(self):
            self.cols = 0
            self.rows = 0
            self.readInCSV()
            self.initDataStruct()

        def readInCSV(self):
            ''' Read in Spread Sheet and stores it as is''' 
            filePoint = fopen(FILENAME, 'rb')
            dataFile = csv.reader(filePoint, 'rb')
            self.spreadSheet = []
            for row in spamReader:
                self.spreadSheet.append(row)
            self.cols = len(self.spreadSheet[0])
            self.rows = len(self.spreadSheet)

        def initDataStruct(self):
            ''' Structures spreadsheet data into classes'''
            for row in xrange(self.rows):
                    for col in xrange(1, self.cols - 2):
                        dataCell = self.initDataCell(row, col) 

        def initDataCell(row, col):
            parentID      = self.spreadSheet[row][0]
            featureVal    = self.spreadSheet[row][col]
            featureNumber = col + -1
            isTarget      = self.spreadSheet[row][-2]
            weight        = self.spreadSheet[row][-1]
                
            return DataCell(parentID, featureVal, isTarget, weight)


class DataCell:
        def __init__(parentID, featureVal, featureNumber, isTarget, weight):
            
            self.parentID      = parentID
            self.featureVal    = featureVal 
            self.featureNumber = featureNumber 
            self.isTarget      = isTarget 
            self.weight        = weight 

class DataColum:
    def __init__(colList)
            
            self.featureNumber = colList[0].featureVal 




if __name__ == '__main__':
            
    
    inputCSV = fileStruct()
