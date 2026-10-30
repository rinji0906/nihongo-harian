#!/bin/bash
# Bungkus nihongo-harian.html menjadi index.html PWA mandiri. Pakai: build-pwa.sh <sumber.html> <folder-tujuan>
SRC=$1; OUT=$2
{ printf '<!doctype html>\n<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<link rel="manifest" href="manifest.webmanifest"><meta name="theme-color" content="#22427A"><link rel="icon" href="icon.svg"><link rel="apple-touch-icon" href="icon.svg">\n<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}</style></head><body>\n'
cat "$SRC"
printf '\n<script>if("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(()=>{});</script>\n</body></html>\n'; } > "$OUT/index.html"
