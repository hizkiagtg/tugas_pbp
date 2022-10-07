# Proyek Django  3 PBP oleh Hizkia Sebastian Ginting

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Pendahuluan

Repositori ini merupakan suatu repositori saya untuk mengunggah tugas saya dalam mata kuliah Pemrograman Berbasis Platform

## Link Aplikasi Heroku

Berikut link dari aplikasi Heroku yang sudah berhasil saya deploy

https://tugas1pbp.herokuapp.com/todolist/

## Kegunaan {% csrf_token %} pada Elemen Form
Cross-Site Request Forgery Attack token atau CSRF token merupakan suatu sistem pertahanan dengan random token, yang dapat mengatasi serangan CSRF. Adapun random token yang dibuat pada sistem ini harus bersifat unik dan berbeda pada tiap sesinya, sehingga akan sulit ditebak oleh peratas. Serangan CSRF itu sendiri merupakan suatu cara dari peretas untuk menyerang web yang kita buat, dengan beragam serangan-serangan yang berbahaya. Adapun csrf_token merupakan suatu sistem built in yang terdapat pada framework django, yang menerapkan sistem pertahan CSRF token. {% csrf_token %} akan dihasilkan saat merender halaman website, dan biasanya akan disisipkan pada hidden parameters dari suatu forms HTML. Token tersebut akan dikirim ke browser client. Sehingga, user yang mempunyai token tersebut dapat diautentikasi oleh website agar user tersebut dapat masuk ke dalam database.

## Apa yang terjadi bila tidak menggunakan {% csrf_token %} pada Elemen Form?

Bila tidak menggunakan csrf_token, maka user yang masuk tidak dapat diatuentikasi secara akurat. Kita tidak akan tahu persis, apakah user tersebut yang benar-benar login, atau merupakan peretas yang berpura-pura menjadi user. Selain itu, kemungkinan dapat terjadi pula serangan-serangan dari peretas menggunakan web.

## Apakah mungkin membuat table form secara manual?

Hal tersebut sangatlah memungkinkan. Berikut sintaks yang dapat digunakan untuk membuat table form secara manual:
```
  <table>
      <tr>
          <td>Username: </td>
          <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
      </tr>
              
      <tr>
          <td>Password: </td>
          <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
      </tr>

      <tr>
          <td></td>
          <td><input class="btn login_btn" type="submit" value="Login"></td>
      </tr>
  </table>
```

## Penjelasan Mengenai Alur Submisi Data pada Django

1. Awalnya, user akan mengisi isian form yang telah disediakan pada web. Di saat user menekan submit, maka akan terjadi request.
2. Server akan menerima HTTP request dengan method "POST". Akibat adanya token CSRF, maka akan dilakukan autentikasi terlebih dahulu.
3. Selanjutnya, akan terjadi proses routing menuju URL yang diinginkan, sesuai dengan tindakan yang dilakukan pada form tersebut.
4. Selanjutnya, akan membuat suatu instance dari model yang ada, sesuai dengan data yang telah dimasukkan pada form. Setelah itu, instance dari model tersebut akan dimasukkan ke dalam database.
5. Template akan melakukan pengaksesan terhadap data yang ada di database, dan kemudian akan menggunakan sesuai dengan kebutuhan.

## Implementasi Checklist
Berikut merupakan langkah-langkah yang saya lakukan untuk melakukan implementasi dalam proyek saya.

1. Untuk tahap pertama, saya harus membuat suatu app Django baru pada direktori saya, yang bernama mywatchlist. Berikut cara pembuatannya:
  ```py
    django-admin startapp todolist
  ```
2. Selanjutnya, akan menambahkan pada `INSTALLED_APPS` django-app yang baru dibuat pada `settings.py` di folder
`project_django`, kemudian menambakan pada `urlpatterns` pada `urls.py`, path dari app yang baru, dengan command:
  ```py
    urlpatterns = [
        ....
        path('todolist/', include('todolist.urls')),
    ]
  ```
