import PyPDF2

def pdfToText(pdfFilePath, outputFilePath):
    
    # Open the PDF file
    pdf_file = open(pdfFilePath, 'rb')

    # Create a PDF reader object
    reader = PyPDF2.PdfReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = len(reader.pages)

    # Initialize a string variable to hold the text
    text = ""

    # Iterate through all the pages and extract text
    for page_num in range(num_pages):
        page_obj = reader.pages[page_num]
        text += page_obj.extract_text()

    # Close the PDF file
    pdf_file.close()

    # Open the file in write mode
    with open(outputFilePath, 'w') as f:
        # Write the text to the file
        f.write(text)

    # Print a message to confirm that the file has been saved
    print("Text saved to file.")

