
import time

def brute_force(password, charset, max_length):
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempts += 1
            attempt_str = ''.join(attempt)
            if attempt_str == password:
                end_time = time.time()
                print(f"Şifre bulundu: {attempt_str}")
                print(f"Deneme sayısı: {attempts}")
                print(f"Geçen süre: {end_time - start_time:.2f} saniye")
                return
    print("Şifre bulunamadı.")

if __name__ == "__main__":
    target_password = input("Kırmak istediğiniz şifreyi girin: ")
    charset = input("Karakter kümesini girin (örneğin, abc123): ")
    max_length = int(input("Maksimum uzunluğu girin: "))

    brute_force(target_password, charset, max_length)
    
