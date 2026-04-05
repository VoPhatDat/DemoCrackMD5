# Rainbow Table MD5

## wordlist.txt

danh sách mật khẩu phổ biến, mỗi dòng 1 cái

```
123456
abcd
```

---

## CreateRainbowTable.py

chạy:

```
CreateRainbowTable.py <file wordlist> <file output .rt>
```

ví dụ:

```
CreateRainbowTable.py wordlist.txt wordlist.rt
```

---

## CrackMD5.py

chạy:

```
CrackMD5.py "hash" <file .rt>
```

ví dụ:

```
CrackMD5.py "e10adc3949ba59abbe56e057f20f883e" wordlist.rt
```

kết quả:

```
123456
```

---

## note

* hash phải là md5
* phải tạo .rt trước
* wordlist mỗi dòng 1 pass
* lỗi lặt vặt thường do format file hoặc đọc file
