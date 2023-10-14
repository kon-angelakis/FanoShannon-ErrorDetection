# FanoShannon-ErrorDetection
A socket application which utilizes the Fano-Shannon compression algorithm as well as the CRC(Cyclic Redundancy Check) on a text file. Its purpose to detect errors on the compressed file after undergoing some user input noise(errors).

### The client:

- Reads the input file (text.txt).  
- Compresses it using the Fano-Shannon compression algorithm.  
- Adds error detection codes to the data (crc).  
- Introduces random errors based on a user-defined percentage.  
- Sends a JSON file to the server with the compressed data, error correction parameters, error information, SHA256 hash, and entropy.  

### The server:

- Receives the JSON from the client.
- Decodes the data using Fano-Shannon compression and the provided error correction parameters.
- Checks and detects errors.
- Calculates the SHA256 hash of the decoded message.
- Compares the calculated hash with the original hash.
- Calculates the entropy of the final message.
- Shows results to user.
