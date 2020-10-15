import os


def main():
    print('='*90)
    print("000      000        000                                                                      ")
    print("000     000   000   000             Y0000   000     000   000  A000A         .d0000000b.     ")
    print("000   000     000   000          0000       000     000   00000    0000     d000P   Y000b    ")
    print("000000              000000     0000         000     000   000        000   d000P     Y00b    ")
    print("000  000      000   000           Y0000     000     000   000        000   000000000000000   ")
    print("000   000     000   000              Y000   000     000   000        000    Y00000b.         ")
    print("000    000    000   Y00b.         0000Y     000     000   000        000      Y000000b.      ")
    print("000     000   000    'Y0000    0000Y          Y0000Y      000        000        'Y000000     ")
    print('='*90)
    print("extensive hacking framework coded by da 1 and only @rai", "\n")
    print("[1]   Info Gathering")
    print("[2]   Vuln Analysis")
    print("[3]   Exploitation")
    print("[4]   Password Cracking")
    print("[5]   Wireless")
    print("[6]   Reverse Engineering")
    print("[7]   Hardware")
    print("[8]   Forensics")
    print("[9]   DDoS")
    print("[10]  DoS")
    choice = input("enter number of choice: ")
    
    if choice == "1":
        print("[*] Info Gathering module is know active...")
        print("[1] Footprinting")
        print("[2] Scanning")
        print("[3] Back")
        infochoice = input("Select a choice: ")

        if infochoice == "1":
            print("[*] Warming up Photon Scanner...")
            print("[!] Photon Scanner is now all warmed up...")
            domain = input("Enter target website URL: ")
            clone = input("Do you want to clone the website locally (y or n): ")
            
            if clone == "y":
                depth = input("What level depth of crawling would you like (default is 2): ")
                thread = input("How many threads (default is 2): ")
                delay = input("How many seconds delay between each HTTP request (Default is 0): ")
                timeout = input("Specify number of seconds to wait before considerring HTTP(S) request timed out (default is 5): ")
                wayback = input("Fetch archived URLs from archive.org to use as seeds (y or n): ")

                if wayback == "y":
                    secret = input("Look for auth or API keys or hashes (y or n): ")

                    if secret == "y":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)

                    
                    if secret == "n":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)

                if wayback == "n":
                     secret = input("Look for auth or API keys or hashes (y or n): ")

                     if secret == "y":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)

                    
                     if secret == "n":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + '-t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + '-t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + '--ninja' + ' --dns'
                            os.system(myCmd1)



            if clone == "n":
                depth = input("What level depth of crawling would you like (default is 2): ")
                thread = input("How many threads (default is 2): ")
                delay = input("How many seconds delay between each HTTP request (Default is 0): ")
                timeout = input("Specify number of seconds to wait before considerring HTTP(S) request timed out (default is 5): ")
                wayback = input("Fetch archived URLs from archive.org to use as seeds (y or n): ")

                if wayback == "y":
                    secret = input("Look for auth or API keys or hashes (y or n): ")

                    if secret == "y":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

                    
                    if secret == "n":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

                if wayback == "n":
                     secret = input("Look for auth or API keys or hashes (y or n): ")

                     if secret == "y":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

                    
                     if secret == "n":
                        form = input("Which output format would you like to save the data (csv or json): ")

                        if form == "csv":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=csv' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

                        if form == "json":
                            myCmd1 = 'python3 ./Modules/Photon/photon.py -u ' + domain + ' --clone' + ' -l ' + depth + ' -t ' + thread + ' -d ' + delay + ' --timeout=' + timeout + ' --wayback' + ' -v ' + '--export=json' + ' --keys ' + ' --dns'
                            os.system(myCmd1)

        if infochoice == "2":

            print("[1] Port Scanning")
            print("[2] GitHub Secrets Scanning")
            infochoice1 = input("Select a choice: ")

            if infochoice1 == "1":
                anon = input("Do you want to remain anonymous while scanning (y or n): ")

                if anon == "y":
                    URL = input("Input URL of target website: ")
                    print("[*] Resolving hostanme to an IP address to prevent DNS leaks, ")
                    myCmd = 'tor-resolve ' + URL
                    os.system(myCmd)
                    print("[*] Now scanning ports")
                    myCmd1 = 'proxychains4 nmap -sT -PN -n -sV -p 80,443,21,22 ' + myCmd
                    os.system(myCmd1)
                    print("ayyy u got em!")
                


                if anon == "n":
                    URL = input("Input URL of target website: ")
                    myCmd = 'nmap -v ' + URL
                    print("ayyy u got em!")


            

            
if __name__ == '__main__':
    main()
