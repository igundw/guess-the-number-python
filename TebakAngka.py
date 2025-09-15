import random

angka_komputer = random.randint(1, 20)
#welcome message
print(f''' 
-------------------
|  Selamat Datang |
|     Di Game     |
|   Tebak Angka   |
-------------------
''')
nama = input('Hai, Siapa Nama Kamu?: ')
ajakan_bermain = input(f'{nama}, apakah Kamu siap bermain tebak angka bersama aku?: ').lower()
# If Level 1 (Tanya ingin main atau tidak)
if 'ya' in ajakan_bermain or 'iya' in ajakan_bermain or 'siap' in ajakan_bermain or 'oke' in ajakan_bermain:
    print('Keren, Bos! Ayo Kita Mulai Bermain!')

    # menyuruh user untuk input jawabannya
    print(f'Nah {nama}, Aku udah milih angka acak dari 1-20 nih, Kamu tebak ya angka berapa!')
    

    # pengecekan jawaban user
    while True:
        pilihan_user = int(input('Angka tebakan kamu adalah: '))
        if pilihan_user < angka_komputer:
            print('Tebakan Kamu terlalu Kecil, Coba lagi!')
        elif pilihan_user > angka_komputer:
            print('Angka yang kamu pilih terlalu besar, Coba lagi ya!')
        elif pilihan_user == angka_komputer:
            print(f'SELAMAT, {nama}! Jawaban Kamu benar :)')
            break
        else: 
            print('Waduhhh angkanya kelewatan, broo')

else:
    print(f'Yahh, oke deh. Semoga next time kita bisa main bareng, ya {nama} :)')

print('-------------- GAME SELESAI --------------')
