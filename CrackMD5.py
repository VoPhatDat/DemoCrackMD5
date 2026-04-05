#!/usr/bin/env python3
import pickle
import sys
import time

def load_rainbow_table_rt(rt_file):
    """Load rainbow table từ file .rt (binary pickle)"""
    try:
        with open(rt_file, 'rb') as f:
            rainbow = pickle.load(f)
        return rainbow
    except FileNotFoundError:
        print(f"[!] Không tìm thấy: {rt_file}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Lỗi load file: {e}")
        sys.exit(1)

def crack_hash(hash_value, rainbow_table):
    """Crack hash bằng rainbow table"""
    hash_value = hash_value.lower().strip()
    
    if hash_value in rainbow_table:
        return rainbow_table[hash_value]
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 crack_rt.py <hash> [rainbow_table.rt]")
        print("Example: python3 crack_rt.py 81dc9bdb52d04dc20036dbd8313ed055 rainbow_table.rt")
        sys.exit(1)
    
    hash_to_crack = sys.argv[1]
    rt_file = sys.argv[2] if len(sys.argv) > 2 else "rainbow_table.rt"
    
    print(f"[*] Loading rainbow table from: {rt_file}")
    start_time = time.time()
    rainbow = load_rainbow_table_rt(rt_file)
    load_time = time.time() - start_time
    
    print(f"[+] Loaded {len(rainbow)} hashes in {load_time:.4f}s")
    
    print(f"[*] Cracking: {hash_to_crack}")
    start_crack = time.time()
    result = crack_hash(hash_to_crack, rainbow)
    crack_time = time.time() - start_crack
    
    if result:
        print(f"[+] FOUND! Password: {result}")
        print(f"[+] Crack time: {crack_time*1000:.2f}ms")
        return 0
    else:
        print(f"[-] Not found in table")
        print(f"[+] Search time: {crack_time*1000:.2f}ms")
        return 1

if __name__ == "__main__":
    sys.exit(main())