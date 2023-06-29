# import os
import subprocess
import argparse
import pathlib

def Rule(appname, dispName, domain, bound, description, name):
	command = f"New-NetFirewallRule -Program {appname} -Action Block -Profile Domain, {domain} -DisplayName {dispName} -Description {description} -Direction {bound}"
	# command = command.split()
	e = subprocess.run(["powershell", "-Command",command], capture_output=True)
	if str(e.returncode) == "1":
		eLog = appname + f" is not blocked | {bound} | {domain}" 
		print(eLog)
		print(e.stderr)
		with open(f"{name}.txt", "w+") as log:
			log.write(eLog)
	elif str(e.returncode) == str(0):
		print(f"{appname} is blocked | {bound} | {domain}")
	else:
		print("Unidentified Error!")


def work(folder, name):
	# with open(f"{name}.txt", "w+") as log:
	# 	log.write("These paths are not blocked:")

	description = dispName = ""
	# if not os.path.isdir(folder):
	# 	return -1

	# else:
		# for root, dirs, files in os.walk(folder, topdown = False):
		# 	for file in files:
		# 		if file[-3:].lower() == "exe":
		# 			appname = os.path.join(root, file)
		# 			appname = f"\"{appname}\""
		# 			print(appname)
		# 			description = dispName = f"\"{name} - {file}\""
					
		# 			domain = "Private"
		# 			bound = "Inbound"
		# 			Rule(appname, dispName, domain, bound, description, name)
		# 			bound = "Outbound"
		# 			Rule(appname, dispName, domain, bound, description, name)
		# 			domain = "Public"
		# 			bound = "Inbound"
		# 			Rule(appname, dispName, domain, bound, description, name)
		# 			bound = "Outbound"
		# 			Rule(appname, dispName, domain, bound, description, name)
					
		# 			print()

	folderpath = pathlib.Path(folder)

	if not folderpath.is_dir():
		return -1

	else:
		for file in folderpath.rglob("*.[eE][xX][eE]"):
			appname = f"\"{file}\""
			print(appname)
			description = dispName = f"\"{name} - {file}\""
					
			domain = "Private"
			bound = "Inbound"
			Rule(appname, dispName, domain, bound, description, name)
			bound = "Outbound"
			Rule(appname, dispName, domain, bound, description, name)
			domain = "Public"
			bound = "Inbound"
			Rule(appname, dispName, domain, bound, description, name)
			bound = "Outbound"
			Rule(appname, dispName, domain, bound, description, name)
			
			print()

	return 0

def check(data):
	if type(data) is int:
		raise argparse.ArgumentTypeError("Invalid Argument, add a string path")
	else:
		return data

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

	res = work(folder, name)
	if res == 0:
		print("All EXEs are blocked.")

	elif res == -1:
		print("Supplied folder path is not a valid folder.")

	# python main.py -p C:\Program Files\Adobe\Illustrator -n "Adobe Illustrator"
	
