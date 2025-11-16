# GitHub'a Yükleme Talimatları

Bu dosya, projeyi GitHub'a nasıl yükleyeceğinizi adım adım açıklar.

## Ön Hazırlık

1. GitHub hesabınıza giriş yapın: https://github.com
2. Git'in bilgisayarınızda kurulu olduğundan emin olun

Git kurulu mu kontrol etmek için:
```bash
git --version
```

## Adım 1: GitHub'da Yeni Repo Oluşturun

1. GitHub'da sağ üstteki "+" işaretine tıklayın
2. "New repository" seçin
3. Repository bilgilerini doldurun:
   - **Repository name**: `calc-and-hang-game` (veya istediğiniz bir isim)
   - **Description**: "An educational word game combining hangman with mathematical operations"
   - **Public** veya **Private** seçin
   - **Initialize this repository with a README** seçeneğini ISARETLEMEYIN (bizim zaten README'miz var)
4. "Create repository" butonuna tıklayın

## Adım 2: Projeyi Git'e Ekleyin

Terminal veya PowerShell'de proje klasörüne gidin:

```bash
cd C:\Users\Alperen\Desktop\ödev
```

Git repository'sini başlatın:

```bash
git init
```

Tüm dosyaları ekleyin:

```bash
git add .
```

İlk commit'i yapın:

```bash
git commit -m "Initial commit: Calc & Hang game with tests and documentation"
```

## Adım 3: GitHub'a Yükleyin

GitHub'daki repo'nuzu bağlayın (URL'i kendi repo URL'inizle değiştirin):

```bash
git remote add origin https://github.com/KULLANICI_ADINIZ/calc-and-hang-game.git
```

Ana branch ismini değiştirin (modern GitHub standart olarak 'main' kullanır):

```bash
git branch -M main
```

Kodu GitHub'a yükleyin:

```bash
git push -u origin main
```

## Adım 4: Doğrulama

1. GitHub repo sayfanızı yenileyin
2. Tüm dosyaların yüklendiğini kontrol edin:
   - ✓ README.md
   - ✓ PROJE_RAPORU_TESLIM.md
   - ✓ requirements.txt
   - ✓ .gitignore
   - ✓ src/calc_and_hang_game.py
   - ✓ tests/test_calc_and_hang.py

## Proje Yapısı (GitHub'da Görünecek)

```
calc-and-hang-game/
├── .gitignore
├── README.md
├── PROJE_RAPORU_TESLIM.md
├── GITHUB_YUKLEME.md
├── requirements.txt
├── src/
│   └── calc_and_hang_game.py
└── tests/
    └── test_calc_and_hang.py
```

## Sonraki Değişiklikler İçin

Kod değişikliği yaptıktan sonra:

```bash
# Değişiklikleri ekle
git add .

# Commit yap (açıklayıcı mesaj yazın)
git commit -m "Açıklama: Ne değiştirdiniz"

# GitHub'a yükle
git push
```

## Sorun Giderme

### "git: command not found" hatası

Git kurulu değil. İndirin: https://git-scm.com/downloads

### "Permission denied" hatası

SSH key kurmanız gerekebilir veya HTTPS ile authentication yapın:
```bash
git config --global user.name "İsminiz"
git config --global user.email "email@example.com"
```

### "Repository not found" hatası

Remote URL'i kontrol edin:
```bash
git remote -v
```

Yanlışsa düzeltin:
```bash
git remote set-url origin https://github.com/KULLANICI_ADINIZ/calc-and-hang-game.git
```

## GitHub'da README Görünümü

GitHub, otomatik olarak README.md dosyanızı ana sayfada gösterecektir. Bu dosya:
- Proje açıklaması
- Kurulum talimatları
- Kullanım örnekleri
- Test bilgileri
- Proje yapısı

hepsini içerir ve ziyaretçilere profesyonel bir görünüm sunar.

## İpuçları

1. **Anlamlı commit mesajları yazın**: "Fix bug" yerine "Fix letter validation in GameStateManager"
2. **.gitignore'u kontrol edin**: Gereksiz dosyalar (\_\_pycache\_\_, .vscode, vb.) yüklenmiyor
3. **README'yi güncel tutun**: Yeni özellik eklerseniz README'yi de güncelleyin
4. **Testleri çalıştırın**: Push yapmadan önce testlerin geçtiğinden emin olun

## Projeyi Klonlamak (Başka Bir Bilgisayarda)

```bash
git clone https://github.com/KULLANICI_ADINIZ/calc-and-hang-game.git
cd calc-and-hang-game
pip install -r requirements.txt
python src/calc_and_hang_game.py
```

---

**Not**: Bu talimatlar projenizi GitHub'a yüklemeniz için hazırlanmıştır. Sorularınız olursa GitHub documentation'a bakabilirsiniz: https://docs.github.com

