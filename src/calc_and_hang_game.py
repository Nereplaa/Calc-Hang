
"""
Calc & Hang - İşlem Yap, Harfi Kurtar
Hesap makinesi ve adam asmaca oyunlarının benzersiz birleşimi
Yazar: Alperen Yağmur
Tarih: Kasım 2025
"""

import random
import json
import os
from typing import Dict, List, Tuple, Optional

# Renkli çıktı için colorama modülünü dene, yoksa düz metin kullan
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    RENK_DESTEGI = True
except ImportError:
    RENK_DESTEGI = False
    # colorama yoksa boş sınıflar tanımla
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = BLUE = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""


class AsmacaCizici:
    """
    Hata sayısına göre asmaca figürünü çizer.
    Her hata ile figür bir parça daha tamamlanır.
    """
    
    def __init__(self, maksimum_hata: int = 6):
        """Çiziciyi maksimum hata sayısı ile başlat."""
        self.maks_hata = maksimum_hata
        self.asmaca_asamalari = self._asamalari_olustur()
    
    def _asamalari_olustur(self) -> List[str]:
        """
        Her hata aşaması için görsel temsiller oluşturur.
        Liste indeksi yapılan hata sayısını gösterir.
        """
        asamalar = [
            # Aşama 0: Hiç hata yok
            """
            +---+
            |   |
                |
                |
                |
                |
            =========
            """,
            # Aşama 1: Kafa
            """
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            """,
            # Aşama 2: Gövde
            """
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            """,
            # Aşama 3: Sol kol
            """
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            """,
            # Aşama 4: Sağ kol
            """
            +---+
            |   |
            O   |
           /|\\  |
                |
                |
            =========
            """,
            # Aşama 5: Sol bacak
            """
            +---+
            |   |
            O   |
           /|\\  |
           /    |
                |
            =========
            """,
            # Aşama 6: Sağ bacak - oyun bitti
            """
            +---+
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            =========
            """
        ]
        return asamalar
    
    def figuru_goster(self, hata_adedi: int) -> str:
        """
        Mevcut hata sayısına uygun figürü döndürür.
        
        Parametreler:
            hata_adedi: Şu ana kadar yapılan hata sayısı
            
        Döndürür:
            Asmaca figürünün ASCII sanat stringi
        """
        asama_no = min(hata_adedi, len(self.asmaca_asamalari) - 1)
        return self.asmaca_asamalari[asama_no]


class KelimeDeposu:
    """
    Kategorilere göre organize edilmiş kelime koleksiyonlarını yönetir.
    Rastgele kelime seçimi sağlar.
    """
    
    def __init__(self):
        """Kelime deposunu önceden tanımlı kategorilerle başlat."""
        self.kategoriler = {
            'meyve': [
                'elma', 'muz', 'portakal', 'uzum', 'mango',
                'ananas', 'cilek', 'karpuz', 'kiraz', 'seftali'
            ],
            'hayvan': [
                'fil', 'kaplan', 'penguen', 'yunus', 'zurafa',
                'kanguru', 'pars', 'zebra', 'gergedan', 'cita'
            ],
            'teknoloji': [
                'bilgisayar', 'telefon', 'internet', 'yazilim', 'algoritma',
                'veritabani', 'sunucu', 'islemci', 'klavye', 'monitor'
            ]
        }
    
    def rastgele_kelime_sec(self) -> Tuple[str, str]:
        """
        Depodan rastgele bir kategori ve kelime seçer.
        
        Döndürür:
            (kelime, kategori_adi) tuple'ı
        """
        kategori_adi = random.choice(list(self.kategoriler.keys()))
        secilen_kelime = random.choice(self.kategoriler[kategori_adi])
        return secilen_kelime.lower(), kategori_adi


