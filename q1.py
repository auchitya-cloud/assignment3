import random
import string

def rand_string(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def create_strings_file(filename, num_lines, line_length):
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            random_string = rand_string(line_length)
            f.write(random_string + '\n')

if __name__ == "__main__":
    file = "random_strings.txt"
    lines = 1000
    length = 50

    create_strings_file(file, lines, length)
    print(f"File '{file}' with {lines} lines of random strings created.")
