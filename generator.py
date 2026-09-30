import hashlib

def main():
    text = input("Enter a string: ")
    hash_result = hashlib.sha256(text.encode("utf-8")).digest()
    bit_string = "".join(f"{b:08b}" for b in hash_result)

    grid_size = 5
    half_width = (grid_size + 1) // 2
    bit_slice = bit_string[:half_width * grid_size]

    rows = [list(bit_slice[i:i + half_width]) for i in range(0, half_width*grid_size, half_width)]
    print(bit_slice)
    for row in rows:
        row += row[half_width - 2::-1]

if __name__ == "__main__":
    main()