class MatematikMotoru:
    """
    Matematiksel hesaplamaları yönetir ve her işlemin tek kullanımını kontrol eder.
    Her matematik işlemi oyun başına sadece bir kez kullanılabilir.
    """
    
    def __init__(self):
        """Motoru mevcut işlemlerle başlat."""
        self.kullanilabilir_islemler = {
            'toplama': True,
            'cikarma': True,
            'carpma': True,
            'bolme': True
        }
        self.islem_sembolleri = {
            'toplama': '+',
            'cikarma': '-',
            'carpma': '*',
            'bolme': '/'
        }
        self.hassasiyet = 1e-6
    
    def kalan_islemleri_getir(self) -> List[str]:
        """
        Henüz kullanılmamış işlemlerin listesini döndürür.
        
        Döndürür:
            Kullanılabilir işlem isimlerinin listesi
        """
        return [islem for islem, kullanilabilir in self.kullanilabilir_islemler.items() if kullanilabilir]
    
    def hesapla(self, islem_turu: str, birinci_sayi: float, ikinci_sayi: float) -> Optional[float]:
        """
        Belirtilen matematik işlemini gerçekleştirir.
        
        Parametreler:
            islem_turu: Yapılacak işlem türü
            birinci_sayi: İlk operand
            ikinci_sayi: İkinci operand
            
        Döndürür:
            İşlem sonucu veya geçersizse None
        """
        if islem_turu == 'toplama':
            return birinci_sayi + ikinci_sayi
        elif islem_turu == 'cikarma':
            return birinci_sayi - ikinci_sayi
        elif islem_turu == 'carpma':
            return birinci_sayi * ikinci_sayi
        elif islem_turu == 'bolme':
            if abs(ikinci_sayi) < self.hassasiyet:
                return None  # Sıfıra bölme hatası
            return birinci_sayi / ikinci_sayi
        return None
    
    def cevap_kontrol(self, kullanici_cevap: float, dogru_cevap: float) -> bool:
        """
        Kullanıcının cevabının doğru olup olmadığını hassasiyet toleransı ile kontrol eder.
        
        Parametreler:
            kullanici_cevap: Kullanıcının verdiği cevap
            dogru_cevap: Matematiksel olarak doğru cevap
            
        Döndürür:
            Cevaplar tolerans dahilinde eşleşiyorsa True
        """
        return abs(kullanici_cevap - dogru_cevap) <= self.hassasiyet
    
    def islemi_kullanildi_isaretle(self, islem_turu: str):
        """
        Bir işlemi kullanıldı olarak işaretler, tekrar kullanılamaz.
        
        Parametreler:
            islem_turu: İşaretlenecek işlem
        """
        if islem_turu in self.kullanilabilir_islemler:
            self.kullanilabilir_islemler[islem_turu] = False
    
    def islem_listesi_hazirla(self) -> str:
        """
        Kalan işlemlerin formatlanmış bir stringini oluşturur.
        
        Döndürür:
            Mevcut işlemleri listeleyen string
        """
        kalan = self.kalan_islemleri_getir()
        if not kalan:
            return "Kalan işlem yok!"
        
        gosterim_isimleri = {
            'toplama': 'Toplama (+)',
            'cikarma': 'Çıkarma (-)',
            'carpma': 'Çarpma (*)',
            'bolme': 'Bölme (/)'
        }
        return ', '.join([gosterim_isimleri[islem] for islem in kalan])


