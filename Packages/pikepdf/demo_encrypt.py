from pikepdf import Pdf, Permissions, Encryption

no_extracting = Permissions(extract=False)
with Pdf.open('demo.pdf') as pdf:
    pdf.save('output.pdf', encryption=Encryption(
            user="112358",
            owner="132134",
            allow=no_extracting
        )
    )