# Nihongo Harian

Aplikasi belajar bahasa Jepang dari nol sampai JLPT N4: timer 30 menit per hari, streak, grafik progres, hiragana & katakana dengan suara, latihan bicara lewat mikrofon, dan menu Ulangi untuk materi yang sering salah.

Buka di HP: https://rinji0906.github.io/nihongo-harian/ lalu pilih **Tambahkan ke layar utama** di menu Chrome.

## Struktur
- `src/app.html`: sumber aplikasi (satu file, juga dipakai untuk versi claude.ai).
- `build-pwa.sh src/app.html .`: membuat ulang `index.html` dari sumber.
- `manifest.webmanifest`, `sw.js`, `icon.svg`: agar bisa dipasang dan dipakai offline. Naikkan nama cache di `sw.js` setiap rilis.

Progres disimpan di perangkat (localStorage).