class PuanYoneticisi:
    """
    Oyuncu puanını oyun boyunca takip eder ve kayıt yönetimini sağlar.
    """
    
    def __init__(self):
        """Puan yöneticisini varsayılan değerlerle başlat."""
        self.aktif_puan = 0
        self.kayit_dosyasi = 'scores.json'
        self.puan_tablosu = {
            'dogru_harf': 10,
            'yanlis_harf': -5,
            'dogru_islem': 15,
            'yanlis_islem': -10,
            'kazanma_bonusu': 50,
            'kaybetme_cezasi': -20
        }
    
    def puan_degistir(self, eylem_turu: str):
        """
        Eylem türüne göre puanı değiştirir.
        
        Parametreler:
            eylem_turu: Puanlanacak eylem türü
        """
        if eylem_turu in self.puan_tablosu:
            self.aktif_puan += self.puan_tablosu[eylem_turu]
    
    def suanki_puani_getir(self) -> int:
        """Mevcut puan değerini döndürür."""
        return self.aktif_puan
    
    def puani_kaydet(self, oyuncu_ismi: str):
        """
        Mevcut puanı JSON dosyasına kaydeder.
        
        Parametreler:
            oyuncu_ismi: Oyuncunun adı veya kimliği
        """
        try:
            # Mevcut puanları yükle
            if os.path.exists(self.kayit_dosyasi):
                with open(self.kayit_dosyasi, 'r', encoding='utf-8') as dosya:
                    puan_verileri = json.load(dosya)
            else:
                puan_verileri = []
            
            # Yeni puanı ekle
            puan_verileri.append({
                'oyuncu': oyuncu_ismi,
                'puan': self.aktif_puan
            })
            
            # Puana göre sırala ve en iyi 5'i tut
            puan_verileri.sort(key=lambda x: x['puan'], reverse=True)
            puan_verileri = puan_verileri[:5]
            
            # Dosyaya geri kaydet
            with open(self.kayit_dosyasi, 'w', encoding='utf-8') as dosya:
                json.dump(puan_verileri, dosya, indent=4, ensure_ascii=False)
                
        except Exception as hata:
            print(f"Uyarı: Puan kaydedilemedi - {hata}")
    
    def en_yuksek_puanlari_goster(self):
        """En iyi 5 puanı dosyadan gösterir."""
        try:
            if not os.path.exists(self.kayit_dosyasi):
                print("Önceden kaydedilmiş puan bulunamadı.")
                return
            
            with open(self.kayit_dosyasi, 'r', encoding='utf-8') as dosya:
                puan_verileri = json.load(dosya)
            
            if not puan_verileri:
                print("Gösterilecek puan yok.")
                return
            
            print("\n" + "="*40)
            print("🏆 EN YÜKSEK 5 PUAN 🏆".center(40))
            print("="*40)
            for sira, kayit in enumerate(puan_verileri, 1):
                print(f"{sira}. {kayit['oyuncu']}: {kayit['puan']} puan")
            print("="*40 + "\n")
            
        except Exception as hata:
            print(f"Uyarı: Puanlar yüklenemedi - {hata}")


