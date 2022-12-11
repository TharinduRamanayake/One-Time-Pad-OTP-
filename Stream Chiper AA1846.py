#AA1846

def main():
    cont=True
    select=""
    print("The key must be less than or equal to plaintext in length\n")
    print("Plaintext must not contain numbers.")
    print("\nSelects:1\n1: Encode\n2: Quit")
    while cont == True:
        select = input(">>> ")
        if select == "1":
            print("Your Ciphertext is " + encode(input("Please enter your plaintext: "), input("Please enter your key: ")))

        elif select == "2":
            cont = False

        else:
            print("Please choose 1 or 2")


def characterToNumber(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = 1
    for letter in alphabet:
        if letter == char:
            break
        else:
            num+=1
    return num


def numberToCharacter(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num+1]

def encodeCharacter(pText, key):
    cNum = ( characterToNumber(pText) + characterToNumber(key) ) % 26
    cText = numberToCharacter(cNum)
    return cText

def encode(pText, key):
    cText= ""
    for i in range(0, len(pText)):
        cText += encodeCharacter(pText[i], key[i])

    return cText


main();