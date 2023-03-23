#!/bin/bash

render() {
  file="$1"
  template="${2:-"templates/base.html"}"

  htmlfile="$1".html
  mdfile="$1".md

  pandoc "$mdfile" -o tmp.html

  sed '/##exercicios##/q' "$template" | head -n-1 > "$htmlfile"
  cat tmp.html >> "$htmlfile"
  sed -n '/##exercicios##/,$p' "$template" | tail +2 >> "$htmlfile"
  sed -i 's/Última modificação: .*$/Última modificação: '"$(date +%d-%m-%Y)/" "$htmlfile"

  rm tmp.html
}

render exercicios
render topicos
