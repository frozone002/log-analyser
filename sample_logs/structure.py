from datetime import datetime

#-------------------
def main():
    print()
    print("LOG ANALYSIS SUMMARY")
    print("=" * 30)
    print(f"total lines rendered: {linesRendered()} ")
    print(f"Latest run time : {timestamp()}")
    print(timeRange(), "\n")
    

    print("Severity counts:")
    for i in checker():
        print(i)
        
    print()
    print("Top error messages:")
    fail_message()

    print("=" * 30)
    

#--------------------------------
                      
def file():
     with open("sample_logs/sample.log", "r") as f: #Enter the log path here
          read = f.readlines()
          return read


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
    emp = []
    for i in file():
        stripped = i.strip()
        split = stripped.split(' ')
        timeTable = split[0:2]
        if i.strip() == "":
            continue
        time = timeTable[-1]
        emp.append(time)

    return f"Time Range: {emp[0]}-{emp[-1]}" #gets the first and last index of the time within the set


def common():
    mostCommon = {}
    for i in file():
        if "ERROR" in i:
            split = i.split('ERROR')
            res = split[-1].strip()
            if res not in mostCommon:
                mostCommon[res] = 1
            else:
                mostCommon[res] = mostCommon[res] + 1

    return mostCommon


def fail_message():
    emp = []
    for msg, count in common().items(): #converts the messages and count as keys and values and iterates through the list
        info = (f"{msg}: ({count} time(s))")
        emp.append(info)
    for num, letter in enumerate(emp, 1): #turns the list into a numbered list
        print(num, letter)



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
