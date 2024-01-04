import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
import re
import matplotlib.pyplot as plt

# Read the Excel file
file_path = 'C:/Users/nalin/OneDrive/Documente/Analysis/job_ads_updated.xlsx'
df = pd.read_excel(file_path)

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

# Display the first few rows of the dataframe
print(df.head())

# Assuming 'competencies' is the column name you want to analyze
competencies_column = df['competencies']

# Tokenization, removing special characters, stopwords, and lemmatization
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

cleaned_competencies = []
tokenized_words = []

for competency in competencies_column:
    # Remove non-alphanumeric characters using regular expression
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', str(competency))
    
    # Tokenization
    tokens = word_tokenize(cleaned_text.lower())
    
    # Remove stopwords and perform lemmatization
    filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    
    # Append the cleaned text and tokenized words
    cleaned_competencies.append(' '.join(filtered_tokens))
    tokenized_words.extend(filtered_tokens)

# Add a new column with cleaned competencies to the dataframe
df['cleaned_competencies'] = cleaned_competencies

# Display all rows of the 'cleaned_competencies' column
print("\nCleaned Competencies:")
print(df['cleaned_competencies'])

# Save the cleaned text to a new Excel file
output_file_path = 'C:/Users/nalin/OneDrive/Documente/Analysis/cleaned_competencies.xlsx'
df.to_excel(output_file_path, index=False)

# Calculate word frequency
fdist = FreqDist(tokenized_words)

# Display the most common words
print("\nMost common words:")
print(fdist.most_common(10))

# Plot the word frequency distribution
fdist.plot(30, cumulative=False)
plt.show()