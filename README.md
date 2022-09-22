# Proyek Django PBP oleh Hizkia Sebastian Ginting

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Pendahuluan

Repositori ini merupakan suatu repositori saya untuk mengunggah tugas saya dalam mata kuliah Pemrograman Berbasis Platform

## Link Aplikasi Heroku

Berikut link dari aplikasi Heroku yang sudah berhasil saya deploy

https://tugas1pbp.herokuapp.com/katalog/

## Chart Tentang Request Clien ke Web Aplikasi Berbasi Django beserta responnya

![PBPChartFinal](https://user-images.githubusercontent.com/92731992/190302136-3c68b714-bb00-4427-ba18-2fd145550bcd.jpg)
Dari chart tersebut, terdapat beberapa proses. Berikut urutan prosesnya:
1. Awalnya, user mengirim suatu request dengan mengakses URL. Request tersebut kemudian akan di proses oleh manage.py, dan kemudian argumen yang di ekstrak akan diteruskan ke proses routing, yaitu menuju urls.py.
2. Terjadi proses routing di urls.py. Di sini request yang telah diproses sebelumnya akan diteruskan ke views yang sesuai.
3. Dari proses sebelumnya, terjadi penangkapan URL yang dikirim oleh user, dan URL akan mencari fungsi yang sesuai di views.py. Selanjutnya, terjadi pengaksesan dari view ke beberapa file.
4. Views (views.py) akan mengakses Model (models.py) dengan proses read/write, jika views ingin mengakses data dari database.
5. Models sebagai jembatan antara views dan database, di mana models-lah yang akan melakukan penulisan atau pembacaan data dari database, yang kemudian akan diteruskan kembali ke views.
6. Views (views.py) akan mencarikan suatu file berupa .html yang sesuai dengan request dari client pada folder templates.
7. File html yang telah diproses tersebut kemudian akan diteruskan kembali ke client sebagai bentuk response.

## Penjelasan tentang Virtual Environment dan Alasan Penggunaan
Virtualenv merupakan suatu environment pada Python, yang memungkinkan terjadinya isolasi dari lingkungan tersebut terhadap virtual environment lain, dan libraries Python lain yang terinstal pada sistem OS. Adapun beberapa alasan penggunaan dari virtualenv dalam proyek django adalah:

1. Virtual environment memungkinkan kita untuk menggunakan beberapa versi dari python beserta library dan modulnya di perangkat kita tanpa memubuat bentrok/kolisi antara setiap environment yang ada. Hal ini tentunya berguna bila kita mengerjakan beberapa proyek django yang mengharuskan kita dalam menggunakan versi python beserta libraries dan modul yang berbeda-beda di tiap proyeknya, dan tentunya dengan virtual environment tidak akan terjadi bentrok antara proyek django yang kita kerjakan

2. Masih tetap berhubungan dengan poin pertama, virtual environment memungkinkan kita untuk menjaga dependensi yang dibutuhkan antara proyek-proyek berbeda. Misalkan kita ingin mengerjakan beberapa proyek, salah satunya mengharuskan dengan versi 1.9, dan yang lainnya adalah 1.10. Dengan virtualenv, kita dapat menjaga dependensi dari kedua proyek.

3. Virtualenv lebih memudahkan kita dalam mengorganisasi proyek kita dan juga memudahkan kita untuk mengetahui lingkungan mana yang harus dijalankan bila di suatu kasus kita ingin menjalankan suatu proyek yang spesifik.

Untuk pertanyaan selanjutnya, tentang kemungkinan pembuatan aplikasi web dengan Django tanpa virtualenv, sebenarnya masih memungkinkan. Tetapi, dalam kasus ini, tentunya kita kehilangan kemampuan untuk menciptakan dan menjaga dependensi dari proyek-proyek Django yang kita buat, serta dalam kasus ini memungkinkan terjadinya bentrok dari antar proyek, yang tentunya bisa saja mengharuskan dalam penggunaan dependensi yang berbeda-beda. Misalkan, bila kita ingin  mengerjakan dua buah proyek, di mana sistem kita terinstal django versi 1.9 dan proyek 1 dan 2 secara berturut-turut mengharuskan versi django 1.9 dan 1.10, kita hanya bisa mengerjakan proyek 1 karena hanya proyek tersebut yang memungkinkan untuk digunakan di sistem kita, dengan tetap menjaga dependensi proyek tersebut.

## Implementasi langkah 1-4
Berikut merupakan langkah-langkah yang saya lakukan untuk melakukan implementasi dalam proyek saya.
1. Untuk tahapan pertama, sebenarnya langkah yang dilakukan sama dengan tutorial lab 1. Awalnya, saya harus membuat suatu fungsi yang menerima request pada folder katalog, yang mengembalikan render(request, "katalog.html", context). Sebelumnya, di-assign di dalam fungsi show_katalog sebuah variabel context, yang berisi database, yang diwakilkan dengan variabel data_barang_katalog. Berikut tampilan kodenya:
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
