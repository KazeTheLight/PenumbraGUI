🌑 Penumbra Flash Tool Pro v3.0 (GUI By Kaze) - Modern UI Edition

Penumbra GUI adalah solusi antarmuka grafis modern untuk engine Penumbra, dirancang khusus untuk menangani perangkat MediaTek (MTK) dengan keamanan tinggi dan navigasi yang mudah. Versi ini hadir dalam format Portable (.exe), serta dilengkapi dengan tampilan UI yang sepenuhnya direvitalisasi untuk pengalaman pengguna yang lebih imersif dan profesional.
✨ Fitur Unggulan

    Portable Engine: Langsung jalankan file .exe tanpa ribet instalasi library.
    Smart Backup: Satu klik untuk mengamankan partisi vital (NVRAM, NVDATA, EFS, PERSIST) guna menjaga IMEI dan sinyal.
    Dual-Method Flashing:
        PGPT Mode: Membaca struktur partisi langsung dari perangkat (Real-time).
        Scatter Mode: Menggunakan file scatter resmi dari firmware vendor.
    One-Click FRP Eraser: Menghapus kunci Akun Google melalui tab PGPT secara instan.
    Safety Lock: Opsi otomatis untuk Relock Bootloader dan Auto Reboot.
    🎨 Modern UI Revamp:
        Multi-Themed Interface: Pilih dari 11 tema visual berbeda (Dark Purple, Dark Blue, Cyberpunk, Matrix Green, Sunset Orange, Ocean Blue, Forest Green, Royal Purple, Vintage Brown, Retro Red, dan banyak lagi).
        Dynamic Title Colors: Judul utama "PENUMBRA TOOL" menyesuaikan warnanya secara otomatis dengan tema yang aktif.
        Card-Based Design: Desain modern dengan elemen-elemen berbentuk kartu (cards) untuk tampilan yang bersih dan rapi.
        Gradient Buttons: Tombol-tombol dengan efek gradien yang elegan dan interaktif.
        Animated Interactions: Efek hover, press, dan transisi yang halus untuk meningkatkan pengalaman pengguna.
        Iconic Labels: Ikon emoji yang intuitif di berbagai tombol dan label untuk navigasi yang lebih cepat.

📦 Persiapan Wajib (Prerequisites)

    Instalasi Driver (Sangat Penting):
        Masuk ke folder tool, cari file installdriver.bat.
        Klik Kanan → Run as Administrator.
        Tanpa langkah ini, perangkat Anda tidak akan terdeteksi di mode BROM.
    Kabel & Baterai:
        Gunakan kabel data original atau kualitas tinggi (hindari kabel magnetik).
        Pastikan daya baterai minimal 30–50%.
    Antivirus:
        Tambahkan folder tool ke Exclusion/Pengecualian Windows Defender atau antivirus pihak ketiga agar file engine tidak terhapus otomatis.

🚀 Panduan Lengkap Penggunaan (Usage)
Langkah 1: Inisialisasi Device

    Buka Penumbra_GUI.exe.
    Klik tombol LOAD DA dan pilih file Download Agent yang sesuai.
    Tips: Gunakan DAMT6789 untuk perangkat Helio G99/G100/G200.
    Hubungkan HP ke PC:
        Matikan HP sepenuhnya.
        Tekan dan tahan tombol Volume Atas + Volume Bawah.
        Colokkan kabel USB (Lepas tombol jika bar progres koneksi sudah berjalan).

Langkah 2: Memuat Daftar Partisi

    Metode PGPT (Direct): Klik tombol LOAD PGPT. Tool akan membaca tabel partisi langsung dari HP Anda. Daftar partisi akan muncul di tabel utama.
    Metode Scatter: Pindah ke tab Scatter Flasher, klik Load Scatter File, lalu pilih file .txt scatter dari firmware Anda.

Langkah 3: Operasi Flashing (Write)

    Pada daftar partisi yang muncul, Double-Click pada nama partisi yang ingin diisi (misal: boot, recovery, atau super).
    Pilih file .img yang sesuai dari komputer Anda.
    Klik tombol WRITE (atau FLASH SELECTED untuk scatter) untuk memulai proses pengisian data.
    ⚠️ Jika terjadi error di tengah proses flashing:
        Tahan tombol Power pada HP selama beberapa detik hingga perangkat mati.
        Cabut dan pasang kembali kabel USB.
        Pastikan driver BROM masih terdeteksi di PC.
        Lanjutkan proses flashing hanya untuk partisi yang gagal, tool akan melanjutkan dari file terakhir yang belum sukses.

Langkah 4: Operasi Backup (Read)

    Pilih partisi yang ingin dicadangkan dari daftar.
    Klik tombol READ. Tool akan meminta Anda memilih lokasi penyimpanan.
    Hasil backup akan tersimpan dengan nama asli partisi tersebut.

Langkah 5: Penyelesaian

    Jika ingin HP menyala otomatis setelah selesai, pastikan opsi Auto Reboot sudah dicentang sebelum menekan tombol Write/Read.
    Tunggu hingga muncul pesan "Operation Success" di Real-time Log.

❤️ Credits & Appreciation

    rama982 — DA for Transsion Devices G99/G100/G200 & Dimensity 8200.  
    Madam Shomy & Sir Roger For Making Antumbra (Core of This GUI)
    Testers — Device testing & validation community.  
    gutsmynuts AKA Kimela — Testing and DA.  
    Kaze — GUI Creator, Logic improvements, & customization.

⚠️ DISCLAIMER
Flashing partisi sistem memiliki risiko tinggi. Kami tidak bertanggung jawab atas kerusakan perangkat (Brick/Bootloop) akibat kelalaian pengguna.
Selalu lakukan SMART BACKUP sebelum melakukan modifikasi.