

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Create a list of the most common topics in linear algebra
topics = ['vector', 'vector', 'linear', 'equation', 'matrix', 'matrix',
          'vector', 'determinant', 'determinant', 'determinant', 'inverse', 'eigenvector',
          'vector', 'eigenvalue', 'eigenvalue', 'eigenvector', 'eigenvector']

# Generate a word cloud
wordcloud = WordCloud(width=1000, height=500, background_color='white').generate(' '.join(topics))

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud.png')
plt.show()



