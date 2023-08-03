import fitz
import os
import glob

for pdfFiles in glob.glob('*.pdf'):
    document = fitz.open(pdfFiles)
    documentPageNumber = document.page_count
    keywordsToSearch = open('keywords.txt', 'r')
    keywordList = keywordsToSearch.read()
    keywordsSeperated = keywordList.split(',')
    keys = {}
    for keywords in keywordsSeperated:
        c=0
        for page in range(0, documentPageNumber):
            content = document[page]
            keywordPattern = keywords.strip()
            keywordSearch = content.search_for(keywordPattern)
            for key in keywordSearch:
                c+=1
            if c>1:
                keys[keywords]=c
    if len(keys)>0:
        print(pdfFiles, '->', keys)
        output = open('keyword_dataset.csv', 'a')
        output.write(pdfFiles + '\t' + str(keys) + '\n')
    else:
        print(pdfFiles, '->', keys)
        output = open('keyword_dataset.csv', 'a')
        output.write(pdfFiles + '\t' + 'Image Format OR No Keywords Found' + '\n')
    