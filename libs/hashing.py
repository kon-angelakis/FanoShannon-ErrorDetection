import hashlib

def calculateSHA256(msg):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(msg.encode('utf-8'))
    return sha256_hash.hexdigest()