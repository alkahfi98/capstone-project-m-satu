# capstone-project-m-satu


# SISTEM INFORMASI BANDARA INTERNASIONAL PURWADHIKA

Sistem ini adalah program untuk manajemen informasi penerbangan, maskapai, rute, dan terminal di Bandara Internasional Purwadhika. Aplikasi ini menyediakan berbagai fitur untuk mengelola informasi penerbangan dan informasi terkait maskapai, rute, maupun terminal.

## Data tabel
| Variabel                     | Tipe Data       | Deskripsi                                                             |
|------------------------------|-----------------|----------------------------------------------------------------------|
| `info_penerbangan`            | List            | Daftar informasi penerbangan yang kosong pada awalnya                |
| `info_maskapai`               | List            | Daftar maskapai yang tersedia, masing-masing merupakan string         |
| `rute_domestik`               | Dictionary      | Dictionary berisi maskapai sebagai kunci dan rute domestik (list) sebagai nilai |
| `rute_internasional`          | Dictionary      | Dictionary berisi maskapai sebagai kunci dan rute internasional (list) sebagai nilai |
| `terminal_maskapai`           | Dictionary      | Dictionary berisi maskapai sebagai kunci dan terminal (string) sebagai nilai  |
| `terminal_maskapai_domestik`  | Dictionary      | Dictionary yang sama dengan `terminal_maskapai`, untuk rute domestik  |
| `terminal_maskapai_internasional` | Dictionary  | Dictionary yang sama dengan `terminal_maskapai`, untuk rute internasional |



## Fitur Utama

1. **Login Manager**: 
   - Login untuk manajer dengan ID dan password yang telah ditentukan.

2. **Menu Penumpang**: 
   - **Lihat Info Penerbangan**: Menampilkan daftar penerbangan yang tersedia.
   - **Lihat Maskapai, Rute, Terminal**: Menampilkan informasi tentang maskapai, rute penerbangan, dan terminal.
   - **Sorting Maskapai, Rute, Terminal**: Mengurutkan data maskapai, rute, dan terminal berdasarkan pilihan pengguna.

3. **Menu Manager**:
   - **Info Penerbangan**: 
     - **Lihat Info Penerbangan**: Menampilkan data penerbangan.
     - **Tambah Info Penerbangan**: Menambahkan penerbangan baru.
     - **Hapus Info Penerbangan**: Menghapus penerbangan berdasarkan nomor.
     - **Ubah Info Penerbangan**: Mengubah detail penerbangan yang sudah ada.
   - **Maskapai, Rute, dan Terminal**:
     - **Tampilkan Data**: Menampilkan informasi maskapai, rute, dan terminal.
     - **Tambah Data**: Menambahkan maskapai, rute, dan terminal baru.
     - **Hapus Data**: Menghapus maskapai, rute, dan terminal.
     - **Ubah Data**: Mengubah informasi maskapai, rute, dan terminal.
     - **Sorting Data**: Mengurutkan data maskapai, rute, dan terminal.



