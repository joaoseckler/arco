#!/usr/bin/env python3

# The server only runs python 3.5, so don't use f-strings!

from fpdf import FPDF
import csv
import requests

output_pdf_file = 'etiquetas.pdf'

#### PDF definitions ####

box_w = 65
box_h = 25

gap = 1.2
margin_top = 9.5
margin_sides = 6.5

title_font_size = 10
info_font_size = 8

COLORS = {
        'pink': (255,20,147),
        'vermelho': (255,0,0),
        'verde': (0,255,0),
        'azul esc.': (0,0,255),
        'azul claro': (173,216,230),
        'preto': (0,0,0),
        'laranja': (255,140,0),
        'amarelo': (255,255,0),
        'cinza': (150,150,150),
        'marrom': (110, 38, 14),
        '': (255, 255, 255),
        }

#########################

def get_color(cor):
    return COLORS[cor.lower().strip()]

class PDF(FPDF):
    n_labels = 0


    def walk(self, x, y):
        self.set_xy(self.get_x() + x, self.get_y() + y)

    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_font('Helvetica', '', title_font_size)
        self.set_margins(margin_sides, margin_top)
        self.new_page()
        self.set_auto_page_break(0)

    def new_page(self):
        self.add_page()
        self.set_xy(margin_sides, margin_top)

    def label(self):
        '''Creates label box and returns original position'''
        x, y = self.get_x(), self.get_y()

        self.n_labels += 1

        ln = 0
        if (self.n_labels % 3) == 0:
            ln = 1

        if (self.n_labels % 33) == 1 and self.n_labels != 1:
            self.new_page()
            x, y = self.get_x(), self.get_y()

        self.cell(box_w, box_h, ln = ln, border=1)

        if ln:
            self.walk(0, gap)
        else:
            self.walk(gap, 0)

        return x, y

    def circle(self, w, h, border = 0, style = 'F', align="L"):
        ''' Behaves like cell but draws a circle'''
        r = min(w, h)
        assert r > 0, "Negative radius. Maybe border is too big"

        original = self.get_x(), self.get_y()

        if align == "C":
            if w < h:
                d = h - w
                self.walk(border, d/2 + border)
            else:
                d = w - h
                self.walk(d/2 + border, border)
        else:
            self.walk(border, border)

        self.ellipse(
                self.get_x(),
                self.get_y(),
                r - 2*border,
                r - 2*border,
                style)
        self.set_xy(original[0] + w, original[1])

    def entrada(self, tombo, autor, exemplar, loc, titulo, cor, secao):
        w0 = box_w/4.5
        w1 = box_w/5.5
        w2 = box_w - w1 - w0
        h = box_h/3


        xy_label = self.label()
        original_xy = self.get_x(), self.get_y()
        self.set_xy(*xy_label)

        self.set_font_size(info_font_size)
        self.cell(w0, h, ln=0, txt=tombo, border= "R")
        self.cell(w1, h, ln=0, txt=loc)

        self.set_font_size(title_font_size)
        self.cell(w2, h, ln=2,
                txt=autor[:self.n_chars_multi_cell(autor, w2, h, max_lines = 1)]
                )
        self.walk(-w0 - w1, 0)

        self.set_font_size(info_font_size)
        self.cell(w0, h, ln=0, txt=exemplar, border="R")
        self.cell(w1, h, ln=2, txt=secao)

        self.walk(-w0, 0)
        self.set_font_size(info_font_size)
        self.cell(w0, h, ln=0, txt=cor, border="R")

        self.set_fill_color(*get_color(cor))
        self.circle(w1, h, 1)
        self.set_fill_color(0, 0, 0)

        self.walk(0, -h)
        self.set_font_size(title_font_size)
        self.multi_cell(w2, h/2, align = "L",
                txt=titulo[:self.n_chars_multi_cell(titulo, w2, h/2)]
                )

        self.set_xy(*original_xy)

    def n_chars_multi_cell(self, string, w, h, max_lines = 4):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Helvetica', '', title_font_size)

        for i in range(len(string)):
            pdf.set_xy(0, 0)
            pdf.multi_cell(w, h, align = "L", txt=string[:i])
            if pdf.get_y() > max_lines * h:
                break
        else:
            i = len(string) + 1

        return i - 1

pdf = PDF()
# pdf.image('etiqueta-referencia.png', 0, 0, 210, 297)

def treat_color(c):
    if c.lower() == 'azul escuro':
        return 'Azul esc.'
    elif c.lower() == 'azul claro':
        return 'Azul claro'
    return c

def treat_section(s):
    if s.lower() == 'hqs':
        return 'HQs'
    else:
        return s.title()



tombo = '949$a'
autor = '100$q'
loc = '090$b'
titulo = '245$a'
cor =  '090$c'
secao = '090$a'
n_exemplares = '562$e'

url = 'https://docs.google.com/spreadsheets/d' \
      '/1nQFe_ZYNsUMopK6SQJWklHCHt96bSzwB-LTgry6J0WI' \
      '/export?gid=1318123784&format=csv'

print("Requesting data from sheet...", end=" ")
csv_data = requests.get(url).content.decode('utf-8') \
           .replace('\r', '').split('\n')
print("Done.")


for entry in csv.DictReader(csv_data):
    ex = 1

    if entry[tombo] and (entry[loc] or entry[titulo]):
        try:
            n = int(entry[n_exemplares])
        except ValueError:
            n = 1
        for i in range(n):
            pdf.entrada(
                    entry[tombo],
                    entry[autor],
                    'Ex. ' + str(n),
                    entry[loc],
                    entry[titulo].rstrip(' /-'),
                    treat_color(entry[cor]),
                    treat_section(entry[secao]),
                    )
    else:
        print("ignorando entrada " +  entry[titulo] + " - " + entry[autor] + "...")

pdf.output(output_pdf_file)
