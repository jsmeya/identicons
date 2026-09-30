import hashlib

def main():
    text = str(input("Enter a string: "))
    hash_result = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(hash_result)

if __name__ == "__main__":
    main()