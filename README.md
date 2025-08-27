# DrPrefix
# Medical Terminology Parser

A Python project that parses medical terminology reference PDFs to build structured dictionaries of **prefixes, roots, and suffixes**. Once the dictionaries are built, the tool lets you input a medical word and automatically decomposes it into its component parts.  

This project was designed as a study and teaching aid for medical terminology classes, making it easier to learn and understand the structure of medical words.

---

## Features
-  **PDF parsing**: Reads and extracts terminology tables (prefix, root, suffix) from a medical terminology guide.  
-  **Data cleaning**: Normalizes word parts, removes duplicates, and sorts by length for accurate matching.  
-  **Word decomposition**: Analyzes user-provided medical terms and splits them into prefix, root, and suffix.  
- **Dictionary output**: Returns results in a clean, structured Python dictionary.  

Example:
```python
{'Prefix': {'Prefix': 'hypo', 'Meaning': 'below or deficient', 'Connecting Vowel': None},
'Suffix': {'Suffix': 'ic', 'Meaning': 'pertaining to'},
'Root': {'Root': 'gastr', 'Meaning': 'stomach', 'Connecting Vowel': ['o', None, None]}}

