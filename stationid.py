def stationid():
    stopid = 0
    line = input("Enter route color (Red/Blue/Brown/Green/Orange/Purple/Pink/Yellow): ")
    line = line.lower()
    while line not in ['red','blue','brown','green','orange','purple','pink','yellow']:
        print("Error, invalid input")
        line = input("Enter route color (Red/Blue/Brown/Green/Orange/Purple/Pink/Yellow): ")
        line = line.lower()
    station = input("Type first 2 letters/numbers of stop: ")
    station = station.lower()
    if line == "red":
        if station == "47":
            stopid = 41230
        if station == "63":
            stopid = 40910
        if station == "69":
            stopid = 40990
        if station == "79":
            stopid = 40240
        if station == "87":
            stopid = 41230
        if station == "95":
            stopid = 40450
        if station == "ad":
            stopid = 41420
        if station == "ar":
            stopid = 41200
        if station == "be":
            response = input("Please enter full name (Belmont/Berwyn) ")
            response = response.lower()
            if response == "belmont":
                stopid = 41320
            if response == "berwyn":
                stopid = 40340
            else:
                print("Error, invalid input")
        if station == 'br':
            stopid = 41380
        if station == 'ce':
            stopid = 41000
        if station == 'ch':
            stopid = 41450
        if station == 'cl':
            stopid = 40630
        if station == 'fu':
            stopid = 41220
        if station == 'ga':
            stopid = 41170
        if station == 'gr':
            response = input("Please enter full name (Grand/Granville) ")
            response = response.lower()
            if response == "grand":
                stopid = 40330
            if response == "granville":
                stopid = 40760
            else:
                print("Error, invalid input")
        if station == 'ha':
            stopid = 41490
        if station == 'ho':
            stopid = 40900
        if station == 'ja':
            response = input("Please enter full name (Jackson/Jarvis) ")
            response = response.lower()
            if response == "jackson":
                stopid = 40560
            if response == "jarvis":
                stopid = 41190
            else:
                print("Error, invalid input")
        if station == 'la':
            response = input("Please enter full name (Lake/Lawrence) ")
            response = response.lower()
            if response == "lake":
                stopid = 41660
            if response == "lawrence":
                stopid = 40770
            else:
                print("Error, invalid input")
        if station == 'lo':
            stopid = 41300
        if station == 'mo':
            response = input("Please enter full name (Monroe/Morse) ")
            response = response.lower()
            if response == "monroe":
                stopid = 41090
            if response == "morse":
                stopid = 40100
            else:
                print("Error, invalid input")
        if station == 'no':
            stopid = 40650
        if station == 'ro':
            stopid = 41400
        if station == 'sh':
            stopid = 40080
        if station == 'so':
            stopid = 40190
        if station == 'th':
            stopid = 40880
        if station == 'wi':
            stopid = 40540
    if line == 'blue':
        if station == 'ad':
            stopid = 41240
        if station == 'au':
            stopid = 40010
        if station == 'be':
            stopid = 40060
        if station == 'ca':
            stopid = 40570
        if station == 'ch':
            stopid = 41410
        if station == 'ci':
            stopid = 40970
        if station == 'cl':
            response = input("Please enter full name (Clark/Lake/Clinton) ")
            response = response.lower()
            if response == "clark/lake":
                stopid = 40380
            if response == "clinton":
                stopid = 40430
            else:
                print("Error, invalid input")
        if station == 'cu':
            stopid = 40230
        if station == 'da':
            stopid = 40590
        if station == 'di':
            stopid = 40320
        if station == 'fo':
            stopid = 40390
        if station == 'ga':
            stopid = 40490
        if station == 'ha':
            response = input("Harlem on which branch? (Forest Park/OHare) ")
            response = response.lower()
            if response == "forest park":
                stopid = 40980
            if response == "ohare":
                stopid = 40750
            else:
                print("Error, invalid branch")
        if station == 'il':
            stopid = 40810
        if station == 'ir':
            stopid = 40550
        if station == 'ja':
            stopid = 40070
        if station == 'je':
            stopid = 41280
        if station == 'ke':
            stopid = 40250
        if station == 'la':
            stopid = 41340
        if station == 'lo':
            stopid = 41020
        if station == 'mo':
            response = input("Please enter full name (Monroe/Montrose) ")
            response = response.lower()
            if response == "monroe":
                stopid = 40790
            if response == "montrose":
                stopid = 41330
            else:
                print("Error, invalid input")
        if station == 'oh':
            stopid = 40890
        if station == 'oa':
            stopid = 40180
        if station == 'pu':
            stopid = 40920
        if station == 'ra':
            stopid = 40470
        if station == 'ro':
            stopid = 40820
        if station == 'ui':
            stopid = 40350
        if station == 'wa':
            stopid = 40370
        if station == 'we':
            response = input("Western on which branch? (Forest Park/OHare) ")
            response = response.lower()
            if response == "forest park":
                stopid = 40220
            if response == "ohare":
                stopid = 40670
            else:
                print("Error, invalid branch")
    if line == 'brown':
        if station == 'ad':
            response = input("Please enter full name (Adams/Wabash/Addison) ")
            response = response.lower()
            if response == "adams/wabash":
                stopid = 40680
            if response == "addison":
                stopid = 41440
            else:
                print("Error, invalid input")
        if station == 'ar':
            stopid = 40660
        if station == 'be':
            stopid = 41320
        if station == 'ch':
            stopid = 40710
        if station == 'cl':
            stopid = 40380
        if station == 'da':
            stopid = 40090
        if station == 'di':
            stopid = 40530
        if station == 'fr':
            stopid = 40870
        if station == 'fu':
            stopid = 41220
        if station == 'ha':
            stopid = 40850
        if station == 'ir':
            stopid = 41460
        if station == 'ke':
            stopid = 41180
        if station == 'ki':
            stopid = 41290
        if station == 'la':
            stopid = 40160
        if station == 'me':
            stopid = 40460
        if station == 'mo':
            stopid = 41500
        if station == 'pa':
            stopid = 41310
        if station == 'qu':
            stopid = 40040
        if station == 'ro':
            stopid = 41010
        if station == 'se':
            stopid = 40800
        if station == 'so':
            stopid = 40360
        if station == 'st':
            stopid = 40260
        if station == 'wa':
            response = input("Washington/_____ (Wabash/Wells) ")
            response = response.lower()
            if response == "wabash":
                stopid = 41700
            if response == "wells":
                stopid = 40730
    if line == 'green':
        if station == '35':
            stopid = 41120
        if station == '43':
            stopid = 41270
        if station == '47':
            stopid = 41080
        if station == '51':
            stopid = 40130
        if station == 'ad':
            stopid = 40680
        if station == 'as':
            response = input("Please enter full name (Ashland/Ashland/63rd) ")
            response = response.lower()
            if response == "ashland":
                stopid = 40170
            if response == "ashland/63rd":
                stopid = 40290
        if station == 'au':
            stopid = 41260
        if station == 'ca':
            stopid = 41360
        if station == 'ce':
            response = input("Please enter full name (Central/Cermak-McCormick Place) ")
            response = response.lower()
            if response == "central":
                stopid = 40280
            if response == "cermak-mccormick place":
                stopid = 41690
            else:
                print("Error, invalid input")
        if station == 'cl':
            response = input("Please enter full name (Clark/Lake/Clinton) ")
            response = response.lower()
            if response == "clark/lake":
                stopid = 40380
            if response == "clinton":
                stopid = 40430
            else:
                print("Error, invalid input")
        if station == 'co':
            response = input("Please enter full name (Conservatory-Central Park Drive/Cottage Grove) ")
            response = response.lower()
            if response == "conservatory-central park drive":
                stopid = 41670
            if response == "cottage grove":
                stopid = 40720
            else:
                print("Error, invalid input")
        if station == 'ga':
            stopid = 40510
        if station == 'ha':
            response = input("Please enter full name (Halsted/Harlem) ")
            response = response.lower()
            if response == "halsted":
                stopid = 40940
            if response == "harlem":
                stopid = 40020
            else:
                print("Error, invalid input")
        if station == 'in':
            stopid = 40300
        if station == 'ke':
            stopid = 41070
        if station == 'ki':
            stopid = 41140
        if station == 'la':
            stopid = 40700
        if station == 'mo':
            stopid = 41510
        if station == 'oa':
            stopid = 41350
        if station == 'pu':
            stopid = 40030
        if station == 'ri':
            stopid = 40610
        if station == 'ro':
            stopid = 41400
        if station == 'st':
            stopid = 40260
        if station == 'wa':
            stopid = 41700
    if line == 'orange':
        if station == '35':
            stopid = 40120
        if station == 'ad':
            stopid = 40680
        if station == 'as':
            stopid = 41060
        if station == 'ha':
            stopid = 40380
        if station == 'ha':
            response = input("Please enter full name (Halsted/Harold Washington Library-State/Van Buren) ")
            response = response.lower()
            if response == "halsted":
                stopid = 41130
            if response == "harold washington library-state/van buren":
                stopid = 40850
            else:
                print("Error, invalid input")
        if station == 'ke':
            stopid = 41150
        if station == 'la':
            stopid = 40160
        if station == 'mi':
            stopid = 40930
        if station == 'pu':
            stopid = 40960
        if station == 'qu':
            stopid = 40040
        if station == 'ro':
            stopid = 41400
        if station == 'st':
            stopid = 40260
        if station == 'wa':
            response = input("Washington/_____ (Wabash/Wells) ")
            response = response.lower()
            if response == "wabash":
                stopid = 41700
            if response == "wells":
                stopid = 40730
        if station == 'we':
            stopid = 40310
    if line == 'purple':
        if station == 'ad':
            stopid = 40680
        if station == 'ar':
            stopid = 40660
        if station == 'be':
            stopid = 41320
        if station == 'ce':
            stopid = 41250
        if station == 'ch':
            stopid = 40710
        if station == 'cl':
            stopid = 40380
        if station == 'da':
            stopid = 40050
        if station == 'de':
            stopid = 40690
        if station == 'di':
            stopid = 40530
        if station == 'fo':
            stopid = 40520
        if station == 'fu':
            stopid = 41220
        if station == 'ha':
            stopid = 40850
        if station == 'ho':
            stopid = 40900
        if station == 'la':
            stopid = 40160
        if station == 'li':
            stopid = 41050
        if station == 'ma':
            stopid = 40270
        if station == 'me':
            stopid = 40460
        if station == 'no':
            stopid = 40400
        if station == 'qu':
            stopid = 40040
        if station == 'se':
            stopid = 40080
        if station == 'so':
            stopid = 40840
        if station == 'st':
            stopid = 40260
        if station == 'wa':
            response = input("Washington/_____ (Wabash/Wells) ")
            response = response.lower()
            if response == "wabash":
                stopid = 41700
            if response == "wells":
                stopid = 40730
        if station == 'we':
            stopid = 41210
        if station == 'wi':
            stopid = 40540
    if line == 'pink':
        if station == '18':
            stopid = 40830
        if station == '54':
            stopid = 40580
        if station == 'ad':
            stopid = 40680
        if station == 'as':
            stopid = 40170
        if station == 'ca':
            stopid = 40440
        if station == 'ce':
            stopid = 40780
        if station == 'ci':
            stopid = 40420
        if station == 'cl':
            response = input("Please enter full name (Clark/Lake/Clinton) ")
            response = response.lower()
            if response == "clark/lake":
                stopid = 40380
            if response == "clinton":
                stopid = 40430
            else:
                print("Error, invalid input")
        if station == 'da':
            stopid = 40210
        if station == 'ha':
            stopid = 40850
        if station == 'ke':
            stopid = 41040
        if station == 'ko':
            stopid = 40600
        if station == 'la':
            stopid = 40160
        if station == 'mo':
            stopid == 41510
        if station == 'po':
            stopid = 41030
        if station == 'qu':
            stopid = 40040
        if station == 'st':
            stopid = 40260
        if station == 'wa':
            response = input("Washington/_____ (Wabash/Wells) ")
            response = response.lower()
            if response == "wabash":
                stopid = 41700
            if response == "wells":
                stopid = 40730
        if station == 'we':
            stopid = 40740
    if line == 'yellow':
        if station == 'de':
            stopid = 40140
        if station == 'ho':
            stopid = 40900
        if station == 'oa':
            stopid = 41680

    route = formatLine(line)  
    return stopid, route.capitalize()

def formatLine(line):
    if line == 'green':
        line = 'G'
    if line == 'brown':
        line = 'Brn'
    if line == 'purple':
        line = 'P'
    if line == 'orange':
        line = 'Org'
    if line == 'yellow':
        line = 'Y'
    return line
