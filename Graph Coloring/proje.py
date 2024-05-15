import networkx as nx
import time
import matplotlib.pyplot as plt

# Kenar listesini dosyadan okumak için bir fonksiyon
def dosyadan_kenar_listesini_oku(dosya_adi):
    kenar_listesi = []
    with open(dosya_adi, 'r') as dosya:
        for satir in dosya:
            if satir.strip():  # Boş satırları atla
                kenar = tuple(map(int, satir.strip().split()))
                kenar_listesi.append(kenar)
    return kenar_listesi

# Graf oluşturma ve renklendirme işlemleri
def graf_renklendir(graf):
    renkler = {dugum: None for dugum in graf}
    for dugumda in graf:
        komşu_renkler = {renkler[komşu] for komşu in graf[dugumda] if renkler[komşu] is not None}
        renk = 0
        while renk in komşu_renkler:
            renk += 1
        renkler[dugumda] = renk
    return renkler

# Veriyi dosyadan okuyarak grafı oluşturun
dosya_adi = 'kenarlar.txt'  # Dosya adını buradan değiştirebilirsiniz
kenar_listesi = dosyadan_kenar_listesini_oku(dosya_adi)

graf = nx.Graph()
graf.add_edges_from(kenar_listesi)

# Algoritmanın çalışma süresini ölçmek için
start_time = time.time()
renkler = graf_renklendir(graf)
end_time = time.time()

# Algoritmanın çalışma süresini yazdır
calisma_suresi = end_time - start_time
print(f"Algoritmanın çalışma süresi: {calisma_suresi:.6f} saniye")

# Kullanılan renk sayısını hesapla
kullanilan_renkler = set(renkler.values())
renk_sayisi = len(kullanilan_renkler)

print(f"Toplam kullanılan renk sayısı: {renk_sayisi}")

# Düğümleri ve renklerini yazdır
print("Köşe ve renk eşleşmeleri:")
for dugum, renk in renkler.items():
    print(f"köşe = {dugum}, renk = {renk}")

# Düğümleri renklerine göre çiz ve görselleştir
nx.draw(graf, node_color=list(renkler.values()), with_labels=True, cmap=plt.get_cmap("tab10"), node_size=20)
plt.title("Verilen Veri Setine Göre Graf - Renklendirme")
plt.show()
