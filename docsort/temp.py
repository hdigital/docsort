'''
Created on 02.04.2024

@author: neumann
'''
import fitz
import easyocr
import os
import shutil
import glob

scanspath = 'scans'
docspath = 'docs'

companies= ["Pydev", "Verein", "Montag", "docsort"]
pdffiles = glob.glob(os.path.join(scanspath, "*.pdf"))
reader = easyocr.Reader(["de", "en"])

for pdfpathname in pdffiles:
    pdfname = pdfpathname.split("\\")[-1]

    doc = fitz.open(os.path.join(scanspath, pdfname))
    page = doc.load_page(0)
    page.clean_contents()
    print(len(page.get_text()))
    if len(page.get_text())<100: 
        pixmap = page.get_pixmap(dpi=288)
        img = pixmap.tobytes()
        result = reader.readtext(img)
    
        pathname = ""
        for p, text,x  in result:
            page.insert_text((p[3][0]/4, p[3][1]/4), text, fontsize=10, stroke_opacity=0.0, fill_opacity=0.0)
            if text in companies and not pathname:
                if not os.path.isdir(os.path.join(docspath, text)):
                    os.makedirs(os.path.join(docspath, text), exist_ok=True)
                pathname = text
        doc.save(os.path.join(docspath, pathname, pdfname))
    else:
        if page.get_text() in companies:
            print(f"copy '{pdfname}'")
            

















"""
for i, info in enumerate(doc.pages()):
    print(info)
    page = doc.load_page(i)
    
    for _, text, _ in result:
        print(text)
"""

