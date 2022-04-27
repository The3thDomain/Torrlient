#!/usr/bin/env python3
import os
import time
import sys
import getpass
import requests

header = {'User-agent': 'TorrlientVM'}
runmsg = "TorrlientVM can automaticly run scripts at startup.\nTo run any of the scripts detected in this log execute \"torrlientvm -init scriptname\".\n\n"

if getpass.getuser() == "root":
    if sys.argv[1] == "-update":
        os.chdir('/opt/TorrlientVM/')

        if os.path.exists('/bin/torrlientvm') == False: 
            os.system('sudo cp TorrlientVM.py /bin/torrlientvm')
            print('Shortcut Created For: TorrlientVM')

        elif open('/bin/torrlientvm', 'r').read() != open('/opt/TorrlientVM/TorrlientVM.py', 'r').read():
            os.system('sudo cp TorrlientVM.py /bin/torrlientvm')
            print('Updated: TorrlientVM')

    if sys.argv[1] == "-search":
        while True:
            if os.path.exists('/opt/TorrlientVM/telemetry.tdb'):
                try:
                    requests.get('https://api.torrlient.com', headers=header)
                except requests.exceptions.HTTPError as errh:
                    print('Err')
                except requests.exceptions.ConnectionError as errc:
                    print('Err')
                except requests.exceptions.Timeout as errt:
                    print('Err')
                except requests.exceptions.RequestException as err:
                    print('Err')
                
            users = os.listdir('/home/')
            for u in range(len(users)):
                os.chdir('/home/'+users[u]+'/')
                user = users[u]
                user_home = os.listdir('.')
                for x in range(len(user_home)):

                    if os.path.exists('/home/'+user+'/TorrlientVM-Runable.log'):
                        os.remove('/home/'+user+'/TorrlientVM-Runable.log')

                    if user_home[x].split('.')[1] == "py":
                        if os.path.exists('TorrlientVM-Runable.log') == False:
                            open('/home/'+user+'/TorrlientVM-Runable.log', 'a').write(runmsg)
                            open('/home/'+user+'/TorrlientVM-Runable.log', 'a').write('TorrlientVM Found Python File: '+user_home[x]+'\n')
                        else:
                            open('/home/'+user+'/TorrlientVM-Runable.log', 'a').write('TorrlientVM Found Python File: '+user_home[x]+'\n')

                    if user_home[x].split('.')[1] == "php":
                        if os.path.exists('TorrlientVM-Runable.log') == False:
                            open('/home/'+user+'/TorrlientVM-Runable.log', 'a').write(runmsg)
                            open('/home/'+user+'/TorrlientVM-Runable.log', 'a').write('TorrlientVM Found PHP File: '+user_home[x]+'\n')
                        else:
                            open('/home/'+user+'/TorrlientVM-Runable.log', 'a').write('TorrlientVM Found PHP File: '+user_home[x]+'\n')
            time.sleep(20)

    if sys.argv[1] == "-listen":
        run = os.listdir('/opt/TorrlientVM/')
        torun = []
        for r in range(len(run)):
            if getpass.getuser() and "tdb" in run[r].split('.'):
                torun.append(run[r])

        if len(torun) >= 1:
            while len(torun) >=1:
                torun.clear()
                ru = os.listdir('/opt/TorrlientVM/')
                for r in range(len(ru)):
                    if getpass.getuser() and "tdb" in ru[r].split('.'):
                        torun.append(ru[r])
                time.sleep(1)

            os.system('sudo poweroff')
        else:
            exit()
            

if getpass.getuser() != "root":
    print('\nWelcome to TorrlientVM\n')

    if len(sys.argv) >= 2:
        if sys.argv[1] == "-queue":
            run = os.listdir('/opt/TorrlientVM/')
            torun = []
            for r in range(len(run)):
                if getpass.getuser() and "tdb" in run[r].split('.'):
                    torun.append(open('/opt/TorrlientVM/'+run[r], 'r').read())
            if len(torun) >= 1:
                print(torun)

        if sys.argv[1] == "-init":
            if os.path.exists('/opt/TorrlientVM/'+getpass.getuser()+'.'+sys.argv[2]+'.tdb') == False:
                open('/opt/TorrlientVM/'+getpass.getuser()+'.'+sys.argv[2]+'.tdb', 'w').write(sys.argv[2])
                print(sys.argv[2]+' has been created for user: '+getpass.getuser()+ ', and will run once at next system reboot.')
            else:
                print(sys.argv[2]+' already exists for user: '+getpass.getuser()+ ', and will run once at next system reboot.')

        if sys.argv[1] == "-remove":
            if os.path.exists('/opt/TorrlientVM/'+getpass.getuser()+'.'+sys.argv[2]+'.tdb') == True:
                os.remove('/opt/TorrlientVM/'+getpass.getuser()+'.'+sys.argv[2]+'.tdb')
                print(sys.argv[2]+' has been removed for user: '+getpass.getuser())

        if sys.argv[1] == "-run":
            run = os.listdir('/opt/TorrlientVM/')
            torun = []
            for r in range(len(run)):
                if getpass.getuser() and "tdb" in run[r].split('.'):
                    torun.append(open('/opt/TorrlientVM/'+run[r], 'r').read())

            for run in range(len(torun)):
                if os.getcwd() != "/home/"+getpass.getuser():
                    os.chdir('/home/'+getpass.getpass())
                
                if "php" in torun[run].split('.'):
                    os.system('php '+torun[run]+' > /dev/null 2>&1 &')
                if "py" in torun[run].split('.'):
                    os.system('python3 '+torun[run]+' > /dev/null 2>&1 &')
                if "sh" in torun[run].split('.'):
                    os.system('./'+torun[run]+' > /dev/null 2>&1 &')

                os.remove('/opt/TorrlientVM/'+getpass.getuser()+'.'+torun[run]+'.tdb')
        
        if sys.argv[1] == "-telemetry":
            if os.path.exists('/opt/TorrlientVM/telemetry') == False:
                open('/opt/TorrlientVM/telemetry', 'w').write('1')
                os.chmod('/opt/TorrlientVM/telemetry', 0o777)
                print('Telemetry: Activated')
            else:
                os.remove('/opt/TorrlientVM/telemetry')
                print('Telemetry: Deactivated')

    else:
        print('We are the Creative, the Innovative, and the Creators.')
