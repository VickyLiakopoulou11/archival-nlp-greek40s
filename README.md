# Integrating Archival Materials for the Study of the Turbulent Greek 40s

This repository supports the Zenodo publication:  
📄 **[Integrating Archival Materials for the Study of the Turbulent Greek 40s](https://doi.org/10.5281/zenodo.4271532)**

## 📌 About This Research  
This study applies **Natural Language Processing (NLP) techniques** for **Information Extraction** from the free text of archival entries in the **Army History Directorate (AHD) archive**.  

The archive contains a **digital catalogue** where entries include standard metadata fields describing the exhibits. The **focus** of this research is the **"title" field**, a short description containing:
- **Named entities** (persons, places, Greek army units/formations, gendarmerie, police)  
- **Abbreviations**  

The **goal** is to automatically extract structured metadata using **NLP techniques**, leveraging tools developed at the **Institute for Language and Speech Processing (ILSP)**. The extracted categories include:  
📌 **Document Type** | **Sender** | **Addressee** | **Date** | **Subject** | **Army Unit** | **Geonames**  

### 🔹 **Methodology**
The research workflow follows **two main processing stages**:  
1️⃣ **Preprocessing**:  
   - **Part-of-Speech Tagging & Lemmatization** using ILSP tools  
   - Tokenization & segmentation into functionally distinct word groups  

2️⃣ **Information Extraction**:  
   - **Regular Expressions + Apache UIMA RUTA** for rule-based entity recognition  
   - **Pattern matching** to identify structured metadata  
   - **Evaluation on a corpus of 1,500 titles**, yielding **highly encouraging results**  

### 🔗 **Publication & Citation**
- 📄 **Zenodo DOI:** [https://doi.org/10.5281/zenodo.4271532](https://doi.org/10.5281/zenodo.4271532)  
- 🏛 **Affiliation:** Institute for Language and Speech Processing (ILSP)  
- 📚 **Keywords:** Information Extraction, NLP, Regular Expressions, Apache UIMA Ruta, Army History Directorate (AHD)  

---

