import os
import getpass
passwd=getpass.getpass("Enter Your Password:")
apass="pk"
if passwd != apass:
    print("Password Incorrect ")
    exit()
os.system("tput setaf 1")
print("\tHey Wellcome to my TUI thats makes life simple")
os.system("tput setaf 7")
print ("\t---------------------------------------------")
while True:
    print("""
    press 1: Launch WordPress With MYSQL
    Press 2: Launch Rocket.Chat with MongoDB 
    Press 3: To Exit""")
    ch=input("Enter Your Choice:")
    if int(ch)==1:
        os.system("docker-compose up -d")
        while True:
                print("""
                       Welcome To  WordPress
                       ---------------------
                       Press 1: Get  URL 
                       press 2: See Logs
                       Press 3: Stop Services
                       Press 4: Resume Services
                       Press 5: Go Back
                       Press 6: To Exit""")
                no=input("Enter Your Choice:")
                if int(no)==1:
                    os.system("docker inspect project_wordpressos_1 | grep IPAddress")
                elif int(no)==2:
                    os.system("docker-compose logs")
                elif int(no)==3:
                    os.system("docker-compose stop")
                elif int(no)==4:
                    os.system("docker-compose start")
                elif int(no)==5:
                    break
                elif int(no) == 6:
                    print("Thank YOU for Using WordPress")
                    exit()
                input("Enter To Continue...")
                os.system("clear")
    elif int(ch)==2:
        os.system("docker run --name db -d mongo:4.0 --smallfiles --replSet rs0 --oplogSize 128")
        os.system("docker exec -ti db mongo")
        os.system("docker run --name rocketchat -p 80:3000 --env ROOT_URL=http://localhost --env MONGO_URL=mongodb://mymongourl/mydb --env MONGO_OPLOG_URL=mongodb://mymongourl:27017/local -d rocket.chat")
        while True:
            print("""
                       Welcome To Rocket.chat
                       --------------------
                       Press 1: Get URL 
                       press 2: See Logs
                       Press 3: Stop Services
                       Press 4: Start Services
                       Press 5: Go Back
                       Press 6: To Exit""")
            number=input("Enter Your Choice:")
            if int(number)==1:
                os.system("docker inspect rocket.chat | grep IPAddress")
            elif int(number)==2:
                os.system("docker rocket.chat logs")
            elif int(number)==3:
                os.system("docker stop rocket.chat")
                os.system("docker stop db")
            elif int(number)==4:
                os.system("docker start rocket.chat")
                os.system("docker start db")
            elif int(number)==5:
                break
            elif int(number) == 6:
                print("Thank YOU for Using Rocket.chat")
                exit()
            input("Enter To Continue...")
            os.system("clear")
    elif int(ch) == 3:
        print("Thank YOU for Using TUI Created By PKumar")
        exit()
    else:
        print("Option not Supported")
    input("Enter To Continue...")
    os.system("clear")