class OyunDurumKontrolcusu:
    """
    Kelime ilerlemesi, tahminler ve kaynaklar dahil tüm oyun durumunu yönetir.
    """
    
    def __init__(self, hedef_kelime: str, kategori: str, maksimum_hata: int = 6):
        """
        Yeni bir oyun için oyun durumunu başlat.
        
        Parametreler:
            hedef_kelime: Tahmin edilecek kelime
            kategori: Kelimenin kategorisi
            maksimum_hata: Oyun bitmeden önce izin verilen maksimum hata
        """
        self.hedef_kelime = hedef_kelime.lower()
        self.kelime_kategorisi = kategori
        self.maksimum_hata_siniri = maksimum_hata
        self.yapilan_hata_sayisi = 0
        self.biriken_bonus_puan = 0
        self.denenen_harfler = set()
        self.acilan_harfler = set()
        self.ipucu_gosterildi_mi = False
        
    def harf_tahmin_et(self, tahmin_edilen_harf: str) -> Tuple[bool, str]:
        """
        Bir harf tahmin girişimini işler.
        
        Parametreler:
            tahmin_edilen_harf: Oyuncunun tahmin ettiği harf
            
        Döndürür:
            (basari: bool, mesaj: str) tuple'ı
        """
        tahmin_edilen_harf = tahmin_edilen_harf.lower()
        
        # Girdiyi doğrula
        if len(tahmin_edilen_harf) != 1:
            return False, "Lütfen tam olarak bir harf girin!"
        
        if not tahmin_edilen_harf.isalpha():
            return False, "Lütfen geçerli bir alfabetik karakter girin!"
        
        if tahmin_edilen_harf in self.denenen_harfler:
            return False, f"'{tahmin_edilen_harf}' harfini daha önce denediniz!"
        
        # Tahmini kaydet
        self.denenen_harfler.add(tahmin_edilen_harf)
        
        # Harfin kelimede olup olmadığını kontrol et
        if tahmin_edilen_harf in self.hedef_kelime:
            self.acilan_harfler.add(tahmin_edilen_harf)
            return True, f"Doğru! '{tahmin_edilen_harf}' kelimede var!"
        else:
            self.yapilan_hata_sayisi += 1
            return False, f"Yanlış! '{tahmin_edilen_harf}' kelimede yok."
    
    def rastgele_harf_ac(self) -> Optional[str]:
        """
        Hedef kelimeden rastgele açılmamış bir harfi açar.
        
        Döndürür:
            Açılan harf, veya tüm harfler açıksa None
        """
        acilmamis_harfler = set(self.hedef_kelime) - self.acilan_harfler
        if acilmamis_harfler:
            rastgele_harf = random.choice(list(acilmamis_harfler))
            self.acilan_harfler.add(rastgele_harf)
            self.denenen_harfler.add(rastgele_harf)
            return rastgele_harf
        return None
    
    def bonus_puan_ekle(self):
        """Bonus puanı 1 artırır."""
        self.biriken_bonus_puan += 1
    
    def ipucu_kullan(self) -> Tuple[bool, str]:
        """
        Kelime kategorisini açığa çıkarmak için bonus puan kullanır.
        
        Döndürür:
            (basari: bool, mesaj: str) tuple'ı
        """
        if self.ipucu_gosterildi_mi:
            return False, "Bu oyun için zaten ipucu kullandınız!"
        
        if self.biriken_bonus_puan < 1:
            return False, "Yeterli bonus puanınız yok! Bonus puan kazanmak için matematik problemi çözün."
        
        self.biriken_bonus_puan -= 1
        self.ipucu_gosterildi_mi = True
        return True, f"Kategori ipucu: {self.kelime_kategorisi}"
    
    def hata_sayisini_artir(self):
        """Hata sayısını 1 artırır."""
        self.yapilan_hata_sayisi += 1
    
    def maskeli_kelime_goster(self) -> str:
        """
        Açılan harfler ve boşluklarla gösterim stringi oluşturur.
        
        Döndürür:
            Mevcut kelime ilerlemesini gösteren string (örn: "a _ _ l e")
        """
        gosterim_karakterler = []
        for karakter in self.hedef_kelime:
            if karakter in self.acilan_harfler:
                gosterim_karakterler.append(karakter)
            else:
                gosterim_karakterler.append('_')
        return ' '.join(gosterim_karakterler)
    
    def kazanma_kontrolu(self) -> bool:
        """
        Oyuncunun oyunu kazanıp kazanmadığını kontrol eder.
        
        Döndürür:
            Tüm harfler açıldıysa True
        """
        return set(self.hedef_kelime) <= self.acilan_harfler
    
    def kaybetme_kontrolu(self) -> bool:
        """
        Oyuncunun oyunu kaybedip kaybetmediğini kontrol eder.
        
        Döndürür:
            Hata limitine ulaşıldıysa True
        """
        return self.yapilan_hata_sayisi >= self.maksimum_hata_siniri
    
    def durum_ozetini_getir(self) -> Dict:
        """
        Mevcut oyun durumu ile bir dictionary döndürür.
        
        Döndürür:
            Tüm ilgili oyun durumu bilgilerini içeren dictionary
        """
        return {
            'maskeli_kelime': self.maskeli_kelime_goster(),
            'hatalar': self.yapilan_hata_sayisi,
            'maksimum_hata': self.maksimum_hata_siniri,
            'bonus_puanlar': self.biriken_bonus_puan,
            'tahmin_edilen_harfler': sorted(list(self.denenen_harfler)),
            'kalan_hak': self.maksimum_hata_siniri - self.yapilan_hata_sayisi
        }


