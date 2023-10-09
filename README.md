# web-scraper

This is a simple python script that scrapes Wikipedia's top grossing animated films and puts it into either a csv or a pandas array for further processing.

Broadly speaking, we get the url, turn the page into an html soup, then search and clean the data by sorting out the appropriate html tags. At the end we can choose to either continue working with this data in Python via the pandas library, or we can export this to a csv to use it in some other data visualization tool (Tableau, Power-BI, etc.)
