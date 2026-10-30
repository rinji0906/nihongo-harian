# Nihongo Harian

Aplikasi belajar bahasa Jepang dari nol sampai JLPT N4: timer 30 menit per hari, streak, grafik progres, hiragana & katakana dengan suara, latihan bicara lewat mikrofon, kurikulum N5 (kosakata, kanji, tata bahasa) dengan kartu SRS, rencana mingguan, dan menu Ulangi.

Buka di HP: https://rinji0906.github.io/nihongo-harian/ lalu pilih **Tambahkan ke layar utama** di menu Chrome.

## Struktur
- `src/app.html`: sumber aplikasi.
- `src/data/*.js`: materi (kosakata, kanji, tata bahasa). Format dijelaskan di baris pertama tiap file.
- `python3 build.py`: membuat `index.html` (GitHub Pages) dan `dist/artifact.html` (versi claude.ai).
- `manifest.webmanifest`, `sw.js`, `icon.svg`: agar bisa dipasang dan dipakai offline. Naikkan nama cache di `sw.js` setiap rilis.

Progres disimpan di perangkat (localStorage).
