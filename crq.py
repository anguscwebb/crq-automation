from pyperclip import copy, paste; from webbrowser import open; import pyautogui as p, time, sys, datetime

#############################    HELPER FUNCTIONS    ###################################

def ciArrayGenerator(*args): #generates array of CI numbers
    ciArray = [None] * (len(args) + 1)
    ciArray[len(args)] = "CI000000XXXXXXX"
    for i in range(len(ciArray)-1):
        ciArray[i] = args[i]
    return ciArray

def ciNumberEntry(): #relates all CI numbers in eSMT
    for i in range(len(ciArray)):
        searchFor('images/relationshipsmagnifyer.PNG', bottomRightQuadrant)
        searchFor('images/useadvancedsearch.PNG', topRightQuadrant)
        searchFor('images/ciid.PNG', topLeftQuadrant)
        p.write(ciArray[i])
        searchFor('images/relationshipsearch.PNG', bottomLeftQuadrant)
        searchFor('images/relationshiprelate.PNG', bottomLeftQuadrant)
        searchFor('images/relationshipok.PNG', middleQuadrant)

def riskAssessment(start, end): #completes a page of the risk assessment questionairre
    for i in range(start, end):
        for j in range(2):
            imageString = 'images/ra{}{}prod.PNG'.format(i, j) if (i == 0 and j == 1 and uatOrProd == 'PROD') else 'images/ra{}{}.PNG'.format(i, j)
            searchFor(imageString, (664, 12, 620, 1000))

def searchFor(image, regionToSearch=(0, 0, 1920, 1080)): #keep searching for an image
    print("Searching for: " + image)
    r = None
    while r is None:
        try:
            location = p.locateOnScreen(image, grayscale=True, region=regionToSearch, confidence=0.7)
            p.click(location)
            p.sleep(1)
            return location
        except Exception as e:
            r = None

def getRequestor(): #retrieve the name of the requestor based on the application acronym (FOR PRIVACY REASONS, NONE OF THESE NAMES ARE REAL PEOPLE)
    if acronym == "CDMS":
        return "Dave", ciArrayGenerator("CI0000000XXXXXX", "CI0000000XXXXXX")
    elif acronym == "PMIS":
        return "Kim", ciArrayGenerator("CI0000000XXXXXX", "CI0000000XXXXXX")
    elif acronym == "CAS":
        return "Charlie", ciArrayGenerator("CI000000XXXXXXX", "CI000000XXXXXXX")
    elif acronym == "PPS":
        return "William", ciArrayGenerator("CI00000000XXXXX")
    elif acronym == "BMS":
        return "Mark", ciArrayGenerator("CI000000XXXXXXX")
    elif acronym == "ADBT":
        return "Emma", ciArrayGenerator("CI000000XXXXXXX")
    elif acronym == "TMITR":
        return "Lawrence", ciArrayGenerator("CI00000000XXXXX")
    elif acronym == "AMS":
        return "Sam", ciArrayGenerator("CI0000000XXXXXX", "CIAPP0000000XXX")
    elif acronym == "TIS":
        return "Rodney", ciArrayGenerator("CI00000000XXXX")

topLeftQuadrant = (0, 0, 959, 539)
topRightQuadrant = (959, 0, 959, 539)
bottomLeftQuadrant = (0, 539, 959, 539)
bottomRightQuadrant = (959, 539, 959, 539)
middleQuadrant = (479, 269, 959, 539)

print("\n\n")
print("  *************************************************************************")
print("  **                                                                     **")
print("  **                                                                     **")
print("  **                   CRQ Automation Tool (ver. 2.0)                    **")
print("  **               by Angus Webb & Redwan Chowdhury, 2024                **")
print("  **                                                                     **")
print("  **                                                                     **")
print("  *************************************************************************")
print("\n\n\n\n")

#############################    OBTAINING DATA FROM USER     ###################################
acronym = input("Please enter the acronym for the CRQ: ").upper()
requestor, ciArray = getRequestor()
uatOrProd = input("Is this CRQ UAT or PROD?: ").upper()
startTime, endTime = ("8:00:00 AM", "4:00:00 PM") if (uatOrProd == "UAT") else ("5:00:00 PM", "8:00:00 PM")
date = input("Please enter the CRQ's date in the following format: MM/DD/YYYY: ")
month = int(date.split('/')[0])
day = int(date.split('/')[1])
year = int(date.split('/')[2])
dateShortForm = datetime.date(year, month, day).strftime("%b%d") #returns short form of date ie. "Jan01"
startDate = "{}/{}/{} {}".format(month, day, year, startTime)
endDate = "{}/{}/{} {}".format(month, day, year, endTime)
if (uatOrProd == "PROD"): uatNum = input("Please enter the CRQ number for UAT: ") #prompt for UAT CRQ number if PROD

print("\n\nCRQ information obtained. Opening eSMT in ", end="")
for char in "3...2...1...\n\n":
    time.sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()

