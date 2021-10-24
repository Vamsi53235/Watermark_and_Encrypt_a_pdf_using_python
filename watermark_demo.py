
from PyPDF4 import PdfFileWriter, PdfFileReader

def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark,strict=False)#create an watermark object
    watermark_page = watermark_obj.getPage(0)#get the watermark 

    pdf_reader = PdfFileReader(input_pdf,strict=False)#read the file to be watermarked i.e create an object to get watermarked
    pdf_writer = PdfFileWriter()#create an object to write an output file
    
    #iterate through the original pdf to watermark all pages
    for page in range(pdf_reader.getNumPages()):
        #Return type: dict. getNumPages () Calculates the number of pages in this PDF file.
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)  #will overlay the watermark_page on the top of the current page
        pdf_writer.addPage(page)    #add that newly merged page to the pdf_writer object
    
    #Encrypt the pdf using password
    pdf_writer.encrypt(user_pwd="Python",owner_pwd='python',use_128bit=True)
    
    #write to the respective output_pdf provided
    with open(output, 'wb') as out:
        pdf_writer.write(out)

create_watermark('without_watermark.pdf', 'output_watermark.pdf','VAMSI_Watermark.pdf')


'''
Link for reference : https://pythonguides.com/pdffilereader-python-example/
    1.PdfFileReader function is used to read the object that holds the path of a pdf file. Also, it offers few more arguments that can be passed.
    2.getPage (pageNumber) Retrieves a page by number from this PDF file.
    3.PdfFileReader used to perform all the operations related to reading a file.
    4.PdfFileReader in Python offers functions that help in reading & viewing the pdf file.
    5.It offers various functions using which you can filter the pdf on the basis of the page number, content, page mode, etc.
    6.PdfFileWriter is used to perform write operations on pdf.
    
'''