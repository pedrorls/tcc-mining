from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams


def pdf_to_text(pdf_path):
    resource_manager = PDFResourceManager()
    string_io = StringIO()
    codec = "utf-8"
    laparams = LAParams()
    device = TextConverter(resource_manager, string_io, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    with open(pdf_path, "rb") as filename:
        for page in PDFPage.get_pages(filename):
            interpreter.process_page(page)

    text = string_io.getvalue()
    device.close()
    string_io.close()

    return text

