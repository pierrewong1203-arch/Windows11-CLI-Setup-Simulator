#import area
import time #for time.sleep
import msvcrt #for check pressed
import os #for clear cmd
import random #for random item, like random delay

#value area

timer = 0

boot_timer = 5
boot_key_pressed = False

#User choice / input
choice = ""
install_choice = ""

#Install info -sku
sku_choose_yet = False
sku_choose_number = 0
sku_choose_number_str = "0"
sku_choose_sure = "N"
sku_choose_type = "" #home or pro or edu or...... (sku type)
sku = ["Windows 11 Home","Windows 11 Home Single Language","Windows 11 Pro","Windows 11 Pro for Workstations","Windows 11 Education","Windows 11 Pro Education","Windows 11 Enterprise","Windows 11 IoT Enterprise","Windows 11 Enterprise multi-session","Windows 11 Enterprise LTSC 2024","Windows 11 IoT Enterprise LTSC 2024","Windows 11 IoT Enterprise Subscription LTSC 2024","Windows Server 2025 Standard Core","Windows Server 2025 Standard (Desktop Experience)","Windows Server 2025 Datacenter Core","Windows Server 2025 Datacenter (Desktop Experience)"]

install_time = 0

def cls(): #simple clean output
    os.system('cls')

def yes_no_question(yn_question="Next", custom_whole_question=False):
    if custom_whole_question == False:
        print(f"{yn_question}? (Y/N)")
    else:
        print(yn_question)
    print("N will exit whole setup.")
    while True:
        key = msvcrt.getch().upper()
        if key == b'Y':
            break
        elif key == b'N':
            exit()

def enter_agree():
    while True:
        if msvcrt.getch() == b'\r':
            break

#warning
print("This is a similator.")
print("This will not change any item in your computer.")
time.sleep(3)
yes_no_question("Press Y To Continue", True)
cls()

if True: #First screen: boot from cd or dvd (.iso)
    print("Press any key to boot from CD or DVD", end="" , flush=True)
    while boot_timer >= 0:
        print(".", end="", flush=True) #add dot
        time.sleep(1)
        if msvcrt.kbhit(): #check if pressed anything
            boot_key_pressed = True
            break
        else:
            boot_timer -= 1
    cls()

if boot_key_pressed == True: #Main setup

    #Setup exe

    if True: #Select language setting
        print("Select language setting")
        print("Language to install:      English")
        print("Time and currency format: Earth")
        yes_no_question()
        cls()

    if True: #Select keyboard setting
        print("Select keyboard setting")
        print("Keyboard of input method: English")
        yes_no_question()
        cls()

    if True: #Select setup option
        while True:
            print("Select setup option")
            print("Install the latest version of Windows11, or repair your PC. If you're installing Windows11, please note your files, apps, and setting will be deleted.")
            print("I would like to A. Install Windows 11")
            print("                B. Repair my PC")
            install_choice = input("A or B").upper()
            if install_choice == "A":
                cls()
                break
            elif install_choice == "B":
                print("Repair my PC is not supported")
                time.sleep(1)
                cls()
            else:
                print("Please enter A or B")
                time.sleep(1)
                cls()

    if True: #Agree Del items
        print("I agree everything will be deleted including files, apps, and setting")
        yes_no_question("Do you agree")
    
    if True: #Product Key
        print("Product Key")
        print("The product key should be with the box the DVD came in or on your email receipt.")
        print("It looks similar to this: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
        print("Press Enter for no product key")
        print("Enter product key")
        choice = input()
        while True:
            if choice == "": #press "Enter" / "Leave Blank"
                cls()
                break
            else: #wrong key
                print("This is not a valid key")
                time.sleep(3)
                cls()
                print("Product Key")
                print("The product key should be with the box the DVD came in or on your email receipt.")
                print("It looks similar to this: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
                print("Press Enter for no product key")
                print("Enter product key")
                choice = input()
        cls()

    if True: #Choose ver. & spam trash info
        while True:
            print("Select Image")
            print("Please select image you want to install.")
            print("Operating System:")
            print(f"1. {sku[0]}")
            print(f"2. {sku[1]}")
            print(f"3. {sku[2]}")
            print(f"4. {sku[3]}")
            print(f"5. {sku[4]}")
            print(f"6. {sku[5]}")
            print(f"7. {sku[6]}")
            print(f"8. {sku[7]}")
            print(f"9. {sku[8]}")
            print(f"10. {sku[9]}")
            print(f"11. {sku[10]}")
            print(f"12. {sku[11]}")
            print(f"13. {sku[12]}")
            print(f"14. {sku[13]}")
            print(f"15. {sku[14]}")
            print(f"16. {sku[15]}")
            print("")
            print("Insert the no. to choose")
            sku_choose_number_str = input()
            try:
                sku_choose_number = int(sku_choose_number_str)
                sku_choose_number -= 1
                print(f"Are you sure you want to install {sku[sku_choose_number]} ? (Y/N)").upper()
                while True:
                    sku_choose_sure = msvcrt.getch().upper()
                    if sku_choose_sure == b'Y':
                        break
                    if sku_choose_sure == b'N':
                        break
                if sku_choose_sure == b'Y':
                    sku_choose_type = sku[sku_choose_number]
                    sku_choose_yet = True
                    break
                else:
                    cls()
            except ValueError:
                print("Please Input a No.")
                time.sleep(1)
                cls()

    if True: #Install
        while True:
            install_time += random.randint(1,5)
            if install_time > 100:
                install_time = 100
            print("Installing Windows 11")
            print("Your PC will restart several times. This might take a while.")
            print(f"{install_time}% complete")
            time.sleep(random.uniform(0.2, 5.0))
            cls()
            if install_time >= 100:
                break
        print("Installing Windows 11")
        print("Your PC will restart several times. This might take a while.")
        print("Your PC will restart in a few moments")
        time.sleep(random.randint(1,5))
      
    if True: #Cointry or Region
        print("Is this the right country or region?")
        print("")
        print("Earth")
        choice = input("Yes")
        cls()

    #oobe

    if True: #Keyboard
        print("Is this the right keyboard layout or input method?")
        print("If you also use another keyboard layout, you cann add that next")
        print("US")
        choice = input("Yes")
        cls()

    if True: #2nd keyboard
        print("Want to add a second keyboard layout?")
        print("Press enter to Skip, Type 'Add' to add layout.")
        choice = input()
        cls()
        if choice == 'Add':
            timer = 4
            while timer >=0:
                timer -= 1
                print("What language do you want to use for your second keyboard layout?")
                print("Not yet supported by this python script")
                print(f"Auto skip in {timer} second(s).")
                cls()

    if True:
        print("4.12 only till here, later still in dev, or I should say 'The other part not born yet. :)' ")

else: #Fake PXE Boot
    cls()
    print("Start PXE over IPv4...")
    time.sleep(1)
    print("  Media test failure, check cable")
    time.sleep(2)
    print("  Exiting PXE ROM")
    time.sleep(1)
    print("No bootable device -- insert boot disk and press any key")
    input()
    exit()

#v4.12
#Coder: Pierre
