#!/bin/bash

name="$1"
template="${2:-"templates/base.html"}"

htmlfile="$name".html
mdfile="$name".md

pandoc "$mdfile" -o tmp.html

sed '/##exercicios##/q' "$template" | head -n-1 > "$htmlfile"
cat tmp.html >> "$htmlfile"
sed -n '/##exercicios##/,$p' "$template" | tail +2 >> "$htmlfile"
sed -i 's/Última modificação: .*$/Última modificação: '"$(date +%d-%m-%Y)/" "$htmlfile"

if [[ "$name" =~ / ]]; then
  sed -i 's|##rel##|../|' "$htmlfile"
else
  sed -i 's|##rel##||' "$htmlfile"
fi

if [[ "$name" =~ /index ]]; then
  sed -i 's|##foot##|../|' "$htmlfile"
else
  sed -i 's|##foot##||' "$htmlfile"
fi

rm tmp.html