3. Sesudah tahapan itu, maka akan dilakukan pembuatan model sesuai dengan atribut yang diinginkan pada tuga sini. Berikut model yang saya buat
  ```py
    class Task(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE) 
      date = models.DateField() 
      title = models.CharField(max_length=255)
      description = models.TextField()
      is_finished = models.BooleanField(default=False)
   ```
   Setelah tahapan membuat model, maka akan dilakukan migrasi model ke database dengan command ```python manage.py makemigrations``` dan ```python manage.py migrate```

4. Selanjutnya membuat function untuk halaman utama, register, login, logout beserta membuat task baru di views pada todolist. Adapun, berikut pasangan-pasangan dari fungsi yang bersesuaian (untuk lebih lengkapnya, dapat dilihat di views.py pada todolist):

halaman utama : ```show_todolist```

register      : ```register```

login         : ```login```

logout        : ```logout```

membuat task  : ```add_todolist```

5. Selanjutnya, akan membuat file html dan button yang bersesuaian. Untuk halaman utama, dapat dilihat di ```todolist.html```, dan button login beserta button add_todolist juga akan ditampilkan pada halaman tersebut. Untuk register akan terdapat pada ```register.html```, untuk login akan ditampilkan pada ```login.html```, serta untuk halaman add_todolist akan terdapat pada ```add_todolist.html```. Semua file tersebut terdapat pada folder templates.

6. Selanjutnya, tinggal mengatur proses routing dari semua halaman yang ada, pada fungsi urls.py, seperti berikut ini:
```
  urlpatterns = [
      path('', show_todolist, name='show_todolist'),
      path('register/', register, name='register'),
      path('login/', login_user, name='login'),
      path('create-task/', add_todolist, name='add_todolist'),
      path('logout/', logout_user, name='logout'),
      path('delete-task/<int:id>', deleted, name = 'deleted'),
      path('finished-task/<int:id>', finished, name = 'finished')
  ]
```

7. Selanjutnya, akan dilakukan proses deploy. Karena menggunakan nama proyek yang sama dengan tugas sebelumnya, maka hanya perlu melakukan command "heroku restart" pada cmd, lalu setelahnya melakukan re-running dari deployment yang ada pada github.

