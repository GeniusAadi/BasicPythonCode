#Program to convert octal into decimal then into binary then into hexadecimal
#Function to convert decimal number into octal number
def dec_oct(decimal):
    r=1
    m_r=""
    octal=""
    while r>0:
        r=decimal%8
        m_r+=str(r)
        decimal=(decimal-r)//8
    octal=octal+str(decimal)+m_r[::-1]
    return octal
#Function to convert decimal number into binary number
def dec_bin(decimal):
    r=1
    m_r=""
    binary=""
    while r>0:
        r=decimal%2
        m_r+=str(r)
        decimal=(decimal-r)//2
    binary=binary+str(decimal)+m_r[::-1]
    return binary
#Function to convert decimal number into hexadecimal number
def dec_hex(decimal):
    r=1
    m_r=""
    hexadecimal=""
    while r>0:
        r=decimal%16
        if r==10:
            m_r+="A"
        elif r==11:
            m_r+="B"
        elif r==12:
            m_r+="C"
        elif r==13:
            m_r+="D"
        elif r==14:
            m_r+="E"
        elif r==15:
            m_r+="F"
        else:
            m_r+=str(r)
        decimal=(decimal-r)//16
    if r==10:
        hexadecimal=hexadecimal+"A"+m_r[::-1]
    elif r==11:
        hexadecimal=hexadecimal+"B"+m_r[::-1]
    elif r==12:
        hexadecimal=hexadecimal+"C"+m_r[::-1]
    elif r==13:
        hexadecimal=hexadecimal+"D"+m_r[::-1]
    elif r==14:
        hexadecimal=hexadecimal+"E"+m_r[::-1]
    elif r==15:
        hexadecimal=hexadecimal+"F"+m_r[::-1]
    else:
        hexadecimal=hexadecimal+str(decimal)+m_r[::-1]
    return hexadecimal
#Function to convert binary number into decimal number
def bin_dec(binary):
    decimal=0
    i=0
    while binary>=1:
        r=binary%10
        binary=(binary-r)//10
        decimal+=r*2**i
        i+=1
    return decimal
#Function to convert octal number into decimal number
def oct_dec(octal):
    r=1
    decimal=0
    i=0
    while r>0:
        r=octal%10
        octal=(octal-r)//10
        decimal+=r*8**i
        i+=1
    return decimal
#Function to convert hexadecimal number into decimal number
def hex_dec(hexadecimal):
    hexa=1
    decimal=0
    i=0
    while hexa>0:
        if "A" in hexadecimal:
            hexa=hexadecimal.replace("A","")
            decimal+=10*16**i
        elif "B" in hexadecimal:
            hexa=hexadecimal.replace("B","")
            decimal+=11*16**i
        elif "C" in hexadecimal:
            hexa=hexadecimal.replace("C","")
            decimal+=12*16**i
        elif "D" in hexadecimal:
            hexa=hexadecimal.replace("D","")
            decimal+=13*16**i
        elif "E" in hexadecimal:
            hexa=hexadecimal.replace("E","")
            decimal+=14*16**i
        elif "F" in hexadecimal:
            hexa=hexadecimal.replace("F","")
            decimal+=15*16**i
        r=int(hexa)%10
        hexa=(int(hexa)-r)//10
        decimal+=r*16**(i+1)
        i+=1
    return decimal
#Function to convert binary number into octal number
def bin_oct(binary):
    octal=""
    while binary>0:
        r=binary%1000
        binary=(binary-r)//1000
        decimal=0
        for i in range(3):
            rr=r%10
            r=(r-rr)//10
            decimal+=rr*2**i
        octal+=str(decimal)
    return octal[::-1]
#Function to convert binary number into octal number
def bin_hex(binary):
    hexadecimal=""
    while binary>0:
        r=binary%10000
        binary=(binary-r)//10000
        decimal=0
        for i in range(4):
            rr=r%10
            r=(r-rr)//10
            decimal+=rr*2**i
        if decimal==10:
            hexadecimal+="A"
        elif decimal==11:
            hexadecimal+="B"
        elif decimal==12:
            hexadecimal+="C"
        elif decimal==13:
            hexadecimal+="D"
        elif decimal==14:
            hexadecimal+="E"
        elif decimal==15:
            hexadecimal+="F"
        else:
            hexadecimal+=str(decimal)
        #print("octal value after adding",octal)
    return hexadecimal[::-1]
#For decimal to octal and vise versa
decimal=int(input("Enter decimal number: "))
octal=int(dec_oct(decimal))
print("Octal value: ",octal)
ans=oct_dec(octal)
print("Decimal value: ",ans,"\n")
#For decimal to binary and vise versa
binary=int(dec_bin(decimal))
print("Binary value: ",binary)
ans=bin_dec(binary)
print("Decimal value: ",ans,"\n")
#For decimal to hexadecimal and vise versa
hexadecimal=dec_hex(decimal)
print("Hexadecimal value: ",hexadecimal)
ans=hex_dec(hexadecimal)
print("Decimal value: ",ans,"\n")
#For binary to octal and vise versa
octal=int(bin_oct(binary))
print("Binary to Octal value: ",octal)
ans=oct_dec(octal)
print("Decimal value: ",ans,"\n")
#For binary to hexadecimal and vise versa
hexadecimal=bin_hex(binary)
print("Binary to Hexadecimal value: ",hexadecimal)
ans=hex_dec(hexadecimal)
print("Decimal value: ",ans,"\n")