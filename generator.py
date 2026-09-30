import hashlib

def main():
    text = input("Enter a string: ")
    hash_result = hashlib.sha256(text.encode("utf-8")).digest()
    bit_string = "".join(f"{b:08b}" for b in hash_result)

    grid_size = int(input("Enter a grid size (n) for (n x n): "))
    half_width = (grid_size + 1) // 2
    bit_slice = bit_string[:half_width * grid_size]

    rows = [list(bit_slice[i:i + half_width]) for i in range(0, half_width*grid_size, half_width)]
    for row in rows:
        row += row[half_width - 2::-1]
        print(f"{" ".join("■" if bit == "1" else " " for bit in row)}")

if __name__ == "__main__":
    main()