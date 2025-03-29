
```python
import itertools
import string

class BruteForceTool:
    def __init__(self, target_password):
        self.target_password = target_password

    def generate_combinations(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        for attempt in itertools.product(characters, repeat=length):
            yield ''.join(attempt)

    def crack_password(self, max_length):
        for length in range(1, max_length + 1):
            for attempt in self.generate_combinations(length):
                print(f"Giriş denemesi: {attempt}")
                if attempt == self.target_password:
                    print(f"Şifre bulundu: {attempt}")
                    return
        print("Şifre bulunamadı.")

def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    file_path = input("Şifrelerin bulunduğu dosyanın yolunu girin: ")
    passwords = read_passwords_from_file(file_path)

    for target_password in passwords:
        print(f"Kırılacak şifre: {target_password}")
        max_length = int(input("Maksimum uzunluğu girin: "))

        brute_force_tool = BruteForceTool(target_password)
        brute_force_tool.crack_password(max_length)
```
