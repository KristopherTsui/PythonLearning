from pikepdf import Pdf

with Pdf.open('demo.pdf') as pdf:
    # Remove pages 2-3 labeled "second page" and "third page"
    del pdf.pages[1:3] 
    print(len(pdf.pages))
    pdf.save('output.pdf')