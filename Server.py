from libs.encoding import mod2div, calc_entropy
from libs.hashing import calculateSHA256

import socket, json, base64


# Error detection 
def handleClient(decoded_mes,key):
    remainder = mod2div(decoded_mes, key)
    if (remainder == '0' * (len(key) - 1)) :
        print("No errors detected.")
    else:
        print("Errors detected.")


# Final Error percentage calculator
def calculateErrorCount(original_data, received_data):
    error_count = 0
    for bit1, bit2 in zip(original_data, received_data):
        if bit1 != bit2:
           error_count += 1
    return error_count


#the main function of the code 
def runServer():
    #define the host address and port of the server
    host = socket.gethostname()
    port = 8081
	#initiate the socket and bind it
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on {}:{}".format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print("Client connected from:", addr)
        #Retrieve JSON as dictionary from client
        serverInput = json.loads(client_socket.recv(2**20).decode('UTF-8'))#define serverInput
        
        encoded_mes = serverInput["encoded_message"].encode("ASCII")# assign values to encoded_mes
        decoded_mes = base64.b64decode(encoded_mes).decode("ASCII")# decode it

        key = ''.join(serverInput["parameters"])# define key 
        original_sha256 = serverInput["SHA256"]#pass the original sha256 hashed message
        original_mes = serverInput["original_message"]# pass original message for comparison 
        handleClient(decoded_mes, key)
        error_count = calculateErrorCount(original_mes, decoded_mes)

        print("Decoded Message: ", decoded_mes)
        print("The Cyclic Redundancy Code prevented ",serverInput["errors"] - error_count," errors")
        print("Final SHA256: ", str(calculateSHA256(decoded_mes)))
        print("Hashes match? ", original_sha256 == calculateSHA256(decoded_mes))
        print("Start Entropy: ", serverInput["entropy"])
        print("Final Entropy: ", calc_entropy(decoded_mes))
        print("\n")
        

    server_socket.close()

runServer()