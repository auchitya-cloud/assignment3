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

if __name__ == "__main__":
    file = "random_strings_5mb.txt"
    target_size_mb = 5

    create_strings_file(file, target_size_mb)
    print(f"File '{file}' created with approximately 5 MB of random strings.")
