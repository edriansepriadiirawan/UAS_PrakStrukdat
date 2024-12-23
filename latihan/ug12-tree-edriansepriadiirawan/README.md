[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SmSQZwAC)
# UG 12 Tree

## Kerjakanlah pada file main.py
Pada UG ini, kalian sudah diberikan sebuah class Node yang merepresentasikan sebuah struktur data tree. Kalian juga diberikan sebuah fungsi bernama generate_tree(number). Fungsi ini berfungsi untuk men-generate suatu Tree berdasarkan angka yang dimasukkan sebagai parameter. Fungsi ini tidak usah kalian pikirkan karena fungsi ini hanya untuk mempermudah saat melakukan testing saja.

Yang harus kalian lakukan sekarang adalah membuat 2 buah fungsi: yang pertama, fungsi minus_plus. Fungsi ini berfungsi untuk menjumlahkan / mengurangkan semua node yang ada di dalam tree. Jika data ganjil, maka kurangkan, dan jika data genap, maka tambahkan. Misal, jika satu tree mempunyai node - node berikut: 20 2 10 2 5, maka hasil akhirnya adalah 29 (20 + 2 + 10 + 2 - 5). Contoh lainnya, jika suatu tree mempunyai node - node berikut: 23 25 27 26, maka hasil akhirnya adalah -49 (- 23 - 25 - 27 + 26).

fungsi yang kedua adalah fungsi bernama find_deepest_leaf. Fungsi ini akan mengembalikan kedalaman node paling dalam. Misal, jika ada sebuah tree :

![](ss.png)

maka, fungsi ini akan mengembalikan nilai 3, karena node leaf paling dalam adalah 29 dengan depth 3. 


## Test Case
    root = generate_tree(840)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()
    root = generate_tree(1200)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()
    root = generate_tree(8440)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()
    root = generate_tree(53)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()

## Output
    PS C:\Users\Gian\Documents\ukdw\ukdw smt5\asdos\minggu12d> python .\kj.py
    hasil plus minus = 1321
    leaf paling dalam = 5

    hasil plus minus = 2145
    leaf paling dalam = 6

    hasil plus minus = 13505
    leaf paling dalam = 4

    hasil plus minus = -53
    leaf paling dalam = 0