Kill Processes.ps1: Kill list of processes from PowerShell.

main.py: Block EXEs from accessing internet via Firewall settings rule.

## Kill Processes
1. Edit Kill Processes.ps1 and change the list to the desired application exe names.

1.1 You can get exe name from task manager while program is running where you can
right click and select details and then copy name.

## Block Internet
1. Copy folder path where EXEs are located and pass it in -p argument.

It will recurse the directory to the deepest and block all EXEs present.
