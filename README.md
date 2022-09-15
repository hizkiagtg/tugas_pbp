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
