import random
import string
import os

def rand_string(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def create_strings_file(filename, target_size_mb):
    target_size_bytes = target_size_mb * 1024 * 1024

    with open(filename, 'w') as f:
        while os.path.getsize(filename) < target_size_bytes:
            random_string = rand_string(100)  # Adjust the string length as needed.
            f.write(random_string + '\n')

def create_multiple_files(num_files, target_size_mb):
    for i in range(1, num_files + 1):
        filename = f"random_strings_{i}_5mb.txt"
        create_strings_file(filename, target_size_mb)
        print(f"File '{filename}' created with approximately 5 MB of random strings.")

if __name__ == "__main__":
    num_files = 10
    target_size_mb = 5

    create_multiple_files(num_files, target_size_mb)
