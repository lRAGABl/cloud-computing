import nltk 

nltk.download('stopwords')
nltk.download('punkt')

def remove_stopwords(text_file_path):  
  with open(text_file_path, 'r') as file:
    text = file.read()
  words = nltk.word_tokenize(text)
  words = [word.lower() for word in words]
  stop_words = set(nltk.corpus.stopwords.words('english'))
  filtered_words = [word for word in words if word not in stop_words]
  return filtered_words


text_file_path = "C:/Users/Mega Store/Downloads/assignment"
filtered_words = remove_stopwords(text_file_path)

def count_word_frequency(list_of_strings):
  word_counts = {}
  for string in list_of_strings:
    words = string.lower().split()
    for word in words:
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
  return word_counts

list_of_strings = filtered_words
word_freqs = count_word_frequency(list_of_strings)

for word, count in word_freqs.items():
  print(f"{word}: {count}")
