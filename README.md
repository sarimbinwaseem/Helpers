Kill Processes.ps1: Kill list of processes from PowerShell.

main.py: Block EXEs from accessing internet via Firewall settings rule.

## Kill Processes:
1. Edit Kill Processes.ps1 and change the list to the desired application exe names.

1.1 You can get exe name from task manager while program is running where you can
right click and select details and then copy name.

## Block Internet:
1. Copy folder path where EXEs are located and pass it in -p argument.
2. Pass recognizable name to -n.
3. Run ```bash
 python block-exes.py -p "C:\Program Files\Program" -n "The Program"
``` 

It will recurse the directory to the deepest and block all EXEs present.

## Backup Call Recordings to Linux using ADB:
1. Enable USB Debugging on the phone.
2. Attach Android phone to Bash enabled system.
3. Modify the backup location in the pullcalls.sh script.
4. Run pullcalls.sh

# Disclaimer: 
Use at your own risk and I am not responsible for any illegal use of any scripts.
