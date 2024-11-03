# Paisa

Bu uygulama, kullanıcıların gelir ve giderlerini takip etmelerine yardımcı olan basit bir Tkinter uygulamasıdır. Uygulama, kullanıcıdan gelir ve gider tutarları, tarih ve açıklama girişi alarak bu bilgileri saklar ve gösterir.

## Özellikler

- Kullanıcıdan gelir ve gider tutarlarını girmesine olanak tanır.
- Gelir ve gider kayıtlarını tarih ve açıklama ile birlikte saklar.
- Mevcut kalan para miktarını görüntüler.
- Kullanıcı dostu arayüz ile basit bir kullanım deneyimi sunar.

## Gereksinimler

Uygulamanın çalışması için Python ve aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- Tkinter (Python ile birlikte gelir, ayrıca kurulum gerektirmez)
- Pandas (Gider ve gelir verilerini yönetmek için)

## Kurulum

1. Python'un bilgisayarınızda kurulu olduğundan emin olun. Python 3.x sürümü önerilmektedir.
2. Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisini açın ve aşağıdaki komutu çalıştırın:

   ```bash
   pip install pandas
   ```

- Bazı durumlarda `pip` komutu doğru çalışmayabiliyor. Böyle bir durumla karşılaşırsanız `pip3`, `pip3.11` veya `pip3.12` komutlarını deneyebilirsiniz.

## Kullanım

İki seçeneğiniz var:

1. Repoyu indirin. Reponun klasörü içindeyken terminal veya komut istemcisinde aşağıdaki komutu kullanın:

  ```bash
  python Paisa.py
  ```

- Yine duruma göre `python` komutu doğru çalışmayabilir. Böyle bir durumla karşılaşırsanız `python3`, `python3.11` veya `python3.12` komutlarını deneyebilirsiniz.

2. [Buraya](https://github.com/thecsa/Paisa/releases/download/Alpha/Paisa.exe) tıklayarak PyInstaller ile `.exe` olarak oluşturulmuş uygulamayı indirin ve çalıştırın.
