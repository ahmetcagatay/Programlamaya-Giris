#by ahmetCagatay

def kosegenMatris():
    
    #kullanıcının kaç tur diyagon görmek istediğini öğreniyoruz.
    tur = int(input("Köşegen Matris kaç satır olsun: "))
    
    #1'i kaydırmak için sonradan arttıracağımız bir veri tanımlıyoruz
    döngü = 0
    
    for i in range(tur):
        
        #ilk turda 0'ı basmaması için
        #"end" fonksiyonunu satır atlamaması için kullanıyoruz.
        if döngü != 0:
            print(str(0)*döngü, end="")
        
        #bir tane "1" ve "tur"un bir eksiği kadar "0" basıyoruz.
        #ve her döngüde 0'ı azaltması için çarpanından "döngü"yü de çıkartıyoruz
        print(("1")+("0")*((tur)-1-döngü))
        
        #1'i kaydırmak için döngüyü arttırıyoruz.
        döngü += 1

kosegenMatris()
