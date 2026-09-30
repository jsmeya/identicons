import hashlib

def main():
    text = str(input("Enter a string: "))
    hash_result = hashlib.sha256(text.encode("utf-8")).digest()
    bit_string = "".join(f"{b:08b}" for b in hash_result)
    print(bit_string)

if __name__ == "__main__":
    main()