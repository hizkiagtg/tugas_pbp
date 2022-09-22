# Proyek Django  3 PBP oleh Hizkia Sebastian Ginting

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Pendahuluan

Repositori ini merupakan suatu repositori saya untuk mengunggah tugas saya dalam mata kuliah Pemrograman Berbasis Platform

## Link Aplikasi Heroku

Berikut link dari aplikasi Heroku yang sudah berhasil saya deploy

Versi HTML:
https://tugas1pbp.herokuapp.com/mywatchlist/html/

Versi XML:
https://tugas1pbp.herokuapp.com/mywatchlist/xml/

Versi JSon:
https://tugas1pbp.herokuapp.com/mywatchlist/json/

## Perbedaan antara JSON, XML, dan HTML

### XML (Extensible Markup Language)
XML merupakan suatu conth format data delivery yang bersifat self-descriptive, sehingga dengan membaca XML, diharapkan agar dapat mengerti informasi yang tertulis. Berbeda dengan HTML dan JSON, data yang berada pada XML berbentuk value yang dibungkus dalam tag berisi key. Selain itu, perbedaan lain XML dengan HTML dan JSON adalah strukturnya yang berupa tree, sehingga akan terdapat root, branch, yang kemudian berakhir pada leaves. Dibandingkan dengan JSON, format XML akan menampung ukuran data yang lebih besar dari pada JSON, karena formatnya yang berupa tree.

Contoh XML:
  ```
    <?xml version="1.0" encoding="UTF-8"?>
    <phone>
        <brand>Samsung</brand>
        <type>Samsung S20 FE</type>
        <memory>256</memory>
    </phone>
  ```

### JSON (JavaScript Object Notation)
Persamaan JSON dengan XML adalah sama-sama bersifat self-descriptive. Tipe data delivery ini biasanya digunakan dalam mobile dan web, serta sintaks-nya merupakan turunan dari javascript. Berbeda dengan XML dan JSON, data yang dibungkus harus berupa pasangan key dan juga value (seperti dictionary pada python). Selain itu, sintaks dari JSON juga relatif lebih mudah dipahami daripada XML, serta ukurannya datanya juga lebih kecil karena hanya berisi pasangan key dan value.

Contoh XML:
  ```
    {
        "brand": "Samsung",
        "type": "S21",
        "color": "Black",
    }
  ```
### HTML (HyperText Transfer Protocol)
HTTP merupakan suatu protokok, di mana didalamnya bisa menampilkan halaman-halaman web, dan berbeda dengan JSON dan XML, HTML dapat digunakan untuk melakukan transaksi antara client dengan server. Sehingga, perbedaan utama dari HTML dengan JSON serta XML, HTML sendiri dapat ditampilkan pada web browser dan memungkinkan adanya interaksi antara client dengan server, sedangkan XML dan JSON lebih kepada penyimpanan dan transfer data (data delivery). Selain itu, HTML juga bersifat stateless, atau independen.

## Mengapa Harus Menggunakan Data Delivery?
Di kehidupan nyata, tentunya sangat membutuhkan proses pengolahan data baik itu pengaksesan maupun transfer data. Selain itu, tentunya di dalam pemrograman berbasis platform, akan membutuhkan mekanisme akses database yang dapat berinteraksi dengan pengguna. Sehingga, tentunya data delivery sangat krusial karena user sendiri sangat membutuhkan data dan pengolahannya. Bila tidak ada hal tersebut, maka tentunya sia-sia proses pengaksesan platform oleh user, karena mereka tidak dapat mengakses data yang mereka inginkan. Selain itu, dalam prakteknya, tentunya tiap proses data delivery membutuhkan jenis yang berbeda. Misalkan ketika ingin mengakses halaman, maka akan digunakan HTML, dan ketika HTML melakukan request data, akan dapat dikembalikan menggunakan XML ataupun JSON. Dari proses tersebut, dapat dilihat bahwa proses data delivery sangat krusial

## Implementasi Checklist
Berikut merupakan langkah-langkah yang saya lakukan untuk melakukan implementasi dalam proyek saya.

1. Untuk tahap pertama, saya harus membuat suatu app Django baru pada direktori saya, yang bernama mywatchlist. Berikut cara pembuatannya:
  ```py
    django-admin startapp mywatchlist
  ```
2. Selanjutnya, akan menambahkan pada `INSTALLED_APPS` django-app yang baru dibuat pada `settings.py` di folder
`project_django`, kemudian menambakan pada `urlpatterns` pada `urls.py`, path dari app yang baru, dengan command:
  ```py
    urlpatterns = [
        ....
        path('mywatchlist/', include('mywatchlist.urls')),
    ]
  ```
3. Sesudah tahapan itu, maka akan dilakukan pembuatan model sesuai dengan atribut yang diinginkan. Berikut model yang saya buat
  ```py
    class MyWatchList(models.Model):
        title = models.CharField(max_length=255)
        watched = models.BooleanField() 
        rating = models.IntegerField(validators= 
                        [MaxValueValidator(5), MinValueValidator(1)])
        release_date = models.DateField()
        review = models.TextField()
   ```
Dalam hal ini, saya membuat watched sebagai boolean, karena hanya memiliki dua kemungkinan, yaitu sudah pernah ditonton atau tidak (true/false). Selain itu, saya juga membatasi nilai dari rating dari 1-5 (inklusif).
5. Sesudah itu, saya tinggal membuat fungsi pada views di mywatchlist, yang akan mengembalikanpada render untuk html, serta akan menampilkan HTTPResponse untuk XML dan JSON. Sesudah itu, akan ditambahkan route nya pada urlpatterns di urls.py, sebagai berikut:
```py
  urlpatterns = [
      path('html/', show_watchlist, name='show_watchlist'),
      path('xml/', show_xml, name= 'show_xml'), 
      path('json/', show_json, name='show_json'),
  ]
```
6. Selanjutnya, tinggal dibuat suatu templete HTML, yang akan memetakan semua data pada model. Adapun pemetaannya sebagai berikut:
```
    {% for watchlist in list_watchlist %}
        <tr>
            <th>{{watchlist.title}}</th>
            <th>{{watchlist.watched}}</th>
            <th>{{watchlist.rating}}</th>
            <th>{{watchlist.release_date}}</th>
            <th>{{watchlist.review}}</th>
        </tr>
    {% endfor %}
```
7. Selanjutnya, akan dilakukan proses deploy, dengan mengubah procfile terlebih dahulu. Di sini, link untuk deploy akan sama dengan tugas minggu lalu, tetapi tinggal di jalankan ulang di github (agar melakukan deploy ulang).

## POSTMAN
### Versi HTML
![image](https://user-images.githubusercontent.com/92731992/191651416-381de771-879a-42b1-a0e5-7f680904fa8a.png)
### Versi XML
![image](https://user-images.githubusercontent.com/92731992/191651513-71af0a3b-bd81-4210-9881-7fa363a39d76.png)
### Versi JSON
![image](https://user-images.githubusercontent.com/92731992/191651592-598ef852-be93-4bf6-8b0b-2e7267cbd827.png)

