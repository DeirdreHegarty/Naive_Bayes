## Naive Bayes Classifier - Sentiment (NLTK)


need to install:
`sudo pip install nltk`

run: `python senti.py `

### Using python shell:


```python
import nltk
from nltk import word_tokenize
```

```python
nltk.downloader()
```
 and download **all** (really just need punkt)

```python
sent = "Hello world. Please tokenize."
word_tokenize(sent)
```

```python
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader
```

### Issue with Data Provided:

Some files were created using a text rich editors. This meant that they were encoded in non utf8 formats.
Code below:
* python to print all unicode chars that cause issues
* `sed` to replace all chars with nothing
* put to .fix files and then last for loop puts back to .txt

One of problem files found -> blurbs/59c653d9fe.txt

![screenshot of special characters - issue](img/data-issue.png)

```bash
CHARS=$(python -c 'print u"\u0091\u0092\u00a0\u200E".encode("utf8")')
for i in *; do sed 's/['"$CHARS"']//g' < $i > ${i}.fix; done
for i in $(find . -type f -name '*.fix'); do mv ${i} ${i%.fix}; done
```

**code I like for getting parent directory of a file (used substring in end):**
```python
import os 
print os.path.basename(os.path.dirname("path/to/blurbs/pos/f574b42c31.txt"))
```
*I first converted all files to .txt to try fixing issue (before I knew it was special chars specifically causing the issue)*

```bash
echo 'set encoding=utf-8' >> ~/.vimrc
echo 'set fileencoding=utf-8' >> ~/.vimrc
for file in $(find path/to/blurbs/ -type f); do vim "$file"wq; done
```

### Note
There are two directories containing data: 'blurbs' and 'sorted-blurbs'. I had originally 
randomly assigned files to `pos` and `neg`. I later sorted the data in 'sorted-blurbs'...

Ultimately the most suitable data -> movie_review data I used for training (in NLTK corpora).
This is commented out in senti.py and is labelled `# BETTER TESTING DATA`.

![screenshot of using movie_review data](img/movie_reviews.png)
![screenshot of using unsorted blurbs](img/blurbs.png)

There are unused functions in `indiv.py`. These were ideas that I was thinking of persuing before deciding on text classification using NLTK and Naive Bayes.

eg. tagSent
![screenshot of using unsorted blurbs](img/tagSent.png)