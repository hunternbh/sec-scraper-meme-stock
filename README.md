sraf-v1-scraper is the original scraper from https://sraf.nd.edu/

python parser is a modified version of the scraper
- changes made is to use a different requests library

sraf-v1-sentiment is the sentiment analysis. The code works
- it uses the loughran macdonald dictionary

Inside the sentiment folder, there is a r file to do the analysis,
we then get the results file where I save the csv.

WHAT TO DO
- go to 1 python parser
- run simple-parser first - you need to feed it ms-list-3.csv,
which is a list of the ciks that we need. it will then generate
the links-2020-q1.txt, which is the name of the file and the link.

- we then use 2-url-retriever, to get the folder of documents.
- the files need to change extension to .txt, run the extension changer
- to run the extension changer, prepare 6 files titled 2020-q1, 2020-q2 and so on, move the files inside
- everytime after collecting, move the files into the folder, then once all 6 folders are filled, then run the change-file-extension.py

- Then, we use 3-data-cleaner. There are 3 parts in this .py file
- Firstly, we need to clean the html markup. This is done using a python library - Beautiful Soup
- You need to use pip install BeautifulSoup
- After Part 1 cleans the html markup, it deposits the output into 2-cleaned-html

- Part 2 cleans up the excess rubbish tesxt at the end of the document. The directly
- downloaded .txt files have a lot of rubbish text at the bottom. By identifying the unique
- stopword signature, we delete all the remaining text from below. It deposits the data into 2-cleaned-signature

- Lastly, Part 3 will filter out 10Q and 10K Risk Factors and MD&A. We leave the 8Ks untouched as they only contain
- relevant information at this point. To identify the stop parts, we notice that all 10Ks and 10Qs follow
- the same format. They have a main contents page and then each relevant part.
- We filter from the unique keyword "Item 1A. Risk Factors" and cut off at "Item 1B. Unresolved Staff Comments"
- After the HTML markup is deleted, each filing still has unique ways of presenting this, for example
- Item 1a - risk factors or Item1a.   risk factors. By using a regex combination, we capture for most of these
- variations. Note that this only works for 10K and 10Q. 10K-A will encounter errors.
- Text Mining is an art. We need to observe and then filter out on our own. No program is smart enough
- to do this yet, unless we train an AI model.


FAQ

1. REQUESTS LIBRARY NOT THERE
- change the python interpreter path - check where pip is installing to
- then go to ctrl shift p in vs code and change