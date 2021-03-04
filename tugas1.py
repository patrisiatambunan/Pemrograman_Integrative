while True:
  try:
    angka = int(input("Masukkan angka: "))
    if angka >= 0 or angka < 0:
        if angka >= 0:
            if angka == 0:
                print("Angka yang anda masukkan bernilai 0")
            else:
                print("Angka yang anda masukkan bernilai positif")
        else:
            print("Angka yang anda masukkan bernilai negatif")
        break
    print("Anda hanya boleh memasukkan angka")
  except Exception as e:
    print("Anda hanya boleh memasukkan angka")
