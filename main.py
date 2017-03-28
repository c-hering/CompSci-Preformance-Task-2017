import os, sys, glob, time

exit = False

def print_options():
    print("OPTIONS: \n      do -x :: x=system command ex. do -x dir\n     scan -f -s :: f=folder to scan ex. scan -f Users, s=single file to scan ex. scan -s blah.txt\n        type exit to exit the progam")

def parse_os_cmd(cmd):
    cmds = cmd.split(" ", 1)
    if cmds[1] == "cd":
        direc = cmds[1].split(" ", 1)
        os.chdir(direc[1])
    else:
        print(os.system(cmds[1]))

def check_line(raw_line):
    mal = False
    keywords = {"maliciouscode", "hack"}
    for word in keywords:
        if word in raw_line.lower():
            mal = True
    return mal

def scan_file(raw):
    mal = False
    fl = raw
    if "scan" in fl:
        file_name = raw.split(" ", 2)
        fl = file_name[2]
    try:
        f = open(fl, "r")
        x = 1
        while f.readline(x):
            #print f.readline(x)
            if check_line(f.readline(x)):
                mal = True
            x = x+1
        if mal:
            print "malicious code detected in file " + f.name
            delete = raw_input("would you like to delete this file? (y/n)").lower()
            if "y" in delete:
                try:
                    f.close()
                    os.remove(fl)
                except Exception:
                    print("oops, looks like that file is being used somewhere else")
        else:
            print "no malicious code detected in file " + f.name
            f.close()
    except Exception:
        print("oops, looks like there is no files named '" + fl + "' in this directory")

def scan_folder(raw):
    folder_name = raw.split(" ", 2)
    os.chdir(folder_name[2])
    for file in glob.glob("*.txt"):
        scan_file(file)

def parse_input(input):
    if "do" in input:
        if input == "do":
            print("Wrong Syntax, type 'help' for help")
        else:
            parse_os_cmd(input)
    elif "exit" in input:
        for x in range(0,15):
            exit_string = "\r" + "Exiting Program" + "." * (x%4) + " " * x
            print exit_string,
            time.sleep(.3)
        sys.exit()

    elif "scan" in  input:
        if input == "scan -f" or input == "scan -s" or input == "scan":
            print("Wrong Syntax, type 'help' for help")
        elif "-s" in input:
            scan_file(input)
        elif "-f" in input:
            scan_folder(input)
    elif "help" in input:
        print_options()
    else:
        print("Command Not Found, Type 'help' for help")

def main():
    print_options()
    while(exit == False):
        input = raw_input(">> ")
        parse_input(input)


main()
