##Created by AhmetÇağatay

###ileride kullanılacak değerlerin tanımı###
gün=0
fazla=[1,3,5,7,8,10,12]
eksik=[4,6,9,11]
ekliYillar=0
eksizYillar=0
a=[]
b=[]
###ileride kullanılacak değerlerin tanımı###


def main():
    #başlangıç fonksiyonu (menü gibi düşünebilirsiniz.)
    print("Herhangi bir tarih giriniz.")
    bugün = tarihiAl()
    print("Arasındaki günü hesaplamak istediğiniz tarihi giriniz.")
    tarih = tarihiAl()

    günSayisi(bugün,tarih)

def tarihiAl():
    #kullanıcıdan tarihleri almak için bu fonksiyounu kullanıyoruz.
    bugün = [-1,-1,-1]
    while 0>bugün[0] or bugün[0]>31:
        bugün[0] = int(input("Gün:"))
        if 0>bugün[0] or bugün[0]>31:
            print("Hata: Günü yanlış girdiniz.")
    while 0>bugün[1] or bugün[1]>12:
        bugün[1] = int(input("Ay:"))
        if 0>bugün[1] or bugün[1]>12:
            print ("Hata: Ayı yanlış girdiniz.")
    bugün[2] = int(input("Yıl:"))
    return bugün





def günEkleAy(veri,artik):
    #Aylara göre gün eklemek için bu fonksiyonu kullanıyoruz.
    global gün
    ekle=0
    for i in range(1,veri+1):
        
        if i == 2:
            
            if artik == 0:
                ekle +=29
            else:
                ekle+=28
                
        elif any([i == x for x in fazla]):
            ekle+=31
                
        elif any([i == x for x in eksik]):
            ekle+=30
            
        else:
            print("başka bir şey çıktı")
            
    gün += ekle

def günCikartAy(veri,artik):
    #Aylara göre gün çıkartmak için bu fonksiyonu kullanıyoruz.
    global gün
    cikart=0
    for i in range(1,veri+1):
        
        if i == 2:
            if artik == 0:
                cikart -=29
                
            else:
                cikart-=28
                
        elif any([i == x for x in fazla]):
            cikart-=31
                
        elif any([i == x for x in eksik]):
            cikart-=30
            
        else:
            print("başka bir şey çıktı")
            
    gün += cikart

def günSayisi(bugün,tarih):
    global ekliYillar
    global eksizYillar
    global gün
    global a
    global b
    #Tarih aralığı gelecek mi? geçmiş mi? şimdi mi?
    #zaman = 0:geçmiş 1:şimdi 2:gelecek
    zaman=1
    if bugün == tarih:
        zaman=1    
    elif bugün[2]>tarih[2]:
        zaman=0
    elif bugün[2]<tarih[2]:
        zaman=2
    else:
        if bugün[1]>tarih[1]:
            zaman=0
        elif bugün[1]<tarih[1]:
            zaman=2
        else:
            if bugün[0]>tarih[0]:
                zaman=0
            elif bugün[0]<tarih[0]:
                zaman=2
            else:
                zaman=1
    #eğer aynı gün ise baştan başlıyoruz
    if zaman==1:
        print("Hata: Aynı günü girdiniz!")
        main()
    
    #eğer aynı gün değil ise devam
    else:

        #eğer "tarih", "bugün"den daha geçmiş bir tarih olarak yazılmışsa
        #bütün denklem geleceğe dair olduğu için
        #tarihlerin yerlerini değiştiriyoruz.
        if zaman == 0:
            a=bugün
            b=tarih
            tarih=a
            bugün=b
            zaman=2
        if zaman==2:
            
            #gün hesaplamasından günü ekliyoruz
            gün += tarih[0]-bugün[0]
            
            #ay hesaplamasından gün ekliyoruz
            artik = bugün[2]%4
            günEkleAy(tarih[1]-1,artik)
            günCikartAy(bugün[1]-1,artik)

            #yıl hesaplamasından gün ekliyoruz
            #Dikkat: Her yıl 365 gün değildir.
            #Eğer bilgi sahibi değilseniz, konu ile ilgili araştırma yapınız.
            for i in range(bugün[2]+1,tarih[2]+1):
                
                if i > 1000 and i%100==0:
                    
                    if i%400==0:
                        ekliYillar += 1
                    else:
                        eksizYillar += 1
                        
                elif i%4==0:
                    ekliYillar += 1
                    
                else:
                    eksizYillar += 1
            
            gün += ekliYillar*366
            gün += eksizYillar*365

            #Ve nihayet hesaplanan günü bastırıyoruz.
            print("Tarihler arasında",gün,"gün var")

main()
