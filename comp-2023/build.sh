#!/bin/bash

pandoc exercicios.md -o tmp.html

sed '/##exercicios##/q' templates/exercicios.html | head -n-1 > exercicios.html
cat tmp.html >> exercicios.html
sed -n '/##exercicios##/,$p' templates/exercicios.html | tail +1 >> exercicios.html

rm tmp.html
