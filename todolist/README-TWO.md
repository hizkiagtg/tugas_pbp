# Proyek Django  3 PBP oleh Hizkia Sebastian Ginting - TUGAS 6

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Pendahuluan

Repositori ini merupakan suatu repositori saya untuk mengunggah tugas saya dalam mata kuliah Pemrograman Berbasis Platform

## Link Aplikasi Heroku

Berikut link dari aplikasi Heroku yang sudah berhasil saya deploy

https://tugas1pbp.herokuapp.com/todolist/

## Perbedaan antara  Asynchronous Programming dengan Synchronous Programming

Pada proses sinkronus, program yang dijalankan berjalan secara berurutan atau sekuensial. Sehingga, untuk menjalankan proses yang lain, harus mengikuti urutan (akan menunggu suatu proses untuk menjalankan proses lainnya). Hal ini berbeda dengan proses asinkronus, yang dimana program bisa menjalankan banyak proses yang berbeda secara bersamaan. Konsep ini mendukung parallelization, yang berarti proses pemecahan bagian sekuensial menjadi bagian-bagian yang terpisah dan saling lepas, sehingga dapat dijalankan secara bersamaan.

## Pengertian Event-Driven Programming beserta Contoh Penerapannya pada AJAX dan Javascript

Paradigma event-driven merupakan suatu paradigma yang menyatakan bahwa proses suatu program akan bergantung pada kejadian atau event yang diperoleh dari aksi/tindakan/action dari user.  Salah satu contoh penerapan yang umum di javascript adalah alert yang dapat muncul ketika menekan suatu tombol. Dalam kasus tersebut, event nya adalah alert, dan action nya adalah pressed button. Pada tugas ini sendiri, salah satu penerapan asinkronus function dapat dilihat dari fungsi getTodolist()

## Penerapan Proses Asinkronus pada Ajax

Dengan menggukan AJAX, akan terjadi proses pemrograman secara asinkronus. Pada dasarnya, AJAX akan memperoleh hasil kembalian data dari server dengan hasil dari pengolahan backend terlebih dahulu, yang dimana akan berjalan secara asinkronus. Data tersebut akan dapat dimanipulasi dalam bentuk HTML, tanpa adanya proses reloading. Sehingga, halaman akan menjadi lebih interaktif.

## Impelemtasi Checklist

### AJAX GET

1. Membuat view yang menampilkan task dalam JSON sebagai berikut:

    ```
    def show_json(request):
        data = Task.objects.filter(user = request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

    ```

2. Membuat path /todolist/json yang mengarah ke view sebagai berikut:

    ```
    urlpatterns = [
        ...
        path('json/', show_json, name='show_json'),
        ...
    ]

    ```

3. Melakukan pengambilan dengan AJAX GET

    ```
        async function getTodolist() {
            $.getJSON("json", function(data) {
                var todolistHTML = '';
                $.each(data, function (key, task) {
                    todolistHTML += getCard(task);
                });
                console.log(todolistHTML); 
                document.getElementById("content").innerHTML = todolistHTML;
            })
        }

    ```

### AJAX POST

1. Tombol untuk menambah todolist dengan modal sebagai berikut:

    ```
    <a class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modal-ajax">Create New Todolist</a>
    ```

2. View untuk menambah todolist dengan AJAX

    ```
    def add_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = datetime.now()
        description = request.POST.get('description')
        newTask = Task(
            user = request.user,
            date = date,
            title = title,
            description = description,
        )
        newTask.save()
        return HttpResponse(serializers.serialize("json",[newTask]), content_type="application/json")
    return HttpResponseNotFound()

    ```

3. Membuat suatu path untuk menambah todolist sebagai berikut:

    ```
    urlpatterns = [
        ...
        path('create-task/', add_todolist, name='add_todolist'),
        ...
    ]

    ```

4. Menghubungkan form dengan path, dapat dilakukan di modal, ketika button ditekan, maka akan menjalankan fungsi 

    ```
        <div class="modal fade" id="modal-ajax" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" >
                <div class="modal-content">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add Your New Todolist</h1>
                    <div class="modal-body">
                        <form id="taskForm" method="POST">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="title" class="col-form-label">Title</label>
                                <input type="text" name="title" class="form-control" id="title" required>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description</label>
                                <textarea class="form-control" id="description"  name="description" required></textarea>
                            </div>
                            
                        </form>
                        <button id="submit-task" class="btn btn-primary" onclick="submitNewTask(taskForm)">Submit Todolist</button>
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    ```
    Ketika Submit Todolist ditekan, maka akan menjalankan submitNewTask yang mengarah ke path tersebut. Adapun fungsinya sebagai berikut:
    ```
    function submitNewTask(taskForm) {
        $.post("create-task/", $(taskForm).serialize(), function(data){
            document.getElementById("content").innerHTML += getCard(data[0]);
        });
    }
    ```

5. Untuk refresh tanpa reload seluruh halaman sudah dihandle di submitNewTask, karena ada modifikasi inner HTML tanpa reload. 