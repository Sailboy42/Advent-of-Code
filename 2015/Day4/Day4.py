import hashlib

secret_key = "bgvyzdsv"
secret_key_example = "abcdef"
req_start_1 = "00000"
req_start_2 = "000000"

def custom_hex(key, start_hex):
    """_summary_

    Args:
        key (_type_): _description_
        start_hex (_type_): _description_
    """
    counter = 0
    while True:
        str2hash = f"{key}{counter}"
        result_hex = hashlib.md5(str2hash.encode()).hexdigest()
        if result_hex.startswith(start_hex):
            print(counter)
            break
        counter += 1

custom_hex(secret_key, req_start_1)
custom_hex(secret_key, req_start_2)
