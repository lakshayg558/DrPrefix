import camelot
from Config import pdftables_csv as ps
import os

def pdf2dataframe():
    if not os.path.exists(ps):
        os.makedirs(ps, exist_ok=True)
    tables = camelot.read_pdf(r'/Users/lakshaygupta/Downloads/Guide to Common Medical Terminology.pdf', pages="all", flavor="lattice")
    tables.export(os.path.join(ps,"Extracted_table.csv"), f="csv", compress= False)
