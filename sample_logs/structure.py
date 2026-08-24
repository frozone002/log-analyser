from datetime import datetime

#-------------------

def main():
    print()
    print("LOG ANALYSIS SUMMARY\n====================")
    print(f"total lines rendered: {linesRendered()} \n")
    print(f"Latest run time : {timestamp()}")

    print("Severity counts:")
    for i in checker():
        print(i)

    print(common())
        

#--------------------------------

def linesRendered():
    lines = len(file())
    return lines

def timestamp() :
    for i in file():
        split = i.split(' ')
        date = split[0:2]
        string = ' '.join(date)
        convert = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
        return convert

def timeRange():
    pass

def common():
    mostCommon = {}
    for i in file():
        if "ERROR" in i:
            split = i.split('ERROR')
            res = split[-1].strip(' ')
            if res not in mostCommon:
                mostCommon[res] = 1
            else:
                mostCommon[res] = mostCommon[res] + 1
    return mostCommon
            

            
def file():
     with open("sample_logs/sample.log", "r") as f:
          read = f.readlines()
          return read
         

def checker(): #uses dictionary 
     checkerdic = {
         "ERROR": 0,
         "WARNING": 0,
         "INFO": 0
     }
     for i in file():
        if "ERROR" in i:
            checkerdic.update({'ERROR': checkerdic.get('ERROR', 0) + 1})
        if "WARNING" in i:
            checkerdic.update({'WARNING': checkerdic.get('WARNING', 0) + 1})
        if "INFO" in i:
            checkerdic.update({'INFO': checkerdic.get('INFO', 0) + 1})

     return f"ERROR: {checkerdic.get('ERROR')}", f"WARNING: {checkerdic.get('WARNING')}", f"INFO: {checkerdic.get('INFO')}"
    
            
               
main()
