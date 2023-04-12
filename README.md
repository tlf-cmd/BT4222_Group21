# BT4222_Group24
## Topical Text Summarization of ESG Reports

### Setup
`pip install -r requirements.txt`
Note: Activate a virtual environment before running pip install

### How to use?
1. Run web scraper to extract S&P Global ESG Scores
- code: `../Scrapers/ESGScoreScraper.ipynb`
- output: `../Scrapers/scraped_data/{TICKER}_criteria_topic_score.csv`
Note: top50companies.csv to include the companies and the corresponding tickers that you would want to scrape. Company name should be the official company name, i.e Apple Inc.

2. Extract textual data from ESG PDF reports
- code: `../pdfToText.ipynb`
- output: `../pdf_text/{TICKER}_{YEAR OF REPORT}.csv`
Note: download and save the company's ESG report under `../ESG_reports/{TICKER}_{YEAR OF REPORT}`

3. Run Text Classifier to classify extracted text
- code: `../topic_classifier.ipynb`
- output: `../output/classified_sentences/{TICKER}_{YEAR OF REPORT}_results.csv`

4. Run Text Summarizer to summarize the text by criteria topics
- code: `../topic_summarizer.ipynb`
- output: `../output/summaries/{TICKER}_{YEAR OF REPORT}_summaries.csv`

---

### Introduction
With the rise of a new generation of socially-responsible investors, there is an increasing demand for companies to operate sustainably and responsibly. Consequently, for companies to be transparent and maintain trust with their shareholders, companies are increasingly disclosing information through annual ESG reports. Coupled with the introduction of new risk factors faced by investors and companies, this gives rise to “ESG Investing” or “Sustainable Investing” among financial institutions such as asset management companies, hedge funds and investment banks. 

For financial institutions, the process of analyzing a company’s ESG performance generally involves:
  1. Analyzing the company’s financial statements and understanding the business model.
  2. Identifying key material ESG risks faced by the company and the industry in general.
  3. Analyzing the company’s ESG report to understand their ESG efforts as well as how they address these ESG risks by identifying any strategies or policies implemented.
  4. Determining if these strategies or policies are adequate and robust in dealing with the key ESG risks identified earlier. Compare ESG scores between companies in the same industry to have a better idea of the effectiveness of these implemented strategies. Note that, these ESG scores are not deterministic in concluding the analysis of the company’s ESG performance.

We found that the process of analyzing an ESG report is a rather tedious and time-consuming process. This is because ESG reports are often long and unstandardised in their reporting format which makes extracting information rather difficult. As such, identifying strategies and policies implemented by companies to address the key ESG risks and extracting other relevant information on the company's ESG efforts is a very manual process that is both time and resource-intensive.

### Project Objective and Implementation
As such, the objective of our project is to help analysts in financial institutions improve on the efficiency of the process by providing generated summaries on the ESG report by relevant ESG topics. 

In this project, we will be utilizing Natural Language Processing (NLP) techniques such as Text Classification and Text Summarization to achieve our objective. In addition, we will using web-scrapping techniques to extract useful information on the company's ESG efforts which would complement the generated summaries.

### Models and Tools used
  1. Text Classification - ESG-BERT model by nbroad (https://github.com/mukut03/ESG-BERT)
  2. Text Summarization - BART model by Facebook (https://huggingface.co/facebook/bart-large-cnn)
  3. Web-Scrapping - Selenium and BeautifulSoup libraries
