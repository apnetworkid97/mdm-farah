# Manajemen Data Mahasiswa

Aplikasi web Python tanpa dependency eksternal untuk mengelola data mahasiswa dengan login, CRUD, file I/O JSON, search, sorting, OOP, regex validation, dan exception handling.

## Fitur

- Login page dengan akun demo `admin / admin123`
- Tambah, edit, hapus, dan tampilkan data mahasiswa
- Penyimpanan data ke file `data/students.json`
- OOP: class, object, encapsulation, inheritance, polymorphism
- Search: Linear Search, Binary Search, Sequential Search (linked list)
- Sorting: Bubble Sort, Selection Sort, Merge Sort
- Validasi input berbasis Regular Expression
- Error handling dengan `try`, `except`, dan custom exception
- Estimasi time complexity ditampilkan di dashboard

## Jalankan

```bash
python app.py
```
## Seeding / dummy data (default 1000)

```bash
py seed-students.py
```
## Seeding / dummy data (custom)

```bash
py seed-students.py 10000
```

## ENVIRONMENT

```bash
EMAIL_ADDRESS = from@gmail.com
EMAIL_PASSWORD = xxxx xxxx xxxx xxxx
```

Lalu buka `http://127.0.0.1:8000`.
