#import pandas as pd
#from nltk.tokenize import word_tokenize
#from nltk.stem import WordNetLemmatizer

# Sample data - replace this with the path to your Excel file
#excel_file_path = 'C:/Users/nalin/OneDrive/Documente/Analysis/cleaned_competencies.xlsx'

# Sample agentic and communal words
#agentic_words = ['lead', 'achieve', 'innovate']
#communal_words = ['collaborate', 'communicate', 'support']

# Read the Excel file into a DataFrame
#df = pd.read_excel(excel_file_path)

# Initialize WordNet lemmatizer
#lemmatizer = WordNetLemmatizer()

# Function to categorize words as agentic or communal
#def categorize_word(word):
    # Lemmatize the word to its root form
    #root_word = lemmatizer.lemmatize(word.lower())

    # Check if the root word is in agentic_words or communal_words
    #if root_word in agentic_words:
        #return 'agentic'
    #elif root_word in communal_words:
        #return 'communal'
    #else:
        #return 'neutral'
    
 # Function to tokenize and categorize text, handling non-string values
#def categorize_text(text):
    #if pd.isna(text):
        #return []
# Convert non-string values to string (e.g., for float values)
    #text_str = str(text)
    
    #words = word_tokenize(text_str.lower())
    #categories = [categorize_word(word) for word in words]
    #return categories


# Tokenize and categorize the 'cleaned_comp' column
#df['word_categories'] = df['cleaned_comp'].apply(categorize_text)

# Calculate the proportion of agentic and communal words in each row
#df['agentic_proportion'] = df['word_categories'].apply(lambda x: x.count('agentic') / len(x) if len(x) > 0 else 0)
#df['communal_proportion'] = df['word_categories'].apply(lambda x: x.count('communal') / len(x) if len(x) > 0 else 0)

# Display the resulting DataFrame
#print(df[['cleaned_comp', 'agentic_proportion', 'communal_proportion']])

#ALL THE BEFORE IS GOOD, BUT NEXT I TRY WITH EXCEL INSTEAD OF LIST IN THE SCRIPT

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Sample data 
excel_file_path = 'C:/Users/nalin/OneDrive/Documente/Analysis/final_excell.xlsx'

# Paths to agentic and communal word files
agentic_words_file = 'C:/Users/nalin/OneDrive/Documente/Analysis/agentic_words.XLSX'
communal_words_file = 'C:/Users/nalin/OneDrive/Documente/Analysis/communal_words.XLSX'

# Read the Excel files with agentic and communal words
agentic_words_df = pd.read_excel(agentic_words_file)
communal_words_df = pd.read_excel(communal_words_file)

# Extract words from the DataFrames
agentic_words = agentic_words_df['agentic_word'].tolist()
communal_words = communal_words_df['communal_word'].tolist()

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to categorize words as agentic or communal
def categorize_word(word):
    # Lemmatize the word to its root form
    root_word = lemmatizer.lemmatize(word.lower())

    # Check if the root word is in agentic_words or communal_words
    if root_word in agentic_words:
        return 'agentic'
    elif root_word in communal_words:
        return 'communal'
    else:
        return 'other'

# Function to tokenize and categorize text, handling non-string values
def categorize_text(text):
    if pd.isna(text):
        return []
    
    # Convert non-string values to string (e.g., for float values)
    text_str = str(text)
    
    words = word_tokenize(text_str.lower())
    categories = [categorize_word(word) for word in words]
    return categories

# Tokenize and categorize the 'competencies' column
df['word_categories'] = df['cleaned_competencies'].apply(categorize_text)

# Calculate the proportion of agentic and communal words in each row
df['agentic_proportion'] = df['word_categories'].apply(lambda x: x.count('agentic') / len(x) if len(x) > 0 else 0)
df['communal_proportion'] = df['word_categories'].apply(lambda x: x.count('communal') / len(x) if len(x) > 0 else 0)

# Display the resulting DataFrame
pd.set_option('display.max_rows', None)
print(df[['agentic_proportion', 'communal_proportion']])

# Create a new DataFrame for the two rows
summary_df = pd.DataFrame({'agentic_proportion': [df['agentic_proportion'].mean()],
                            'communal_proportion': [df['communal_proportion'].mean()]})

# Append the summary DataFrame to the original DataFrame
df = pd.concat([df, summary_df], ignore_index=True)

# Save the DataFrame to a new Excel file
output_excel_path = 'C:/Users/nalin/OneDrive/Documente/Analysis/output_file.xlsx'
df.to_excel(output_excel_path, index=False)
print(f"Excel file saved to: {output_excel_path}")