# BT4222_Group24
## Topic-based Text Summarization of ESG Reports

### Setup
`pip install -r requirements.txt`

Note: Activate a virtual environment before running pip install

### How to use?
1. Run web scraper to extract S&P Global ESG Scores
- code: `../Scrapers/ESGScoreScraper.ipynb`
- output: `../Scrapers/scraped_data/{TICKER}_criteria_topic_score.csv`
- Note: top50companies.csv to include the companies and the corresponding tickers that you would want to scrape. Company name should be the official company name, i.e Apple Inc.

2. Extract textual data from ESG PDF reports
- code: `../pdfToText.ipynb`
- output: `../pdf_text/{TICKER}_{YEAR OF REPORT}.csv`
- Note: download and save the company's ESG report under `../ESG_reports/{TICKER}_{YEAR OF REPORT}`

3. Run Text Classifier to classify extracted text
- code: `../topic_classifier.ipynb`
- output: `../output/classified_sentences/{TICKER}_{YEAR OF REPORT}_results.csv`

4. Run Text Summarizer to summarize the text by criteria topics
- code: `../topic_summarizer.ipynb`
- output: `../output/summaries/{TICKER}_{TYPE OF INPUT}_summaries.csv`

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
    - Classifies text into 26 pre-defined ESG-labels and corresponding probabilities
    - We would map the ESG-labels to S&P Global's ESG Criteria Topic based on relevancy
  2. Text Summarization - BART model by Facebook (https://huggingface.co/facebook/bart-large-cnn)
    - Fine-tuned using CNN Daily Mail (Text-Summary dataset)
    - Performs Abstractive Summarization
  3. Web-Scrapping - Selenium and BeautifulSoup libraries

### Model Overview

![Screenshot 2023-04-14 at 22 30 34](https://user-images.githubusercontent.com/59095693/232073533-07674c2f-e65b-4cd5-a350-9dcf3c046206.png)

### ROUGE-N Metric
To evaluate the quality of the generated summaries, we will utilize the ROUGE-N (Recall-Oriented Understudy for Gisting Evaluation) metric, a widely used evaluation metric in text summarization tasks. In ROUGE-N, “N” represents the length of n-grams, which are contiguous sequences of N words in a text. ROUGE-L takes the longest common subsequence (LCS) between reference and generated summary. ROUGE-Lsum evaluates summaries on summary-level instead of sentence-level.

We used the Top 40 sentences by probability as a proxy for reference summaries due to the lack of human-generated summaries available. Next, we evaluated the quality of generated summaries using different input parameters (Top 20, Top 30, Random 20 and Random 30 sentences) and analyzed the average ROUGE-N scores as shown in Table 3. Our findings indicate that using Top 30 sentences yielded the best performance followed by Random 30 sentences based on “rougeLsum” value. 

NOTE: Using top 40 sentences as reference summaries may not be a perfect ground truth to use for evaluation as our summaries are generated using abstractive summarization which may have low lexical overlaps with the proxy reference summary. However, we observed that these summaries still capture crucial information for each criteria topic and the evaluation still provides valuable insights on understanding the parameters that we could consider using for future inputs.

### Evaluation Results using ROUGE-N Metric
- After obtaining the classified ESG-BERT labels for each sentence, we grouped them together based on the label with the highest probability and map them to the S&P Global's ESG Criteria Topics based on relevancy.
- Next, we have used 4 different types of input to generated summaries and evaluated their quality using ROUGE-N (Recall-Oriented Understudy for Gisting Evaluation) metric.

For each mapped criteria topic, we use:
 1. Top 20 Sentences by probability obtained from ESG-BERT
 2. Top 30 Sentences by probability obtained from ESG-BERT
 3. Random 20 Sentences 
 4. Random 30 Sentences

Here is the results:

Conclusion: We found that using Top 30 Sentences yielded the best quality summaries followed by Top 20 Sentences. Hence, we will be using the Top 30 sentences for generating summaries.

### Results
Some examples of the summary generated using Top 30 sentences based on probability

<b>Summary Generated for the Criteria Topic "Supply Chain Management" for Amazon Inc. ESG Report</b>

`In 2021, we began implementing recommendations from the HRIA, such as increasing our support for industry collaboration on responsible mineral sourcing, and building the capacity of our supply chain partners to effectively manage human rights risks. In 2020, we conducted Amazons first HRIA on the raw and recovered materials supply chain for Amazon-branded digital devices.We are dedicated to working with our suppliers to understand root causes and build strong management systems to address and mitigate issues. We are building our efforts to provide people connected to our value chain with access to effective grievance mechanisms. We update our supply chain map at least annually to provide customers and external stakeholders visibility into where we source. We want our Amazon Private Brands to support responsible supply chains and contribute to growing circular economies.
`
- AMZN Supply Chain Management Criteria Topic Score: 17
- Industry Best Supply Chain Management Criteria Topic Score: 93

<b>Summary Generated for the Criteria Topic "Climate Strategy" for Meta Platforms Inc. ESG Report</b>

`Data for Good partnered with the Yale Program on Climate Change Communication to conduct a global Climate Change Opinion Survey across 31 countries and territories on Facebook. This grant program will lay the foundation for important future work in fighting back against misinformation about climate change. More than six in 10 respondents across countries surveyed say they want more information about climate change. Meta helped lead the scoping and definition of the strategic initiative. We also debuted a new video series in Asia focused on climate change, called Forward Together. We embrace our responsibility as a global company to address the climate challenge that impacts us all. Achieving 50%-70% renewable energy could generate up to 600,000 jobs in wind, solar and battery storage. Net Positive Water Impact is a cornerstone concept for accelerating progress on UNSDG #6-Clean Water and Sanitation for all.`

- META Climate Strategy Criteria Topic Score: 55
- Industry Best Climate Strategy Criteria Topic Score: 84

### Insights
1. Despite using only the Top 30 sentences for each criteria topic as input for summarization, we found these summaries are still valuable for analysts as it provides insightful information on the company’s approach towards these criteria topics. Our generated summaries serve as a useful starting point for analysts to initiate a thorough analysis of the ESG reports. The generated summaries provide a better understanding of what to focus on and where to delve deeper. As such, we are able to help analysts better prioritize their time and effort in the analysis process, thus improving their overall efficiency.

2. Another key insight is that it is prudent to recognize that ESG analysis is a highly contextual and complex process. To provide a comprehensive analysis requires extensive background information and knowledge beyond the annual ESG reports. While the summaries provide insightful information on the ESG reports efficiently, we recommend that analysts should not rely solely on them during the ESG report analysis step of the overall process.

3. Through our project, we have learnt that the issue of “Greenwashing”, where companies engage in deceptive practices to appear environmentally responsible, cannot be neglected. This presents an additional layer of complexity and challenge to analysts in accessing a company’s ESG performance solely based on its ESG reports. Instead of taking the content of the ESG reports at face value, we recommend analysts conduct thorough and rigorous analyses to validate the authenticity of the strategies and policies disclosed and implemented by a company in addressing its key ESG risks.
