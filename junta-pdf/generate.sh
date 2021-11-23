#!/bin/bash

cd files
for i in *; do
  if [ "$i" != "in1.pdf" -a "$i" != "in2.zip" ]; then
    rm -f "$i"
  fi
done
rm -f TUDO.zip



mkdir -p 2
mv in2.zip 2
cd 2; unzip in2.zip; rm in2.zip; cd ..


for i in 2/*; do
  pdftk in1.pdf "$i" cat output "$(basename "$i")"
done

rm -rf 2
rm "in1.pdf"
zip TUDO.zip *

