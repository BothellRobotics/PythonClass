#1 0 1 1 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0

#length = 4

#binum[0] = 1
#binum[1] = 0
#binum[2] = 1
#binum[3] = 1


#Assign user entered value into a String binaryNumber
binaryNumber = input("Please enter a binary number to convert to Decimal Number")

print(binaryNumber)

#Get the length of user entered binary Number and assign to a variable length
length = len(binaryNumber)

#Start converting Right most Binary Number to Decimal Number and move towards Left
#Start basePower = 0 and increment by 1 as you move from Right to Left
#Keep appending the converted values to the result
#Exit the Loop once you reach the Left most number in the Binary

decimalValue = 0
basePower = 0
#While the length is greater than 0
while length > 0:
	#binaryNumber = Start last element in the array binaryNumber[Length -1] and assign it to binaryNumber
    binaryElement = binaryNumber[length - 1]

    #Make sure the user entered value does not contain anything other than 0 and 1
    if binaryElement != '1' and binaryElement != '0':
        raise Exception('Only 1 and 0 are allowed in Binary Number. User entered value contains {}'.format(binaryElement))

	#DeciValue = DeciValue + BiValue * 2**BasePower
    decimalValue = decimalValue + int(binaryElement) * (2 ** basePower)

	#BasePower = BasePower + 1
    basePower = basePower + 1

	#Legth = Length - 1
    length = length - 1

print('Decimal Value of binary number: ' + binaryNumber + ' = {}'.format(decimalValue))
