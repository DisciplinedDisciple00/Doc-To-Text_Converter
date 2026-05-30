from pypdf import PdfReader


#Finding length of doc for slider limit
def len_finder(file):
    reader = PdfReader(file)
    file_pages = reader.pages

    max_pages = len(file_pages)
    return max_pages

#Main text extraction
def converter(file, target):
    reader = PdfReader(file)
    file_pages = reader.pages

    cleaned_pages_text = []

    for i in range(target):
        page_text = file_pages[i].extract_text()
        cleaned_page_text = page_text.split("\n")
        cleaned_pages_text.append(cleaned_page_text)

    return cleaned_pages_text