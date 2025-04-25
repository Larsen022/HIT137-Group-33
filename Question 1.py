def adjust_shift(shift): #Define function to a 13 letter wrap
    if shift % 13 == 0: #Check if code does a 360 and ends back on same number
        return shift + 1 #Add 1 if it lands on same value
    return shift #Otherwise leave unchanged

def encrypt_char(c, n, m): #Define fucntion to a set parameters
    if 'a' <= c <='z': #Is character lowercase
        if c <= 'm': #Which half of does the letter belong
            shift = adjust_shift(n * m) #calculate shift
            return chr(((ord(c) - ord('a') + shift) % 13) + ord('a')) #Apply shift to a-m
        else: #If not in a-m it is in n-z
            shift = adjust_shift(n + m) #Calculate shift using n + m
            return chr(((ord(c) - ord('n') - shift) % 13) + ord('n')) #Apply adjust shift
    elif 'A' <= c <= 'Z': #Check if character is uppercase
        if c <= 'M': #Check if it is A-M
            shift = adjust_shift(n) #Calculate shift
            return chr(((ord(c) - ord('A') - shift) % 13) + ord('A')) #Apply shift
        else: #Otherwise it is N-Z
            shift = adjust_shift(m ** 2) #Calculate shift for N-Z
            return chr(((ord(c) - ord('N') + shift) % 13) + ord('N')) #Apply shift
    else: #For non letters leave unchanged
        return c #End encryption 
    
def decrypt_char(c, n, m): #Define encryption reverse and restore 
    if 'a' <= c <= 'z': #Check if lower case
        if c <= 'm': #Is it a-m
            shift = adjust_shift(n * m) #Calculate adjusted 
            return chr(((ord(c) - ord('a') - shift) % 13) + ord('a')) #Apply reverse shift
        else: #otherwise it is n-z
            shift = adjust_shift(n + m) #Calculate shift
            return chr(((ord(c) - ord('n') + shift) % 13) + ord('n')) #Apply reverse shift
    elif 'A' <= c <= 'Z': #Check if it is uppercase
        if c <= 'M': #Check if A-M
            shift = adjust_shift(n) #Calculate and adjust using n
            return chr(((ord(c) - ord('A') + shift) % 13) + ord('A')) #Apply reverse shift
        else: #Otherwise it is N-Z
            shift = adjust_shift(m ** 2) #Calculate and adjust using m
            return chr(((ord(c) - ord('N') - shift) % 13) + ord('N')) #Apply reverse shift
    else: #For non letters, return as it is
        return c #End of function 

def encrypt_text(text, n, m): #Function to encrypt string
    return ''.join(encrypt_char(c, n, m) for c in text) #Apply encrypt_char to each character

def decrypt_text(text, n, m): #Function to decrypt string
    return ''.join(decrypt_char(c, n, m) for c in text) #Return decypted string using decrypt_char

def check_correctness(original, decrypted): #Function to check original to decrypted
    return original == decrypted #Return true if it matches

def main():#Main logic for program
    while True:#loop to ensure correct input
        mode = input("Press e to encrypt, or d to decrypt, or q to quit: ").lower() #Ask user what they want to do 
        if mode in ['e', 'd']:#break loop if valid input enteres
            break #if user presses q
        elif mode == 'q': #print exit msg
            print("Exiting Program") #Display msg
            exit() #exit program 
        else: #If it wasn't valid print invalid 
            print("Invalid input, please type 'e' or 'd'.") #Display msg

    if mode == 'e': #Start encryption
        while True: #start loop for correct input
            try: #Covert input
                n = int(input("Enter value for n (number): ")) #Prompt user for n value
                break #Break if correct
            except ValueError: #Print error if invalid
                print("Invalid input, please enter a whole number for n.") #Display msg
        while True: #Star loop for correct input for m
            try: #Try to convert input to integer
                m = int(input("Enter value for m (number): ")) #Prompt user for value of m
                break #Break if correct
            except ValueError: #Print error if invalid 
                print("Invalid input, please enter a whole number for m.") #Display msg

        with open("raw_text.txt", "r") as f:#Open original
            original_text = f.read() #Check contents
        encrypted = encrypt_text(original_text, n, m) #Call encrypted text
        with open("encrypted_text.txt", "w") as f: #Open encrypted text
            f.write(encrypted) #Write to file
        print("Encryption complete.") #Display msg that encryption is done

        decrypted = decrypt_text(encrypted, n, m) #Make decrypted text
        if check_correctness(original_text, decrypted): #Compare texts to check 
            print("Encryption and Decryption Match.") #Display msg that it is correct
        else: #Otherwise print that it went wrong
            print("Something went wrong.") #Display msg

    elif mode == 'd': #Start decryption
        while True: #Loop until valid input for n is entered
            try: #try using input
                n = int(input("Enter value for n (number): ")) #Prompt user for input
                break  #Break if converstion worked
            except ValueError: #Print error if invalid character entered
                print("Invalid input, please enter a whole number for n.") #Display msg
        while True: #Start loop for valid input of m
            try: #Try using input
                m = int(input("Enter value for m (number): ")) #Prompt user for valid input
                break #Break if converstion worked
            except ValueError: #Print error if invalid character entered 
                print("Invalid input, please enter a whole number for m.") #Display msg

        with open ("encrypted_text.txt", "r") as f: #Open encrypted txt
            encrypted = f.read() #Read text
        decrypted = decrypt_text(encrypted, n, m) #Make decrypt txt
        with open("decrypted_text.txt", "w") as f: #Open decrypt text to write
            f.write(decrypted) #Write to decrypt txt
        print("Decryption finished.") #Display that decryption is done
        
        try: #Try to open original 
            with open("raw_text.txt", "r") as f: #Open raw txt
                original_text = f.read() #Read original again
            if check_correctness(original_text, decrypted): #Compare decrypted with original
                print("Decrypted text matches original") #print that they match
            else: # Or print that there is no original file to check
                print("Decrypted Text does not match original.") #Display msg
        except FileNotFoundError: #If original wasn't found display msg
            print("Original File not found, skipping check.") #Display txt

    else:#If something goes wrong outside of all this
        print("Invalid input.") #Display error msg

if __name__ == "__main__": #Check if script is being run directly 
    main() #Run funtion to start 

    #Letters required being confined to each half of the alphabet as if they could move into another half, it would confuse the script and lead to unreliable decryptions.
