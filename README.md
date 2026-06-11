### PDF-To-Text Converter

## Overview

PDF-To-Text Converter is a Python and Streamlit-based web application that extracts text from PDF documents and displays the results through an interactive user interface.

The project began as a simple PDF text extraction tool and has gradually evolved to support page selection, improved formatting, and OCR-based extraction for image-only PDF pages.


## Technologies Used - 

* Python
* Streamlit
* PyPDF
* PDF2Image
* Pillow
* Pytesseract
* Tesseract OCR


## Features

# V1 - Basic PDF Text Extraction - 

* Upload PDF documents through a web interface.
* Extract text using PyPDF.
* Display extracted text page by page.
* Support for multi-page PDFs.


# V2 - User Interface Improvements - 

* Dynamic page count detection.
* Slider-based page selection.
* Range selection for extracting specific pages.
* Expandable sections for each page.
* Improved text formatting.
* Paragraph preservation using newline-based preprocessing.
* Cleaner and more organized output display.

# V3 - OCR Integration - 

* OCR fallback for image-based PDF pages.
* Automatic detection of pages where native text extraction fails.
* Conversion of PDF pages into images using PDF2Image.
* Text extraction from images using Tesseract OCR.
* Unified output pipeline for both native extraction and OCR extraction.
* Support for scanned and image-only PDF documents.


## Current Workflow - 

1. Upload a PDF document.
2. Select the page range to process.
3. For each selected page:

   * Attempt text extraction using PyPDF.
   * If text extraction succeeds, process and display the extracted text.
   * If text extraction fails, convert the page to an image and perform OCR.
4. Display extracted content in expandable page sections.


## Project Goal - 

The long-term goal of this project is to evolve from a PDF text extraction tool into a complete AI-powered document assistant capable of:

* Text Extraction
* OCR
* Summarization
* Document Question Answering
* RAG-Based Retrieval
* Agentic Workflows
* Local LLM Integration
