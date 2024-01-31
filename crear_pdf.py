from xhtml2pdf import pisa
from jinja2 import Template
from datetime import datetime

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        
    return not pisa_status.err

hoy = datetime.today()
timestamp = datetime.timestamp(hoy)
#sourceHtml = open('mipdf.html').read()

# Generate PDF
pdf_path = "example_"+str(timestamp)+".pdf"
data = {'nombre':'Gustavo Javier Marchena Bárcenas','fecha':hoy}
template = Template(open('mipdf.html').read())
html = template.render(data)
if convert_html_to_pdf(html, pdf_path):
    print(f"PDF generated and saved at {pdf_path}")
else:
    print("PDF generation failed")