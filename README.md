# Ad Hoc Compounds for Stance Detection

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg


## 1. About 

This repository contains all data and code for the following paper:

> Qi Yu, Fabian Schlotterbeck, Hening Wang, Naomi Reichmann, Britta Stolterfoht, Regine Eckardt and Miriam Butt. 2024. Ad Hoc Compounds for Stance Detection. *Proceedings of the Joint Workshop on Multiword Expressions and Universal Dependencies (MWE-UD) @ LREC-COLING 2024*.

**A short summary of the paper:**

We examine German ad hoc compounds that express attitudinal meanings of the speakers. 
While such compounds are crucial for stance detection, the state-of-the-art dependency parsers and
Universal Dependency treebanks struggle with parsing them. 
Through a corpus analysis and a psycholinguistic experiment, we verify that such compounds systematically convey attitudinal meaning. 
Furthermore, we report initial experiments with large language models that underline 
the difficulties in capturing attitudinal meanings conveyed by ad hoc compounds.

## 2. Content of the Repository

| Folder                   | Description                                                                                                                                                                                                                                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```1_corpus_study```               |   Data and code for the corpus study (see Section 3.1 of the paper)                                                                    |
| ```2_psycholinguistic_experiment```   | Data and code for the psycholinguistic experiment (see Section 3.3 of the paper)                                                                                                                                                                                                              |
| ```3_LLM_simulation```             | Code for the simulation experiment with large language models (see Section 4 of the paper)     |

## 3. Cite the paper

```
@inproceedings{yu-etal-2024-ad,
    title = "Ad Hoc Compounds for Stance Detection",
    author = "Yu, Qi  and
      Schlotterbeck, Fabian  and
      Wang, Hening  and
      Reichmann, Naomi  and
      Stolterfoht, Britta  and
      Eckardt, Regine  and
      Butt, Miriam",
    editor = {Bhatia, Archna  and
      Bouma, Gosse  and
      Do{\u{g}}ru{\"o}z, A. Seza  and
      Evang, Kilian  and
      Garcia, Marcos  and
      Giouli, Voula  and
      Han, Lifeng  and
      Nivre, Joakim  and
      Rademaker, Alexandre},
    booktitle = "Proceedings of the Joint Workshop on Multiword Expressions and Universal Dependencies (MWE-UD) @ LREC-COLING 2024",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.mwe-1.27",
    pages = "231--242"
}
```

## 4. Acknowledgement
This project is funded by the Deutsche Forschungsgemeinschaft (DFG – German Research Foundation) under Germany‘s Excellence Strategy – EXC-2035/1 – 390681379.

