#import area
import time #for time.sleep
import msvcrt #for check pressed
import os #for clear cmd
import random #for random item, like random delay

#value area
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

install_time = 10.0

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
    #print("") #Stop printing at same line --replaced by next line
    os.system('cls')

if boot_key_pressed == True: #Main setup

    if True: #Select language setting
        print("Select language setting")
        print("Language to install:      English")
        print("Time and currency format: Earth")
        choice = input("Next?").upper()
        os.system('cls')

    if True: #Select keyboard setting
        print("Select keyboard setting")
        print("Keyboard of input method: English")
        choice = input("Next?").upper()
        os.system('cls')

    if True: #Select setup option
        while True:
            print("Select setup option")
            print("Install the latest version of Windows11, or repair your PC. If you're installing Windows11, please note your files, apps, and setting will be deleted.")
            print("I would like to A. Install Windows 11")
            print("                B. Repair my PC")
            install_choice = input("A or B").upper()
            if install_choice == "A":
                break
            elif install_choice == "B":
                print("Repair my PC is not supported")
                time.sleep(1)
                os.system('cls')
            else:
                print("Please enter A or B")
                time.sleep(1)
                os.system('cls')

    if True: #Agree Del items
        print("I agree everything will be deleted including files, apps, and setting")
        choice = input("Do you agree? (Y/N)").upper()
        os.system('cls')
    
    if True: #Product Key
        print("Product Key")
        print("The product key should be with the box the DVD came in or on your email receipt.")
        print("It looks similar to this: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
        print("Press Enter for no product key")
        print("Enter product key")
        choice = input()
        while True:
            if choice == "":
                #press "Enter" / "Leave Blank"
                os.system('cls')
                break
            else:
                #wrong Key
                print("This is not a valid key")
                time.sleep(3)
                os.system('cls')
                print("Product Key")
                print("The product key should be with the box the DVD came in or on your email receipt.")
                print("It looks similar to this: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
                print("Press Enter for no product key")
                print("Enter product key")
                choice = input()

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
                sku_choose_sure = input(f"Are you sure you want to install {sku[sku_choose_number]} ? (Y/N)").upper()
                if sku_choose_sure == "Y":
                    sku_choose_type = sku[sku_choose_number]
                    sku_choose_yet = True
                    break
                else:
                    os.system('cls')
            except ValueError:
                print("Please Input a No.")
                time.sleep(1)
                os.system('cls')

    if True: #Install
        while install_time > 0:
            print(f"Installing {sku_choose_type}")
            time.sleep(random.uniform(0.1, 1.0))
            os.system('cls')
            print(f"Installing {sku_choose_type}.")
            time.sleep(random.uniform(0.1, 1.0))
            os.system('cls')
            print(f"Installing {sku_choose_type}..")
            time.sleep(random.uniform(0.1, 1.0))
            os.system('cls')
            print(f"Installing {sku_choose_type}...")
            time.sleep(random.uniform(0.1, 1.0))
            install_time -= random.uniform(0.5, 1.0)
            os.system('cls')

    if True: #OOBE
        print("in dev, not yet")
        #oobe, later

else: #Fake PXE Boot
    os.system('cls')
    print("Start PXE over IPv4...")
    time.sleep(1)
    print("  Media test failure, check cable")
    time.sleep(2)
    print("  Exiting PXE ROM")
    time.sleep(1)
    print("No bootable device -- insert boot disk and press any key")
    input()
    exit()

#v4.9
#Coder: Pierre