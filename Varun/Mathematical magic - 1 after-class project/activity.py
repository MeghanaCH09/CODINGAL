def  binaryToDec(binaryInput): 
    binary = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, '0100': 4, '0101': 5, '0110': 6, '0111': 7, '1000': 8, '1001': 9, '1010': 10, '1011': 11, '1100': 12, '1101': 13, '1110': 14, '1111': 15}
    resultInteger = 0 

    while len(binaryInput) % 4 !=0: 
        binaryInput = '0' + binaryInput
    
    for i in range(0, len(binaryInput),4):
        segment = binaryInput[i:i+4]
        if segment in binary: 
           resultInteger = resultInteger * 16 + binary[segment]
        else: 
            return ValueError("Invalid binary entry")

binary = input("Input desired binary numeral: ")
print("Decimal equivalent: ",binaryToDec(binary))