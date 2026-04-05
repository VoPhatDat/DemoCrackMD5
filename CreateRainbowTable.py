#!/usr/bin/env python3
import pickle
import hashlib
import sys

def generate_rainbow_table_rt(wordlist_file, output_file):
    """Tạo rainbow table và lưu dạng .rt (binary pickle)"""
    rainbow = {}
    count = 0
    
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f_in:
            for line in f_in:
                password = line.strip()
                if password:
                    md5_hash = hashlib.md5(password.encode()).hexdigest()
                    rainbow[md5_hash] = password
                    count += 1
                    if count % 10000 == 0:
                        print(f"[*] Processed {count} passwords...")
    except FileNotFoundError:
        print(f"[!] Không tìm thấy: {wordlist_file}")
        sys.exit(1)
    
    # Lưu dạng .rt (binary pickle)
    with open(output_file, 'wb') as f:
        pickle.dump(rainbow, f)
    
    file_size = open(output_file, 'rb').read().__len__()
    print(f"[+] Done! Saved {count} hashes -> {output_file}")
    print(f"[+] File size: {file_size} bytes ({file_size/1024/1024:.2f} MB)")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 gen_rainbow_rt.py <wordlist> <output.rt>")
        print("Example: python3 gen_rainbow_rt.py passwords.txt rainbow_table.rt")
        sys.exit(1)
    
    wordlist = sys.argv[1]
    output = sys.argv[2]
    generate_rainbow_table_rt(wordlist, output)