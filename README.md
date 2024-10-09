# Keyword Analysis for Newspaper Articles

This Python script analyzes newspaper articles from a specified Excel file to assess the relevance of articles based on certain keywords. It marks articles containing specific terms as irrelevant and assigns a confidence score.

## Key Features

- **Data Import**: Loads newspaper article data from an Excel spreadsheet for processing.

- **Relevance Check Function**: Implements a function to evaluate each article's text. The function checks the first and second words of the article text for specific keywords:
  - If the first word is "publicidade", "necrologia", or "desporto", the article is marked as irrelevant (`Relevance = 0`) with a confidence score of `10`.
  - If the second word is "publicidade", "necrologia", or "classificados", the same relevance and confidence rules apply.

- **Data Processing**: Applies the relevance check function across all rows in the dataset, updating the `Relevance` and `Confidence` columns accordingly.

- **Results Output**: Prints the updated relevance values for each article, the count of relevance categories, and the available columns in the dataset. The updated dataset is then saved back to the original Excel file.

## Usage

1. Ensure you have the required libraries installed:
   ```bash
   pip install pandas openpyxl
