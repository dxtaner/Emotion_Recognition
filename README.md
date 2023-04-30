
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


