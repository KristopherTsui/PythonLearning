from pikepdf import Pdf

# Split a PDF into single page PDFs
# It will not transfer some metadata associated with the PDF as a whole,
# such as the list of bookmarks
with Pdf.open('demo.pdf') as pdf:
    for n, page in enumerate(pdf.pages):
        dst = Pdf.new()
        dst.pages.append(page)
        dst.save(f"{n:02d}.pdf")