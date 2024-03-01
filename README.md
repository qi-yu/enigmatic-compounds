# Ad Hoc Compounds in Political Discourse

## 1. About 

This repository contains all source code and data for the following study:

Qi Yu, Fabian Schlotterbeck, Regine Eckardt, and Britta Stolterfoht. 2022. An experimental study on ad hoc compounds in political discourse. 9th Experimental Pragmatics Conference (XPRAG 2022). September 22-23, IUSS Pavia, Italy. [Abstract](https://osf.io/fq69z)



## 2. Content of the Repository

### 2.1 Data
The folder ```data``` contains data collected from the experiment.
    - ```data/data.csv```: data without information on political leaning of the experiment participants
    - ```data/data_with_political_leaning.rds```: data with information on political leaning of the experiment participants (collected in Anselm's experiment)
 
**Note:**

The item amount of the two datasets differs slightly, as the political leaning of some participants were missing due to an internal system error in Anselm's experiment

### 2.2 Code

- ```clmm.Rmd```: analysis published in the XPRAG 2022 abstract
- ```clmm_with_political_leanings.Rmd```: additional analyses after the publication of the XPRAG 2022 abstract. Specifically, the political leaning of the experiment participants is added as a new predictor. 
