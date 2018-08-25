import math

netime = [166,117,132,143,156,126,119,140,130,114,122,124,116,99,192]
nestation = ["Punggol", "Sengkang", "Buankok", "Hougang", "Kovan", "Serangoon", "Woodleigh", "Potong Pasir", "Boon Keng", "Farrer Park", "Little India", "Dhoby Ghaut", "Clarke Quay", "Chinatown", "Outram Park", "HarbourFront"]
cctime = [164,131,142,143,152,111,108,120,161,120,265,131,149,195,116,180,32,118,121,176,126,114,133,120,142,101,91]
ccstation = ["HarbourFront", "Telok Blangah", "Labrador Park", "Pasir Panjang", "Haw Par Villa", "Kent Ridge", "one-north", "Buona Vista", "Holland Village", "Farrer Road", "Botanic Gardens", "Caldecott", "Marymount", "Bishan", "Lorong Chuan", "Serangoon", "Bartley", "Tai Seng", "MacPherson", "Paya Lebar", "Dakota", "Mountbatten", "Stadium", "Nicoll Highway", "Promenade", "Esplanade", "Braw Basah", "Dhoby Ghaut"]
ewtime = [142,135,149,180,190,195,215,140,125,295,145,125,175,115,120,125,175,115,120,125,175,110,115,125,170,120,115,150,125,150,115,155,165,310,180,180]
ewstation = ["Tuas Link", "Tuas West Road", "Tuas Crescent", "Gul Circle", "Joo Koon", "Pioneer", "Boon Lay", "Lakeside", "Chinese Garden", "Jurong East", "Clementi", "Dover", "Buona Vista", "Commonwealth", "Queenstown", "Redhill", "Tiong Bahru", "Outram Park", "Tanjong Pagar", "Raffles Place", "City Hall", "Bugis", "Lavender", "Kallang", "Aljunied", "Paya Lebar", "Eunos", "Kembangan", "Bedok", "Tanah Merah", "Simei", "Tampines", "Pasir Ris"]
nstime = [140,142,148,142,101,120,146,161,131,113,157,228,236,375,180,407,167,143,132,139,285,161,390,138,198]
nsstation = ["Marina South Pier","Marina Bay","Raffles Place", "City Hall", "Dhoby Ghaut", "Somerset", "Orchard", "Newton", "Novena", "Toa Payoh", "Braddell", "Bishan", "Ang Mo Kio", "Yio Chu Kang", "Khatib", "Yishun", "Sembawang", "Admiralty", "Woodlands", "Marsiling", "Kranji", "Yew Tee", "Choa Chu Kang", "Bukit Gombak", "Bukit Batok", "Jurong East"]
dttime = [81,184,131,135,143,144,128,113,113,133,152,138,118,103,112,129,102,85,106,135,113,111,79,144,145,113,122,113,127,117,208,110,149]
dtstation = ["Expo", "Upper Changi", "Tampines East", "Tampines", "Tampines West", "Bedok Reservoir", "Bedok North", "Kaki Bukit", "Ubi", "MacPherson", "Mattar", "Geylang Bahru", "Bendemeer", "Jalan Besar", "Bencoolen", "Fort Canning", "Chinatown", "Telok Ayer", "Downtown", "Bayfront", "Promenade", "Bugis", "Rochor", "Little India", "Newton", "Stevens", "Botanic Gardens", "Tan Kah Kee", "Sixth Avenue", "King Albert Park", "Beauty World", "Hillview", "Cashew", "Bukit Panjang"]

global startline
startline=0

def startstation(start):
    global numstart
    global linestart
    if start in nestation:   
        numstart = nestation.index(start)
        linestart = nestation
    elif start in ccstation:
        numstart = ccstation.index(start)
        linestart = ccstation
    elif start in ewstation:
        numstart = ewstation.index(start)
        linestart = ewstation
    elif start in nsstation:
        numstart = nsstation.index(start)
        linestart = nsstation
    elif start in dtstation:
        numstart = dtstation.index(start)
        linestart = dtstation

def endstation(end):
    global numend
    global lineend
    if end in nestation:
        numend = nestation.index(end)
        lineend = nestation
    elif end in ccstation:
        numend = ccstation.index(end)
        lineend = ccstation
    elif end in ewstation:
        numend = ewstation.index(end)
        lineend = ewstation
    elif end in nsstation:
        numend = nsstation.index(end)
        lineend = nsstation
    elif end in dtstation:
        numend = dtstation.index(end)
        lineend = dtstation

'''def srtime():
    global time
    if lineend = linestart and lineend!=ccstation:
        for x in range(min(numend,numstart),max(numend,numstart)):
            if linestart == nestation:
           time += netime[x+min(numstart,numend)]
            print(nestation[x+min(numstart,numend)])
        elif linestart == ewstation:
            time += ewtime[x+min(numstart,numend)]
        elif linestart == nsstation:
            time += nstime[x+min(numstart,numend)]
        elif linestart == dtstation:
            time += dttime[x+min(numstart,numend)]'''
        
    
def settime():
    global time
    diff = max(numstart,numend) - min(numstart,numend)
    for x in range(diff):
        if linestart == nestation:
            time += netime[x+min(numstart,numend)]
            #print(nestation[x+min(numstart,numend)])
        elif linestart == ccstation:
            time += cctime[x+min(numstart,numend)]
            #print(ccstation[x+min(numstart,numend)])
        elif linestart == ewstation:
            time += ewtime[x+min(numstart,numend)]
            #print(ewstation[x+min(numstart,numend)])
        elif linestart == nsstation:
            time += nstime[x+min(numstart,numend)]
            #print(nsstation[x+min(numstart,numend)])
        elif linestart == dtstation:
            time += dttime[x+min(numstart,numend)]
            #print(dtstation[x+min(numstart,numend)])
        
def checkinterchange():
    if linestart != lineend:
        for x in range(len(linestart)):
            check = linestart[x]
            if check in lineend:
                endstation(check)
                settime()
                linestart.pop(linestart.index(check))
                startstation(check)
                endstation(endd)
                settime()
                break

def calc():
    global time
    startstation(startt)
    endstation(endd)
    if linestart == lineend:
        settime()
    else:
        checkinterchange()
        time += 300
    minutes = time//60
    seconds = time%60
    '''print(time)'''
    print("It takes about " + str(minutes) + " minutes")
    print()

def train():
    global startt
    global endd
    global time
    startt = input("Starting station: ")
    endd = input("Destination: ")
    time = 0
    calc()

while 1==1:
    train()
