[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PItWslYG)

# UG 12 Tree

## Kerjakanlah pada file main.py
Pada UG ini, kalian sudah diberikan sebuah class Node yang merepresentasikan sebuah struktur data tree. Kalian 

Yang harus kalian lakukan sekarang adalah membuat sebuah buah fungsi: yang pertama, fungsi minus_plus. Fungsi ini berfungsi untuk menjumlahkan / mengurangkan semua node yang ada di dalam tree. Jika data ganjil, maka kurangkan, dan jika data genap, maka tambahkan. Misal, jika satu tree mempunyai node - node berikut: 20 2 10 2 5, maka hasil akhirnya adalah 29 (20 + 2 + 10 + 2 - 5). Contoh lainnya, jika suatu tree mempunyai node - node berikut: 23 25 27 26, maka hasil akhirnya adalah -49 (- 23 - 25 - 27 + 26).


## Test Case
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print()
    print(binaryT.plus_minus())

## Output

    PS C:\Users\Gian\Documents\ukdw\ukdw smt5\asdos\minggu13b> python .\kj.py

    -7