#dari celsius ke kelvin atau sebaliknya
def celAndKel(type,value):
    hasil = value
    # jika dari celsius menuju ke kelvin
    if type=="celcius":
        hasil+=273.15
    # jika dari kelvin menuju ke celsius
    else:
        hasil-=273.15
    return hasil

# dari celsius atau kelvin ke fahrenheit
def toFahrenheit(type,value):
    hasil = value
    # jika dari celsius menuju ke fahrenheit
    if type=="celcius":
        hasil = (hasil*9/5) + 32
    # jika dari kelvin menuju ke fahrenheit maka perlu diubah dulu ke celsius
    else:
        hasil = (celAndKel("kelvin",hasil)*9/5) + 32
    return hasil    

# dari fahrenheit ke celsius atau kelvin
def fromFahrenheit(type,value):
    hasil = value
    # jika dari fahrenheit menuju ke celsius
    if type=="celcius":
        hasil = (hasil-32)*5/9
    # jika dari fahrenheit menuju ke kelvin maka perlu ubah dulu ke celsius baru diubah ke kelvin
    else:
        hasil = (celAndKel("celcius",(hasil-32)*5/9))
    return hasil

cek = False
while not cek:
    print("Daftar temperatur")
    print("1. Celsius")
    print("2. Kelvin")
    print("3. Fahrenheit")
    dataFrom = int(input("Pilih dari temperatur apa data dipilih = "))

    print("Daftar temperatur")
    print("1. Celsius")
    print("2. Kelvin")
    print("3. Fahrenheit")
    dataTo = int(input("Pilih data temperatur ingin diubah ke tipe data apa = "))

    valueTemp = int(input("Masukan value temperatur yang ingin diubah = "))
    if dataFrom==1 and dataTo==2:
        print("Hasil temperatur adalah "+str(celAndKel("celcius",valueTemp)))
    elif dataFrom==1 and dataTo==3:
        print("Hasil temperatur adalah "+str(toFahrenheit("celcius",valueTemp)))
    elif dataFrom==2 and dataTo==1:
        print("Hasil temperatur adalah "+str(celAndKel("kelvin",valueTemp)))
    elif dataFrom==2 and dataTo==3:
        print("Hasil temperatur adalah "+str(toFahrenheit("kelvin",valueTemp)))
    elif dataFrom==3 and dataTo==1:
        print("Hasil temperatur adalah "+str(fromFahrenheit("celcius",valueTemp)))
    elif dataFrom==3 and dataTo==2:
        print("Hasil temperatur adalah "+str(fromFahrenheit("kelvin",valueTemp)))
    lanjut = input("Ingin lanjut ?(y/n):")
    lanjut.lower
    if lanjut=="n":
        cek = True