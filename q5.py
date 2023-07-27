def convert_to_uppercase(filename):
    with open(filename, 'r') as f:
        content = f.read()

    with open(filename, 'w') as f:
        f.write(content.upper())

if __name__ == "__main__":
    file_sizes_gb = [1, 2, 3, 4, 5]

    for size_gb in file_sizes_gb:
        filename = f"random_strings_{size_gb}gb.txt"
        convert_to_uppercase(filename)
        print(f"File '{filename}' converted to uppercase.")
