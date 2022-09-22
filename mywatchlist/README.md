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
### HTML

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
3
Untuk tahapan pertama, sebenarnya langkah yang dilakukan sama dengan tutorial lab 1. Awalnya, saya harus membuat suatu fungsi yang menerima request pada folder katalog, yang mengembalikan render(request, "katalog.html", context). Sebelumnya, di-assign di dalam fungsi show_katalog sebuah variabel context, yang berisi database, yang diwakilkan dengan variabel data_barang_katalog. Berikut tampilan kodenya:

  ```py
    def show_katalog(request):
        data_barang_katalog = CatalogItem.objects.all()
        context = {
            'list_katalog': data_barang_katalog,
            'nama': 'Hizkia Sebastian Ginting'
        }
        return render(request, "katalog.html", context)
  ```
2. Untuk membuat routing, langkah yang dilakukan adalah memodifikas urlpatterns yang terdapat pada urls.py pada folder project-django serta pada folder katalog.
Awalnya, pada urls.py pada project_django perlu ditambah route sebagai berikut:
  ```py
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('example_app.urls')),
      path('katalog/', include('katalog.urls'))
  ]
  ```
  Selanjutnya, pada urls.py pada katalog akan ditambahkan pada urlpatterns nya sebagai berikut:
  ```py
  urlpatterns = [
      path('', show_katalog, name='show_katalog'),
  ]
  ```
  Sesudah itu, proses routing akan berhasil
  
3. Untuk memetakan data ke html, perlu dilakukan modifikasi pada file katalog.html pada templates. Pemetaan datanya akan dilakukan dengan mengiterasi semua elemen yang ada pada list_katalog, dan semua database pada CatalogItem akan di-display. Berikut potongan kodenya:
```
    {% for elemen in list_katalog %}
        <tr>
            <th>{{elemen.item_name}}</th>
            <th>{{elemen.item_price}}</th>
            <th>{{elemen.item_stock}}</th>
            <th>{{elemen.description}}</th>
            <th>{{elemen.rating}}</th>
            <th>{{elemen.item_url}}</th>
        </tr>
    {% endfor %}
```
4. Untuk melakukan deployment ke heroku, langkah yang saya lakukan adalah membuat suatu app baru pada heroku terlebih dahulu. Pada kasus ini, saya membuat nama app nya sebagai 'tugas1pbp'. Selanjutnya, saya harus membuat suatu repositori secret pada Action Secrets di repositori github saya, yang akan menyimpan nama proyek pada 'HEROKU_APP_NAME', serta API Key pada 'HEROKU_API_KEY'. Selanjutnya, karena ada file dpl.yml pada procfile, deployment dapat berjalan sebagai mana mestinya dengan melakukan re-run workflows.
