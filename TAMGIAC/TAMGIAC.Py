def dich_chu(c, k):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    return c


def giai_ma(s):
    ket_qua = ""
    i = 0

    while i < len(s):
        if s[i].isalpha():
            c = s[i]
            i += 1

            # Đọc số đứng sau chữ cái
            k = 0
            while i < len(s) and s[i].isdigit():
                k = k * 10 + int(s[i])
                i += 1

            ket_qua += dich_chu(c, k)
        else:
            # Ký tự không phải chữ cái giữ nguyên
            ket_qua += s[i]
            i += 1

    return ket_qua



with open("MATTHU.INP", "r", encoding="utf-8") as f:
    s = f.readline().strip()

cac_mat_thu = s.split("@")

mat_thu_dai_nhat = ""

for mat_thu in cac_mat_thu:
    giai_ma_mat_thu = giai_ma(mat_thu)

    if len(giai_ma_mat_thu) > len(mat_thu_dai_nhat):
        mat_thu_dai_nhat = giai_ma_mat_thu

with open("MATTHU.OUT", "w", encoding="utf-8") as f:
    f.write(mat_thu_dai_nhat)