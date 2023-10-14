from libs.FanoShannon import FanoShannon
from libs.encoding import encodeData, calc_entropy
from libs.hashing import calculateSHA256

import socket, random, json, base64

GEN_POLYNOMIAL = "10011" #Generator polynomial


# applies a error_count errors in encoded data (not probabilistic)
def populateErrors(data, error_count):
    for i in range(error_count):
        rnd = random.randint(0,len(data)-1)
        if data[rnd] == '1':
            data[rnd] = 0
        else:
            data[rnd] = 1
    return (''.join([str(elem) for elem in data]))


def main():
    
    compressed_data = FanoShannon()
    
    #connect to the server 
    s = socket.socket()
    port = 8081
    s.connect((socket.gethostname(), port))

    error_perc = float(input("Enter Error Percentage(%) -> "))
    data = compressed_data.strip()


    #encode the compressed data using the crc algorithm
    encoded_data = encodeData(data, GEN_POLYNOMIAL)
    start_entropy = calc_entropy(encoded_data)
    original_encoded_data = encoded_data #keep the original encoding here as a temp
    error_count = int(len(encoded_data)*error_perc/100)
    binary_list = list(encoded_data) # encoded_data is a string and here is its list

    #After errors are added encode into base64
    encoded_data = populateErrors(binary_list, error_count)
    b64_encoded_data = base64.b64encode(encoded_data.encode("ASCII"))
    b64_encoded = b64_encoded_data.decode("ASCII")

    #Server input using a JSON file
    data = { 
        "original_message": original_encoded_data,
        "encoded_message": b64_encoded,
        "compression_algorithm": "fano-shannon",
        "encoding": "cyclic",
        "parameters": [GEN_POLYNOMIAL],
        "errors": error_count,
        "SHA256": calculateSHA256(original_encoded_data),
        "entropy": start_entropy
    }
    json_data=json.dumps(data)
    
    s.send(json_data.encode("UTF-8")) #parse JSON file to server

    input("Press any key to continue..")

    s.close()


main()