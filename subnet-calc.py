#################################################################
#								#
#		Usage: python3 subnet_calc.py			#
#		RomanRII's Subnet Calculator			#
#								#
#################################################################

# Vars:
#      Vars: var1 = InitIP | address = var1 split by '.' |
#      Octets:	fo1 = first octet | so = second octer | to = third octet | fo2 = fourth octet

#TODO
#	Fix Bits Section
#	Add Calculator
#	Make data beautiful


import math

def IPInput():
	#GET INIT IP
	print("\n* Enter the IP Address you want to use. Ex: 172.20.0.0 *\n")
	var1 = input(">> ")
	return var1

def CIDRInput():
	print("\n* Input the CIDR you want to use. Range from 8-32 *\n")
	CIDR = input(">> /")
	return CIDR
def BitsInput():
	print("\n* Input the number of bits to borrow from host portion. *\n")
	bits = input(">> ")
	return bits

def BitCheck():
	bits = BitsInput()
	try:
		bits = int(bits)
	except:
		print("\n !! Invalid number for bits. Please enter valid number. !!\n")
		BitsInput()
		bits = 1
	else:
		return bits

def IPSplit():
	#IMPORTS VAR1 FROM IPInput()
	var1 = IPInput()
	CIDR = CIDRInput()
	bits = BitCheck()
	#SPLITS var1 INTO 4 OCTETS
	address = var1.split(".")
	#ASSIGNS OCTETS A VARNAME AND CONVERTS TO INTEGER
	try:
		fo1 = address[0]
		so = address[1]
		to = address[2]
		fo2 = address[3]
		fo1 = int(fo1)
		so = int(so)
		to = int(to)
		fo2 = int(fo2)
		CIDR = int(CIDR)
	except:
		print("\n !! Invalid IP or CIDR | Failed IP/CIDR Validity Check !!\n")
		IPInput()
	else:
		print("\n[+] IP and CIDR are valid. Checking range.      [+]")
		return fo1, so, to, fo2, CIDR, bits

def RangeCheck():
	fo1, so, to, fo2, CIDR, bits = IPSplit()
	#OCTET RANGE CHECK START	If octet1 is LTOET 0 or octet1-4 MTOET 255 trip Invalid IP
	if fo1 ==0:
		print("!! Invalid IP Address | First Octet cannot be 0 !!\n")
	if fo1 >=256:
		print("!! Invalid IP Address | First Octet cannot more than 255 !!\n")
	if so >=256:
		print("!! Invalid IP Address | Second Octet cannot be more than 255 !!\n")
	if to >=256:
		print("!! Invalid IP Address | Third Octet cannot be more than 255 !!\n")
	if fo2 >=256:
		print("!! Invalid IP Address | Fourth Octet cannot be more than 255 !!\n")
	#OCTET RANGE CHECK END
	print("[+] IP range is valid. Checking CIDR range.     [+]")
	if CIDR ==0:
		print("!! Invalid CIDR Range | CIDR must be between 1-32 !!\n")
	if CIDR >=33:
		print("!! Invalid CIDR Range | CIDR must be between 8-32 !!\n")
	print("[+] CIDR range is valid. Assigning Subnet Class.[+]")
	return fo1, so, to, fo2, CIDR, bits


def SubnetClass():
	fo1, so, to, fo2, CIDR, bits = RangeCheck()
	subnetClass = " "
	#DETERMINES WHICH SUBNET CLASS THE IP BELONGS TO
	if fo1 >= 1 and fo1 <= 127:
		subnetClass = "Class A"
	if fo1 >= 128 and fo1 <= 191:
		subnetClass = "Class B"
	if fo1 >= 192 and fo1 <= 223:
		subnetClass = "Class C"
	if fo1 >= 224 and fo1 <= 239:
		subnetClass = "Class D"
	if fo1 >= 240 and fo1 <= 254:
		subnetClass = "Class E"
	return fo1, so, to, fo2, CIDR, subnetClass, bits

def IPAddress():
	fo1, so, to, fo2, CIDR, subnetClass, bits = SubnetClass()
	fo1 = str(fo1)
	so = str(so)
	to = str(to)
	fo2 = str(fo2)
	CIDR = str(CIDR)
	bits = str(bits)
	IPAddy = fo1+"."+ so+"."+ to+"."+ fo2
	return IPAddy, CIDR, subnetClass, bits

def DataOrganization():
	IPAddy, CIDR, subnetClass, bits = IPAddress()
	print("\n * Here is the calculation for your subnet *\n")
	print("IP Address: ",IPAddy)
	print("CIDR: ",CIDR)
	print("Subnet Class: ",subnetClass)
	print("Bits borrowed: ", bits)

DataOrganization()
