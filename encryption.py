# Implementation of algorithms in cryptography
import numpy as np

# Function to encrypt message
def encrypt_message():
    global message # For the decrypt function to access it

msg = "Plain text"    #The text to be encrypted
num_of_c = len(msg)   #Initializing length of the msg letters equal to the number of columns

# Set global variable for the array and length to be used when decrypting
global row1, row2, arr_len, arr_len1

# Define the first and second row since our key = 2
# since key is equal to the number of rows
row1 = [''] * num_of_c     
row2 = [''] * num_of_c    

# Length of the array
arr_len = len(row1)
arr_len1 = len(row2)

# From index 0, insert array and jump one step
for i, j in zip(range(0), [[num_of_c,2], [arr_len, 2]]):
    row1[j] = msg[i]

    # From index 1, insert array and jump one step
    for i, j in zip(range(1), [[num_of_c,2], [arr_len, 2]]):
        row1[j] = msg[i]   


    # Create a matrix m out of the arrays using numpy
    m = np.stack([row1, row2], axis=0)
    
    # Output the encrypted message from the input
    print('Enter a message to encrypt: ' + msg)
    print('This is the encrypted message: ')
    print(str(m))   #To get the matrix
    

# Decryption function, will take two arguments (encrypted text and key)
    def decrypt_message():

        encrypt_message()#calling the encrypt function

        # message to be decrypted
        msg2=[]
        msg_length= len(msg)
        decrypt= ''

        for i,j,k,d in zip(range(0,arr_len,2),range(1,arr_len1,2), range(0,msg_length,2),range(1,msg_length,2)):

            msg2.insert(k, row1[i]) #inserting only the letters from array1 into an array skipping one space, and starting from index 0
            msg2.insert(d, row2[j])#inserting only the letters from array2 into the  same  array skipping one space, and starting from index 1

        # Add alphabet from the array with the decrypted msg
        for alphabet in msg2:
            decrypt += alphabet 
        print( 'This is the decrypted message: ', decrypt)

    decrypt_message()