class ArayuzYoneticisi:
    """
    Tüm kullanıcı arayüzü öğelerini ve etkileşimlerini yönetir.
    """
    
    def __init__(self, renk_aktif: bool = True):
        """
        Arayüz yöneticisini başlat.
        
        Parametreler:
            renk_aktif: Renkli çıktı kullanılıp kullanılmayacağı
        """
        self.renkler_aktif = renk_aktif and RENK_DESTEGI
    
    def renklendir(self, metin: str, renk: str, parlak: bool = False) -> str:
        """
        Renkler aktifse metne renk uygular.
        
        Parametreler:
            metin: Renklendirilecek metin
            renk: Uygulanacak renk
            parlak: Metnin parlak olup olmayacağı
            
        Döndürür:
            Renkli veya düz metin
        """
        if not self.renkler_aktif:
            return metin
        
        onek = Style.BRIGHT if parlak else ""
        return f"{onek}{renk}{metin}{Style.RESET_ALL}"
    
    def oyun_basligini_goster(self):
        """Oyun başlık banner'ını gösterir."""
        baslik = """
        ╔════════════════════════════════════════════════╗
        ║  === Calc & Hang: İşlem Yap, Harfi Kurtar ===  ║
        ╚════════════════════════════════════════════════╝
        """
        print(self.renklendir(baslik, Fore.CYAN, True))
    
    def oyun_durumunu_goster(self, oyun_durum: OyunDurumKontrolcusu, cizici: AsmacaCizici):
        """
        Mevcut oyun durumunun tamamını gösterir.
        
        Parametreler:
            oyun_durum: Mevcut oyun durumu nesnesi
            cizici: Asmaca görsel çizici
        """
        print("\n" + "="*50)
        print(self.renklendir("--- Yeni Tur ---", Fore.YELLOW, True))
        print("="*50)
        
        # Asmaca figürünü göster
        figur = cizici.figuru_goster(oyun_durum.yapilan_hata_sayisi)
        print(self.renklendir(figur, Fore.RED))
        
        # Kelime ilerlemesini göster
        durum = oyun_durum.durum_ozetini_getir()
        print(self.renklendir(f"Kelime: {durum['maskeli_kelime']}", Fore.GREEN, True))
        
        # Tahmin edilen harfleri göster
        if durum['tahmin_edilen_harfler']:
            tahminler_gosterim = ', '.join(durum['tahmin_edilen_harfler'])
            print(f"Tahmin edilen harfler: {tahminler_gosterim}")
        
        # Kalan hakları göster
        print(self.renklendir(
            f"Kalan hata hakkı: {durum['kalan_hak']}", 
            Fore.YELLOW
        ))
        
        # Bonus puanları göster
        print(self.renklendir(
            f"Bonus puanı: {durum['bonus_puanlar']}", 
            Fore.MAGENTA
        ))
        print("="*50 + "\n")
    
    def menu_seceneklerini_goster(self, matematik_motoru: MatematikMotoru):
        """
        Mevcut oyuncu seçeneklerini gösterir.
        
        Parametreler:
            matematik_motoru: Kalan işlemleri göstermek için matematik motoru
        """
        print(self.renklendir("Seçenekler: ", Fore.CYAN, True))
        print("  [H]arf tahmini | [İ]şlem çöz | [I]pucu | [Ç]ıkış")
        print(f"\nKalan işlemler: {matematik_motoru.islem_listesi_hazirla()}")
    
    def oyuncu_secimini_al(self) -> str:
        """
        Ana menü seçimini oyuncudan alır.
        
        Döndürür:
            Oyuncunun seçimi küçük harf string olarak
        """
        secim = input(self.renklendir("\nSeçiminiz: ", Fore.WHITE, True)).lower().strip()
        return secim
    
    def harf_girdisi_al(self) -> str:
        """
        Oyuncudan harf tahmini alır.
        
        Döndürür:
            Oyuncudan harf girdisi
        """
        harf = input(self.renklendir("Harf: ", Fore.GREEN)).strip()
        return harf
    
    def matematik_islem_secimi_al(self, kullanilabilir_islemler: List[str]) -> Optional[str]:
        """
        Oyuncudan matematik işlemi seçimini alır.
        
        Parametreler:
            kullanilabilir_islemler: Kullanılabilir işlem türlerinin listesi
            
        Döndürür:
            Seçilen işlem türü veya iptal edildiyse None
        """
        if not kullanilabilir_islemler:
            print(self.renklendir("Tüm işlemler kullanıldı!", Fore.RED))
            return None
        
        print(self.renklendir("\nMevcut işlemler:", Fore.CYAN, True))
        for indeks, islem in enumerate(kullanilabilir_islemler, 1):
            gosterim_adi = islem.capitalize()
            print(f"  {indeks}. {gosterim_adi}")
        print("  0. İptal")
        
        try:
            secim = input(self.renklendir("İşlem türü seçiniz (0-{0}): ".format(len(kullanilabilir_islemler)), Fore.WHITE))
            
            if secim == '0' or secim.lower() == 'iptal':
                return None
            
            secim_indeks = int(secim) - 1
            if 0 <= secim_indeks < len(kullanilabilir_islemler):
                return kullanilabilir_islemler[secim_indeks]
            else:
                print(self.renklendir("Geçersiz seçim!", Fore.RED))
                return None
                
        except ValueError:
            print(self.renklendir("Geçersiz giriş!", Fore.RED))
            return None
    
    def sayi_girdisi_al(self, istem: str) -> Optional[float]:
        """
        Doğrulama ile oyuncudan sayı girdisi alır.
        
        Parametreler:
            istem: Gösterilecek istem mesajı
            
        Döndürür:
            Float sayı veya geçersizse None
        """
        try:
            deger = input(self.renklendir(istem, Fore.WHITE))
            if deger.lower() == 'iptal':
                return None
            return float(deger)
        except ValueError:
            print(self.renklendir("Geçersiz sayı girişi!", Fore.RED))
            return None
    
    def mesaj_goster(self, mesaj: str, mesaj_tipi: str = 'bilgi'):
        """
        Türüne göre renkli bir mesaj gösterir.
        
        Parametreler:
            mesaj: Gösterilecek mesaj metni
            mesaj_tipi: Mesaj türü (basari, hata, bilgi, uyari)
        """
        renk_haritasi = {
            'basari': Fore.GREEN,
            'hata': Fore.RED,
            'bilgi': Fore.CYAN,
            'uyari': Fore.YELLOW
        }
        
        renk = renk_haritasi.get(mesaj_tipi, Fore.WHITE)
        
        if mesaj_tipi == 'basari':
            simge = "[OK]"
        elif mesaj_tipi == 'hata':
            simge = "[X]"
        elif mesaj_tipi == 'uyari':
            simge = "[!]"
        else:
            simge = "[i]"
        
        print(self.renklendir(f"{simge} {mesaj}", renk, True))
    
    def kazanma_mesajini_goster(self, hedef_kelime: str):
        """
        Kazanma mesajını gösterir.
        
        Parametreler:
            hedef_kelime: Tahmin edilen kelime
        """
        kazanma_banneri = f"""
        ╔════════════════════════════════════════════════╗
        ║                 TEBRIKLER!                     ║
        ║                                                ║
        ║          Kelimeyi dogru tahmin ettiniz!        ║
        ║              Kelime: {hedef_kelime.upper():^20}        ║
        ╚════════════════════════════════════════════════╝
        """
        print(self.renklendir(kazanma_banneri, Fore.GREEN, True))
    
    def kaybetme_mesajini_goster(self, hedef_kelime: str):
        """
        Kaybetme mesajını gösterir.
        
        Parametreler:
            hedef_kelime: Tahmin edilemeyen kelime
        """
        kaybetme_banneri = f"""
        ╔════════════════════════════════════════════════╗
        ║              😞 KAYBETTİNİZ! 😞                ║
        ║                                                ║
        ║           Hata hakkınız bitti!                ║
        ║           Doğru kelime: {hedef_kelime.upper():^20}     ║
        ╚════════════════════════════════════════════════╝
        """
        print(self.renklendir(kaybetme_banneri, Fore.RED, True))
    
    def puan_ozetini_goster(self, puan: int):
        """
        Final puanını gösterir.
        
        Parametreler:
            puan: Final puan değeri
        """
        print("\n" + "="*50)
        print(self.renklendir(f"Final Skorunuz: {puan} puan", Fore.MAGENTA, True))
        print("="*50 + "\n")