#############################    AUTOMATION PROCESS     ##################################
open('LINK TO CRQ SUBMISSION WEBSITE (eSMT)')

#open a new change
searchFor('images/applications.PNG', topLeftQuadrant)
searchFor('images/changemanagementbutton.PNG', topLeftQuadrant)
p.move(300, 0, 0.2) 
p.move(0, 75, 0.5)
p.click()

#fill in first sections (service field, template, summary, notes, target date)
searchFor('images/servicefield.PNG', (342, 519, 800, 250))
p.write("LTC")
searchFor('images/serviceoption.PNG', (342, 519, 800, 250))
searchFor('images/templatesearch.PNG', (342, 519, 800, 250))
searchFor('images/templateltc.PNG', bottomLeftQuadrant)
searchFor('images/{}template.PNG'.format(uatOrProd), middleQuadrant)
searchFor('images/templateselect.PNG', bottomLeftQuadrant)
p.scroll(-1000)
p.sleep(2)
searchFor('images/uatsummary.PNG', topLeftQuadrant) if (uatOrProd == 'UAT') else searchFor('images/prodsummary.PNG', topLeftQuadrant)
p.tripleClick()
p.sleep(1)
p.write("LTC - .NET SDC Standard UAT Promotion - " + acronym + " - " + dateShortForm) if (uatOrProd == 'UAT') else p.write("LTC - .NET SDC PROD Promotion - " + acronym + " - " + dateShortForm)
searchFor('images/notes.PNG', topLeftQuadrant)
p.sleep(1)
p.hotkey('ctrl', 'a')
p.hotkey('ctrl', 'v')
searchFor('images/targetdate.PNG', topLeftQuadrant)
p.write(startDate)

#complete risk assessment
p.sleep(1)
searchFor('images/riskassessment.PNG', bottomLeftQuadrant) #start risk assessment
riskAssessment(0, 5) #page 1 of risk assessment
searchFor('images/ranext.PNG', bottomLeftQuadrant) #hit 'next'
riskAssessment(5, 7) #page 2 of risk assessment
searchFor('images/rasave.PNG', bottomLeftQuadrant) #hit 'save'

#manager/manager group
searchFor('images/managergroup.PNG', bottomLeftQuadrant)
p.write('ECM - LTC')
searchFor('images/managergroupoption.PNG', bottomLeftQuadrant)
p.move(0, 50)
searchFor('images/changemanager.PNG', bottomLeftQuadrant)
p.write('Anonymous Manager')
searchFor('images/changemanageroption.PNG', bottomLeftQuadrant)

#categorization tab
p.scroll(1000)
searchFor('images/categorizationtab.PNG', topRightQuadrant)
p.sleep(1)
searchFor('images/tier1.PNG', bottomRightQuadrant)
p.hotkey('ctrl', 'a')
p.write("Application Support (Tier 3)")

#relationships tab
searchFor('images/relationshipstab.PNG', topRightQuadrant)
p.sleep(1)
p.scroll(-1000)
searchFor('images/relationshiptabsearch.PNG', bottomRightQuadrant)
searchFor('images/configurationitem.PNG', bottomRightQuadrant)
ciNumberEntry()
if (uatOrProd == 'PROD'): #enter UAT CRQ if we are creating a PROD CRQ
    searchFor("relationshiptabsearch.PNG", bottomRightQuadrant)
    p.sleep(1)
    p.click() #click on infrastructure change
    p.move(200, 0)
    p.click()
    p.write(uatNum)
    searchFor('relationshipsmagnifyer.PNG', bottomRightQuadrant)
    searchFor('relationshiprelate.PNG', bottomLeftQuadrant)
    searchFor('relationshipok.PNG', middleQuadrant)

#date/system tab
p.scroll(1000)
p.sleep(1)
searchFor('images/datesystemtab.PNG', topRightQuadrant)
p.sleep(1)
searchFor('images/startdate.PNG', topRightQuadrant)
p.write(startDate)
searchFor('images/enddate.PNG', topRightQuadrant)
p.write(endDate)
p.scroll(-1000)
searchFor('images/outageduration.PNG', bottomRightQuadrant)
p.write("0")

#copy CRQ number and generate email to requestor
p.scroll(1000)
p.sleep(1)
p.doubleClick(654, 372)
p.hotkey('ctrl', 'c')
p.sleep(1)
copy("Hi " + requestor +  ",\n\n" + uatOrProd + " CRQ has been submitted, CRQ# is " + paste() + ".\n\n*Anonymous Name*, please create CODEREPO folder:\n\"" + paste() + "_" + acronym + " - " + uatOrProd + "\"\n\nAnd calendar entry for "+ dateShortForm + ":\n\"" + paste() + " - LTC - .NET SDC Standard " + uatOrProd + " Promotion LTC - " + acronym + " - " + dateShortForm + " - " + requestor + "\"\n\nThank you!")
print("Email has been copied to clipboard. Process complete./n")
exit()