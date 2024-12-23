[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/NS5AeyeU)
# UG 11 HASHING
## Gunakan main.py 
## Haram hukumnya untuk memakai dictionary
Buatlah sebuah hash table untuk melakukan penyimpanan pasangan nim dan nama mahasiswa. Jadikan nim sebagai key dan nama sebagai value nya.

kapasitas defaultnya adalah 10.

Gunakanlah linear probing untuk melakukan collision handling.

Tugas kalian sederhana. Kalian hanya tinggal memodifikasi penerapan Hash Table yang ada pada modul kalian. Berikut adalah list method yang harus kalian buat:

- **_get_hash(self, key)**
  
  Fungsi ini berfungsi untuk mengembalikan hasil daripada hash function. Tinggal ikuti saja yang ada di modul. Ingat bahwa key adalah NIM yang bertipe data sebuah interger bukan string sehingga ada bagian dari fungsi ini yang harus kalian modif sedikit.

- **_probing(self, key)**
  
  Fungsi ini berfungsi untuk melakukan probing pada hash table kalian jika semisalnya terjadi collision. Fungsi ini memanfaatkan linear probing untuk menangani collision.

- **_linear_probing(self, key, index)**
  
  Fungsi ini berfungsi untuk melakukan linear probing

- **add(self, key, value)**
  
  Fungsi ini berfungsi memasukkan key value pair ke dalam hash table

- **get_data(self, key)**
  
  Fungsi ini berfungsi mengambil data dari hash table berdasarkan key.

- **resize(self, size)**
  
  Fungsi ini berfungsi untuk melakukan penambahan jumlah kapasitas dari hash table. parameter *size* adalah jumlah kapasitas yang baru. Misal, jika aku punya hash table dengan nama ht, maka jka aku panggil ht.resize(3), maka hash table akan berubah kapasitasnya menjadi 3. 

- **print_all(self)**
  
  Fungsi ini untuk menampilkan nim dan nama dari hash table (lihat hasil outputnya untuk lebih jelas)
Hampir semua method yang ada disini, ada juga di modul (ada yang namanya berbeda). 

## Test Case
```
    ht : HashTable = HashTable()
    # isi hash table
    ht.add(71210689, "Gian")
    ht.add(71210683, "Yandi")
    ht.add(71210699, "Andreas")

    print("==== HASH TABLE SEBELUM DIRESIZE ====")
    print()
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
    print()
    # resize hash table
    ht.resize(3)

    print("==== HASH TABLE SETELAH DIRESIZE ====")
    print()
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
```
## Output
```
PS C:\Users\Gian\Documents\ukdw\ukdw smt5\asdos\minggu11d> python .\kj.py
==== HASH TABLE SEBELUM DIRESIZE ====

==== ISI HASH TABLE ====
NIM: 71210699 NAMA: Andreas
NIM: 71210683 NAMA: Yandi
NIM: 71210689 NAMA: Gian
mahasiswa dengan NIM 71210683 adalah Yandi

==== HASH TABLE SETELAH DIRESIZE ====

==== ISI HASH TABLE ====
NIM: 71210689 NAMA: Gian
NIM: 71210683 NAMA: Yandi
NIM: 71210699 NAMA: Andreas
mahasiswa dengan NIM 71210683 adalah Yandi
```
