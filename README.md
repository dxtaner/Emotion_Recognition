
<body>
    <h1>Emotion Recognition </h1>
    <p>Bu proje, kullanıcının yüz ifadesine göre duygularını tanımlayan bir Emotion Recognition'si sağlar.</p>
  <h2>Başlangıç</h2>

<p>Bu yönergeler, projeyi yerel makinenizde çalıştırmak veya test etmek için size yol gösterecektir.</p>

<h3>Gereksinimler</h3>

<p>Bu projeyi çalıştırmak için aşağıdaki yazılım ve araçlara ihtiyacınız olacaktır:</p>

<ul>
    <li>Python 3.x</li>
    <li>OpenCV (Computer Vision Library)</li>
    <li>Tensorflow (Machine Learning Library)</li>
</ul>

<h3>Kurulum</h3>

<ol>
    <li>Bu repo'yu klonlayın:</li>

    <pre><code>git clone https://github.com/dxtaner/emotion_recognition.git</code></pre>

    <li>Gerekli paketleri yükleyin:</li>

    <pre><code>pip install opencv-python tensorflow</code></pre>

    <li>duygutanima.ipynb'yi çalıştırın:</li>

</ol>

<h2>Kullanım</h2>

<p>API, sadece bir JSON isteği alır ve JSON yanıtı döndürür. İstek, <code>image_url</code> alanını içermelidir ve analiz edilecek resmin URL'sini içermelidir.</p>

<p>API aşağıdaki duyguları tanıyabilir:</p>

<ul>
    <li>Mutlu</li>
    <li>Üzgün</li>
    <li>Kızgın</li>
    <li>Şaşkın</li>
    <li>Korkmuş</li>
    <li>Nötr</li>
</ul>

<p> sonuç olarak en yüksek güven skoruna sahip duyguyu döndürür.</p>
    
<h1>Eğitim Verisi için Ön İşleme</h1>
<p>Örnek sayısı: 28709</p>
<h2>Eğitim Verisi İçin Model Oluşturma</h2>
<p>Kullanılan model: Convolutional Neural Network (CNN)</p>
<h3>Model Yapısı</h3>
<ul>
  <li>1. Katman: 64 filtreli 3x3 boyutunda bir Conv2D katmanı</li>
  <li>2. Katman: 64 filtreli 3x3 boyutunda bir Conv2D katmanı</li>
  <li>3. Katman: 32 filtreli 3x3 boyutunda bir Conv2D katmanı</li>
  <li>4. Katman: 32 filtreli 3x3 boyutunda bir Conv2D katmanı</li>
  <li>5. Katman: 32 filtreli 3x3 boyutunda bir Conv2D katmanı</li>
  <li>Tam Bağlantı Katmanı: 128 nöronlu bir Dense katmanı</li>
  <li>Çıkış Katmanı: 7 nöronlu bir Dense katmanı</li>
</ul>
<h3>Model Eğitimi</h3>
<p>Eğitim süresi: 25 epoch</p>
<p>Batch boyutu: 100</p>
<h2>Test Verisi İçin Ön İşleme</h2>
<p>Test örnek sayısı: 3589</p>
<h2>Model Performansı</h2>
<p>Doğruluk (accuracy) değeri: 0.53</p>
<p>Kayıp (loss) değeri: 1.14</p>


