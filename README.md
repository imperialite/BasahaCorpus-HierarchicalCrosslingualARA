# BasahaCorpus: An Expanded Linguistic Resource for Readability Assessment in Central Philippine Languages

***CURRENTLY BEING UPDATED***

This repository hosts the code and data used for the EMNLP 2023 (Main) paper *"BasahaCorpus: An Expanded Linguistic Resource for Readability Assessment in Central Philippine Languages"* by Joseph Imperial and Ekaterina Kochmar.

### Dependencies
1. Numpy and Pandas for data processing.
2. Rank-Biased Overlap (https://github.com/changyaochen/rbo).
3. Implementation of cross-lingual n-gram overlap by [Imperial and Kochmar (2023, ACL)](https://aclanthology.org/2023.findings-acl.331/). Code is added to the repository.

### Data
The data from these languages are all distributed across the Philippine elementary system's first three grade levels (L1, L2, L3). We sourced this dataset from [Let's Read Asia (LRA)](https://www.letsreadasia.org/) with explicit permission obtained to share and conduct research with the corpus.

All used datasets are inside the `data` folder categorized by language. The formatted .txt and .csv files as the extracted features from the code are included in each language.

#### Linguistic Feature Extraction
Inside the `code` folder there are three parser files (`syll_parse.py`, `trad_parser.py`, `CLGSNGO_parser.py`) and three function files (`SYLL.py`, `TRAD.py`, `CLGSNGO.py`). The function files contain the functions for extracting the linguistic features and the parser files are where you input your .csv files to iterate row-by-row. Each parser file will output a .csv file containing the extracted features, which you can combine or concatenate together for experimentation (see examples such as `rin_features.csv` in the data/features/ folder).

### References
If you use any of the materials in this repository, including the dataset or the code, please add the following citations to your paper:
```
Imperial, J.M., & Kochmar, E. (2023). Automatic Readability Assessment for Closely Related Languages. Annual Meeting of the Association for Computational Linguistics (ACL).

Imperial, J. M., & Ong, E. (2020). Exploring hybrid linguistic feature sets to measure filipino text readability. In 2020 International Conference on Asian Language Processing (IALP) (pp. 175-180). IEEE.

Imperial, J. M., Reyes, L. L. A., Ibanez, M. A., Sapinit, R., & Hussien, M. (2022). A Baseline Readability Model for Cebuano. In Proceedings of the 17th Workshop on Innovative Use of NLP for Building Educational Applications (BEA 2022) (pp. 27-32).

```


### Contact
If you need any help reproducing the results, please don't hesitate to contact me below:

**Joseph Marvin Imperial** <br/>
jmri20@bath.ac.uk <br/>
www.josephimperial.com 
