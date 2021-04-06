#!/bin/bash

cd files


for i in *; do
  if [ "$i" != "in.pdf" ]; then
    rm -f "$i"
  fi
done
rm -f TUDO.zip

pdftk "in.pdf" burst

for i in pg_*.pdf; do
  pdftotext "$i";
done

for i in pg_*.txt; do
  name=$(cat "$i" | head -10 | tail -1 | cut -d' ' -f 2-)
  date=$(cat "$i" | head -8 | tail -1 | cut -d' ' -f 2 | sed 's$/$_$g')
  mv "${i%.txt}.pdf" "${date}_HOLERITE_${name// /_}.pdf"
done

rm *.txt
rm "in.pdf"
zip TUDO.zip *.pdf
