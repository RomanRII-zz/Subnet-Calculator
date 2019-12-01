#
#   [0xAA55] RomanRII
#

#INPUT START
def IPInput():
   global IPInput
   print("\n* Enter the IP Address you want to use. Ex: 172.20.0.0 *\n")
   IPInput = input(">> ")
   return IPInput
def CIDRInput():
    global CIDRInput
    print("\n* Input the CIDR you want to use. Range from 8-32 *\n")
    CIDRInput = input(">> /")
    return CIDRInput
def BitsInput():
    global BitsInput
    print("\n* Input the number of bits to borrow from host portion. *\n")
    BitsInput = input(">> ")
    return BitsInput
#INPUT END
#DATA CHECK START
def IPCheck():
        IPAddress = IPInput
        IPAddress = IPAddress.split(".")
        try:
            FirstOctet = IPAddress[0]
            SecondOctet = IPAddress[1]
            ThirdOctet = IPAddress[2]
            FourthOctet = IPAddress[3]
            FirstOctet = int(FirstOctet)
            SecondOctet = int(SecondOctet)
            ThirdOctet = int(ThirdOctet)
            FourthOctet = int(FourthOctet)
        except:
            print("\n !! Invalid IP Address | IP Address Contains An Invalid Character !!\n")
            Main()
        else:
            print("\n[+] IP Address Is Valid. Checking CIDR.       [+]")
def CIDRCheck1():
    CIDR = CIDRInput
    try:
        int(CIDR)
    except:
        print("\n !! Invalid CIDR | CIDR Contains An Invalid Character !!\n")
        Main()
    else:
        print("[+] CIDR Contains Valid Characters | Checking CIDR Range [+]")
    
def CIDRCheck2():
    CIDR = CIDRInput
    CIDR = int(CIDR)
    if CIDR ==0:
        print("\n !! Invalid CIDR | CIDR Is Not In The Accepted Range !!\n")
    if CIDR >=33:
        print("\n !! Invalid CIDR | CIDR Is Not In The Accepted Range !!\n")
    print("[+] CIDR Is In Valid Range | Checking Bits [+]\n")
def BitsCheck1():
    Bits = BitsInput
    try:
        bits = int(bits)
    except:
        print("\n !! Invalid Bits Input | The Bits Inputted Contain Invalid Characters !!\n")
def BitsCheck2():
    Bits = BitsInput

#DATA CHECK END
#DATA ORGANIZATION START
def IPSplit():
    '''
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
    '''
def SubnetClass():
    '''
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
    '''
def DataOrganization():
    print("You hit dataorg")
#DATA ORGANIZATION END
#MAIN START
def Main():
    #GRAB INPUTS
    IPInput()
    CIDRInput()
    BitsInput()
    #CHECK INPUTS
    IPCheck()
    CIDRCheck1()
    CIDRCheck2()
    BitsCheck1()
    BitsCheck2()
    #ORGANIZE DATA
    SubnetClass()
    DataOrganization()
    data = int(input("Enter the loop. Press one"))
    if data == 1:
        Main()
    else:
        print("Peace")
#MAIN END
Main()