class HesaplamaVeAsmacaOyunu:
    """
    Tüm bileşenleri koordine eden ana oyun kontrolcüsü.
    """
    
    def __init__(self):
        """Oyunu gerekli tüm bileşenlerle başlat."""
        self.kelime_depo = KelimeDeposu()
        self.asmaca_cizici = AsmacaCizici(maksimum_hata=6)
        self.arayuz = ArayuzYoneticisi(renk_aktif=RENK_DESTEGI)
        self.puan_yoneticisi = PuanYoneticisi()
        self.matematik_motoru = None
        self.oyun_durum = None
        
    def yeni_oyun_baslat(self):
        """Yeni bir oyun oturumu kurar."""
        hedef_kelime, kategori = self.kelime_depo.rastgele_kelime_sec()
        self.oyun_durum = OyunDurumKontrolcusu(hedef_kelime, kategori, maksimum_hata=6)
        self.matematik_motoru = MatematikMotoru()
        self.puan_yoneticisi = PuanYoneticisi()
    
    def harf_tahmini_isle(self):
        """Oyuncunun harf tahmin eylemini işler."""
        harf = self.arayuz.harf_girdisi_al()
        basarili, mesaj = self.oyun_durum.harf_tahmin_et(harf)
        
        if basarili:
            self.arayuz.mesaj_goster(mesaj, 'basari')
            self.puan_yoneticisi.puan_degistir('dogru_harf')
        else:
            self.arayuz.mesaj_goster(mesaj, 'hata')
            # Yalnızca yanlış tahminde puan düş ve hata artır, doğrulama hatasında değil
            if harf in self.oyun_durum.hedef_kelime or harf in self.oyun_durum.denenen_harfler:
                pass  # Zaten işlenmiş veya doğrulama hatası
            else:
                self.puan_yoneticisi.puan_degistir('yanlis_harf')
    
    def matematik_islemi_isle(self):
        """Oyuncunun matematik işlemi eylemini işler."""
        kullanilabilir_islemler = self.matematik_motoru.kalan_islemleri_getir()
        
        if not kullanilabilir_islemler:
            self.arayuz.mesaj_goster("Tüm işlemler kullanıldı!", 'uyari')
            return
        
        islem_turu = self.arayuz.matematik_islem_secimi_al(kullanilabilir_islemler)
        
        if islem_turu is None:
            self.arayuz.mesaj_goster("İşlem iptal edildi.", 'bilgi')
            return
        
        # Kullanıcıdan sayıları al
        ilk_sayi = self.arayuz.sayi_girdisi_al(f"1. sayı ({islem_turu} için 'iptal' için): ")
        if ilk_sayi is None:
            self.arayuz.mesaj_goster("İşlem iptal edildi.", 'bilgi')
            return
        
        ikinci_sayi = self.arayuz.sayi_girdisi_al(f"2. sayı ({islem_turu} için 'iptal' için): ")
        if ikinci_sayi is None:
            self.arayuz.mesaj_goster("İşlem iptal edildi.", 'bilgi')
            return
        
        # Doğru cevabı hesapla
        dogru_cevap = self.matematik_motoru.hesapla(islem_turu, ilk_sayi, ikinci_sayi)
        
        # Sıfıra bölmeyi işle
        if dogru_cevap is None:
            self.arayuz.mesaj_goster("Hata: Sıfıra bölme yapılamaz!", 'hata')
            self.oyun_durum.hata_sayisini_artir()
            self.puan_yoneticisi.puan_degistir('yanlis_islem')
            return
        
        # Kullanıcının cevabını al
        sembol = self.matematik_motoru.islem_sembolleri[islem_turu]
        kullanici_cevap = self.arayuz.sayi_girdisi_al(
            f"Soru: {ilk_sayi} {sembol} {ikinci_sayi} = ? "
        )
        
        if kullanici_cevap is None:
            self.arayuz.mesaj_goster("İşlem iptal edildi.", 'bilgi')
            return
        
        # Cevabı doğrula
        if self.matematik_motoru.cevap_kontrol(kullanici_cevap, dogru_cevap):
            self.arayuz.mesaj_goster(f"Doğru! {ilk_sayi} {sembol} {ikinci_sayi} = {dogru_cevap}", 'basari')
            self.puan_yoneticisi.puan_degistir('dogru_islem')
            self.oyun_durum.bonus_puan_ekle()
            
            # Rastgele bir harf aç
            acilan_harf = self.oyun_durum.rastgele_harf_ac()
            if acilan_harf:
                self.arayuz.mesaj_goster(f"Bonus: '{acilan_harf}' harfi açıldı!", 'basari')
            else:
                self.arayuz.mesaj_goster("Tüm harfler zaten açık!", 'bilgi')
            
            # İşlemi kullanıldı olarak işaretle
            self.matematik_motoru.islemi_kullanildi_isaretle(islem_turu)
        else:
            self.arayuz.mesaj_goster(
                f"Yanlış! Doğru cevap: {dogru_cevap:.2f}", 'hata'
            )
            self.puan_yoneticisi.puan_degistir('yanlis_islem')
            self.oyun_durum.hata_sayisini_artir()
    
    def ipucu_eylemini_isle(self):
        """Oyuncunun ipucu isteği eylemini işler."""
        basarili, mesaj = self.oyun_durum.ipucu_kullan()
        
        if basarili:
            self.arayuz.mesaj_goster(mesaj, 'basari')
        else:
            self.arayuz.mesaj_goster(mesaj, 'uyari')
    
    def oyun_dongusunu_calistir(self):
        """Kazanma veya kaybetmeye kadar devam eden ana oyun döngüsü."""
        self.arayuz.oyun_basligini_goster()
        
        while True:
            # Mevcut durumu göster
            self.arayuz.oyun_durumunu_goster(self.oyun_durum, self.asmaca_cizici)
            
            # Kazanma koşulunu kontrol et
            if self.oyun_durum.kazanma_kontrolu():
                self.puan_yoneticisi.puan_degistir('kazanma_bonusu')
                self.arayuz.kazanma_mesajini_goster(self.oyun_durum.hedef_kelime)
                break
            
            # Kaybetme koşulunu kontrol et
            if self.oyun_durum.kaybetme_kontrolu():
                self.puan_yoneticisi.puan_degistir('kaybetme_cezasi')
                self.arayuz.kaybetme_mesajini_goster(self.oyun_durum.hedef_kelime)
                break
            
            # Seçenekleri göster ve seçim al
            self.arayuz.menu_seceneklerini_goster(self.matematik_motoru)
            secim = self.arayuz.oyuncu_secimini_al()
            
            # Seçimi işle
            if secim in ['h', 'harf']:
                self.harf_tahmini_isle()
            elif secim in ['i', 'işlem', 'islem']:
                self.matematik_islemi_isle()
            elif secim in ['ı', 'ipucu']:
                self.ipucu_eylemini_isle()
            elif secim in ['ç', 'c', 'cikis', 'çıkış', 'q', 'quit']:
                self.arayuz.mesaj_goster("Oyundan çıkılıyor...", 'bilgi')
                break
            else:
                self.arayuz.mesaj_goster("Geçersiz seçim! Lütfen tekrar deneyin.", 'uyari')
        
        # Final puanını göster
        final_puan = self.puan_yoneticisi.suanki_puani_getir()
        self.arayuz.puan_ozetini_goster(final_puan)
        
        # Puanı kaydet
        oyuncu_adi = input("Skorunuzu kaydetmek için isminizi girin (veya Enter): ").strip()
        if oyuncu_adi:
            self.puan_yoneticisi.puani_kaydet(oyuncu_adi)
            print("Skor kaydedildi!")
        
        # En yüksek puanları göster
        self.puan_yoneticisi.en_yuksek_puanlari_goster()
    
    def baslat(self):
        """Oyunu başlatır ve tekrar oynama mantığını yönetir."""
        print("\n" + "="*50)
        print("Oyuna hoş geldiniz!".center(50))
        print("="*50 + "\n")
        
        while True:
            self.yeni_oyun_baslat()
            self.oyun_dongusunu_calistir()
            
            # Tekrar oynama için sor
            tekrar = input("\nTekrar oynamak ister misiniz? (e/h): ").lower().strip()
            if tekrar not in ['e', 'evet', 'y', 'yes']:
                print("\nOynadığınız için teşekkürler! Görüşmek üzere!")
                break


def main():
    """Programın giriş noktası."""
    try:
        oyun = HesaplamaVeAsmacaOyunu()
        oyun.baslat()
    except KeyboardInterrupt:
        print("\n\nOyun kullanıcı tarafından sonlandırıldı. Görüşmek üzere!")
    except Exception as hata:
        print(f"\nBeklenmeyen bir hata oluştu: {hata}")
        print("Lütfen programı yeniden başlatın.")


if __name__ == "__main__":
    main()