8. Selanjutnya, saya terlebih dahulu harus membuat 2 user, dengan cara meregristrasi terlebih dahulu pada pilihan form login. Username pertama yang saya buat adalah "hizkia123". Selanjutnya, saya memasukkan 3 pasang data todolist (title, description) pada pilihan "ADd New todolis". Berikut 3 data yang saya masukkan pada user "hizkia123":
![image](https://user-images.githubusercontent.com/92731992/192939817-43d4d95d-6e33-4b1f-adb3-e7d00eecbb68.png)
Selanjutnya, saya membuat username yang lain, yaitu "gtg123", dan melakukan proses yang sama seperti yang diatas. Berikut tampilan todolist yang saya buat untuk user tersebut:
![image](https://user-images.githubusercontent.com/92731992/192939987-1edce8eb-b048-4194-b291-d1bc682c45ba.png)

## Tambahan Pertanyaan Untuk Tugas 5
### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline CSS
Merupakan suatu format penulisan CSS di mana bagian-bagian dari CSS langsung menempel (sebagai attachment) pada kode/bagian dari HTML. Biasanya, style jenis ini akan terdapat dalam tag HTML dalam bentuk atribut. Kekurangan dari inline CSS yaitu dapat mempengaruhi ukuran halaman dan ukurusan download, serta lebih time-consuming untuk pembuatannya. Selain itu dapat membuat struktur HTML menjadi berantakan
2. Internal or Embedded CSS
Pada jenis CSS bagian ini, kita diharuskan untuk menambahkan tag <style> pada bagian <head> di dokumen HTML. Style jenis ini lumayan efektif untuk melakukan style di 1 halaman. Namun, akan memakan banyak waktu untuk membuat style ini di berbagai halaman di website. Kelebihan dari style ini adalah kita bisa menggunakan ID selectors, dan kekurangannya adalah akan menambah ukuran halaman dan waktu loading.
3. External CSS
External CSS mengharuskan kita untuk membuat suatu eksternal file CSS, yang nanti akan dipanggil dengan dengan menambahkan referesensi pada section head. Metode ini lebih efisien, terutama ketika ingin melakukan styling terhadap website yang besar. Dengan hanya menggunakan 1 file css saja, maka kita dapat mengubah seluruh situs web. Kelebihan dari metode ini memungkinkan kita untuk menggunakan kode HTML yang lebih jelas dan ukuran lebih kecil, karena CSS ditulis terpisah. Selain itu, kita dapat menggunakan styling yang sama di berbagai halaman. Adapun kekurangannya, halaman mungkin tidak dapat dirender secara normal selama eksternal CSS dapat di-load. Selain itu, melakukan upload atau linking berbagai CSS dapat meningkatkan kecepatan download dari situs.
  
### Sebutkan tag HTML5 yang kamu ketahui
```
 <html>     : Untuk membuat dokumen html
 <title>    : Untuk membuat judul dari halaman
 <body>     : Untuk membuat tubuh dari halaman
 <h1>-<h6>  : Untuk membuat heading
 <p>        : Untuk membuat paragraf
 <form>     : Untuk membuat suatu form
 <table>    : Untuk membuat suatu file
 <input>    : Berguna untuk mengambil input
 <button>   : Untuk membuat suatu tombol yang dapat di-klik
 <br>       : Untuk membuat suatu breakline (baris putus)

```
### Sebutkan CSS selector yang kamu ketahui
```
 .class              : 
   Untuk membuat suatu class, yang nanti bisa mengambil semua elemen dari class ="class" tersebut
 .class .subclass    : 
   Untuk membuat suatu class dan subclassnya, yang nantinya bisa mengambil dari elemen subclass, yang merupakan turunan dari class
 #id                 :
   Untuk memilih elemen dengan id = id
 *                   :
   Untuk memilih semua elemen
 [attribute]         :
   Untuk mengambil semua elemen, sesuai dengan atribut terget, dimana targetnya adalah "attribute"

```
### Implementasi dari Checklist
1. Kostumasi halaman untuk login, register, dan create-task

Untuk halaman-halaman tersebut, saya hanya menggunakan styling dengan internal CSS. Sehinggga, saya harus menyisipkan antara head, style-style yang ingin saya gunakan. Berikut salah satu syle yang saya buat (untuk create-task):

```
  <style>
      button {
          padding: 0.5rem;
          font-family: inherit;
          font-size: inherit;
          width: 100%;
          background-color: #3d6dab;
          color: rgb(0, 0, 0);
          padding: 14px 20px;
          margin: 8px 0;
          border: none;
          border-radius: 4px;
          cursor: pointer;
      }
      input[type=text], select {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
      }
  </style>
```
Untuk halaman todolist, saya juga menggunakan internal CSS untuk mebuat card, tetapi saya juga menambahkan bootsrap untuk navbar. Adapun untuk card nya, saya menggunakan flip card, dengan efek rotate ketika di hover. Di sini, class utama dari selector nya adalah.flip-card, yang memiliki beberapa kelas yang berhubungan, yang termasuk didalamnya mengatur halaman belakang (.flip-card-back) dan halaman depan (.flip-card-back).  Berikut tampilan kodenya:
```
    .flip-card {
        background-color: transparent;
        width: 500px;
        height: 175px;
        perspective: 1000px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
    }

    .flip-card-front {
    background-color: #bbb;
    color: black;
    }

    .flip-card-back {
        background-color: #bbb;
        color: white;
        transform: rotateY(180deg);
    }
```
2. Membuat halaman menjadi responsif

Untuk membuat halaman menjadi responsif, maka saya menambahkan Media Query pada setial internal CSS, pada setiap template HTML. Di sini, saya mengkostumasi agar halaman dapat dibuka diperangkat mobile (smartphone). Berikut tampilan kode Media Query nya:
```
  @media only screen and (max-width: 768px) {
      .container{
          margin: 30px;
          padding: 30px 40px;
          font-size: 0.8rem;
      }

  }
```
