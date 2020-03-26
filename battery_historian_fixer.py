import re
import sys

verbose = False
usage = '''
usage: python battery_historian_fixer.py <source_file_path> [-v]
______________________________________________________________
-v provides more details as it runs

'''

def removeFraction(content):
    try:
        vals = content.split(",")
        for i in range(len(vals)):
            try:
                vals[i] = str(int(round(float(vals[i]))))
            except Exception:
                pass
        newContent = ",".join(vals)
        if verbose:
            print("%s -> %s" % (content, newContent))
        if not newContent.endswith('\n'):
            newContent += '\n'
        return newContent
    except Exception:
        return content

def getOutputPath(inputPath):
    idxOfDot = inputPath.rfind(".")
    if(idxOfDot != -1 and inputPath[idxOfDot + 1:] in ["txt", "log"]):
        return inputPath[0:idxOfDot] + "_fixed" + inputPath[idxOfDot:]
    else:
        return inputPath + "_fixed"

def main():
    inputPath = None
    global verbose
    global usage
    if len(sys.argv) < 2:
        print(usage)
        return
    for i in range(1, len(sys.argv)):
        if(sys.argv[i] == '-v'):
            verbose = True
        else:
            inputPath = sys.argv[i]

    try:
        inputFile = open(inputPath, 'r', encoding='utf-8', errors='ignore')
    except Exception:
        print("invalid file path: " + inputPath)
        return

    outputPath = getOutputPath(inputPath)
    outputFile = open(outputPath, 'w', encoding='utf-8')

    isInCheckIn = False

    num = 0

    try:
        for line in inputFile:
            if isInCheckIn:
                if line.find("== Running Application Activities") != -1:
                    isInCheckIn = False
                    print("exit checkin section")
                if line.find(",wfcd,") != -1 or line.find(",gwfcd,") != -1:
                    line = removeFraction(line)
                elif line.find(",mcd,") != -1 or line.find(",gmcd,") != -1:
                    line = removeFraction(line)
                elif line.find(",ble,") != -1 or line.find(",gble,") != -1:
                    line = removeFraction(line)
            else:
                if line.find("CHECKIN BATTERYSTATS") != -1:
                    isInCheckIn = True
                    print("enter checkin section")
            outputFile.write(line)
            num += 1
        print("everything done! Output path is " + outputPath)
    finally:
        outputFile.close()
        inputFile .close()
main()


    

