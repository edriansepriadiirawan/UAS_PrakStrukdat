class Hashing:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    
    def hash_function(self, new_data):
        index = new_data % self.size
        return index

    def add(self, new_data):
        if self.data[self.hash_function(new_data)] == None:
            index = self.hash_function(new_data)
            self.data[index] = new_data
        else:
            index = self.hash_function(new_data)
            self.data[index].append(new_data)
    
    def find(self, key):
        key_hash = self.hash_function(key)
        if self.data[key_hash] is None:
            return False
        for index in range(self.size):
            if(self.data[index] == key):
                print('keynya adalah : ',key,'Indexnya adalah : ',index)
                return True
        print("Key ", key, " tidak ditemukan")
        return False

    def __str__(self):
        hash_table_str = 'Ukuran Tabel Hash: ' + str(self.size) + '\n'
        hash_table_str = hash_table_str + "Isi Tabel: " + str(self.data)
        return hash_table_str

if __name__ == "__main__":
    while True:
        masukkan = int(input("Masukkan Berapa banyak data : "))
        hash = Hashing(masukkan)
        for i in range(masukkan):
            inputadd = int(input("Masukkan data : "))
            hash.add(inputadd)
        print(hash)
        findin = int(input("Masukkan data yang ingin dicari : "))
        hash.find(findin)
        
        masukkan1 = str(input("Apakah anda ingin melanjutkan program(ya)?"))
        if masukkan1 == 'ya':
            continue
        else:
            break
