from pikepdf import Pdf

with Pdf.open('demo.pdf') as my_pdf:
    # Rotate all pages in a file by 180 degrees
    for page in my_pdf.pages:
        page.Rotate = 180

    my_pdf.save('output.pdf')