import random
import string

def rand_string(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def create_strings_file(filename, target_size_gb):
    target_size_bytes = target_size_gb * 1024 * 1024 * 1024

    with open(filename, 'w') as f:
        while f.tell() < target_size_bytes:
            random_string = rand_string(100)  # Adjust the string length as needed.
            f.write(random_string + '\n')

if __name__ == "__main__":
    file_sizes_gb = [1, 2, 3, 4, 5]

    for size_gb in file_sizes_gb:
        filename = f"random_strings_{size_gb}gb.txt"
        create_strings_file(filename, size_gb)
        print(f"File '{filename}' created with {size_gb}GB of random strings.")
