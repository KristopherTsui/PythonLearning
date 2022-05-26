from pikepdf import Pdf, OutlineItem

# Outline structure
with Pdf.open('demo.pdf') as pdf:
    with pdf.open_outline() as outline:
        # Creating outlines
        # Page counts are zero-based
        outline.root.append(OutlineItem('Basic theory', 0))
        main_item = OutlineItem('Generalized limits', 1)
        outline.root.append(main_item)
        main_item.children.append(OutlineItem('Definitions', 1))
        main_item.children.append(OutlineItem('Application:Stone-Cech compactification', 2))
        main_item.children.append(OutlineItem("Application:Tycheuoff's theorem", 3))
        outline.root.append(OutlineItem('Ultraproducts', 3))
        outline.root.append(OutlineItem('Two more perspectives on ultrafilters', 8))

    pdf.save('output.pdf')