import os
from PyPDF2 import PdfFileReader, PdfFileWriter


class PdfSplitter:
    def split(self, path: str):
        print("PATH:")
        print(path)
        fname = os.path.splitext(os.path.basename(path))[0]
        print("FNAME:")
        print(fname)

        pdf = PdfFileReader(path)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            output_filename = "{}_page_{}.pdf".format(fname, page + 1)

            with open(output_filename, "wb") as out:
                pdf_writer.write(out)

            print("Created: {}".format(output_filename))


# if __name__ == '__main__':
# path = 'test.pdf'
# pdf_splitter(path)
