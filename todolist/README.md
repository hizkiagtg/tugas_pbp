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

4. Selanjutnya membuat function untuk halaman utama, register, login, logout beserta membuat task baru di views pada todolist. Adapun, berikut pasangan-pasangan dari fungsi yang bersesuaian (untuk lebih lengkapnya, dapat dilihat di views.py pada todolist)
halaman utama : ```py show_todolist```
register      : ```py register```
login         : ```py login```
logout        : ```py logout```
membuat task  : ```py add_todolist```

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
