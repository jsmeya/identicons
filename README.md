# identicon
A simple identicon generator inspired by GitHub's default profile pictures.

## How it works
1. Hashes your input string with SHA-256 and converts the digest into a 256-bit string.
2. Slices off enough bits to fill the left half (plus the middle column) of an `n x n` grid.
3. Mirrors each row horizontally, so the pattern is symmetric.
4. Prints the grid to the terminal: `1` bits become `■`, `0` bits become blank space.

The same input always produces the same identicon.

## Usage
Requires Python 3.12+.

```
python generator.py
```

You'll be prompted for:
- **A string** to generate the identicon from (e.g. a username)
- **A grid size** `n` for an `n x n` grid

## Example
```
Enter a string: hello
Enter a grid size (n) for (n x n): 5
```

## Notes
- Odd grid sizes work best, since the mirrored grid has a center column.
- The hash has 256 bits, so grid sizes above 22 run out of bits.
