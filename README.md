# wb-wikosophy
Python recursive function to test Wikipidia "Getting to Philosophy" phenomenon.

As stated in Wikipidia "Getting to Philsophy" article, clicking on the first link in the main text of a Wikipedia article, 
and then repeating the process for subsequent articles, would usually lead to the Philosophy article.
This repository is all about testing this phenonemon.

# Basic pseudocode:
1. Find all paragraphs of the article.
2. Elemenate unwanted tags ids and classes.
3. Remove any statement between parantheses
4. Get the first link.
5. Request the link page and back to 1 again untill finding the Philosophy article, being stuck in a loop or reaching a deadend page

# Challenges:
- Removing parantheses removed some links like:
  https://en.wikipedia.org/wiki/Object_(philosophy)
  So, it was necessary to change regex pattern in order to ignore any '(' preceded by '_'.
- Some links caused TypeErros because they were fake but included in the structure of the page,
  I handled them with an exception to continue searching for other links if any error is raised.

## run the script: 
```
git clone https://github.com/OmarGhoneim/wb-wikosophy
cd wb-wikosophy
virtualenv -p python3
pip install -r requirements.txt
python wikosopher.py
```
