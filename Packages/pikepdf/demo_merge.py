from pikepdf import Pdf, OutlineItem
from glob import glob

# Add an entry for each file in a merged document automatically
pdf = Pdf.new()

page_count = 0
with pdf.open_outline() as outline:
    for file in glob('0*.pdf'):
        with Pdf.open(file) as src:
            oi = OutlineItem(file, page_count)
            outline.root.append(oi)
            page_count += len(src.pages)
            pdf.pages.extend(src.pages)

pdf.save('output.pdf')