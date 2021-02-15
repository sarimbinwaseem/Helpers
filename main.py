import os
import os
import subprocess
import argparse

def check(data):
	if str(type(data)) == "<class 'int'>":
		raise argparse.ArgumentTypeError("Invalid Argument, add a string path")
	else:
		return data

def work(folder, name):
	description = dispName = ""
	count = 0
	if os.path.isdir(folder):
		for root, dirs, files in os.walk(folder, topdown = False):
			for file in files:
				if file[-3:] == "exe":
					appname = os.path.join(root, file)
					appname = f"\"{appname}\""
					print(appname)
					description = dispName = f"\"{name} - {file}\""

					# Outbound Rule
					command = f"New-NetFirewallRule -Program {appname} -Action Block -Profile Domain, Private -DisplayName {dispName} -Description {description} -Direction Outbound"
					# command = command.split()
					e = subprocess.run(["powershell", "-Command",command], capture_output=True)
					if str(e.returncode) == "1":
						print(appname + " is not blocked | Outbound")
						print(e.stderr)
					elif str(e.returncode) == str(0):
						print(f"{appname} is blocked | Outbound")
					else:
						print("Unidentified Error!")

					# Inbound Rule
					command = f"New-NetFirewallRule -Program {appname} -Action Block -Profile Domain, Private -DisplayName {dispName} -Description {description} -Direction Inbound"
					e = subprocess.run(["powershell", "-Command",command], capture_output=True)
					if str(e.returncode) == "1":
						print(appname + " is not blocked")
						print(e.stderr)
					elif str(e.returncode) == str(0):
						print(f"{appname} is blocked | Inbound")
					else:
						print("Unidentified Error!")
					count += 1
					print()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Block folder of EXEs from accessing Internet.")
	
	parser.add_argument("-p", "--path", help = "Add path to the folder where EXEs are located",
		type = check, required = True)
	
	parser.add_argument("-n", "--name", help = "Add name to display in Firewall.",
		type = check, required = True)
	
	args = parser.parse_args()
	folder = args.path
	name = args.name
	work(folder, name)

	