# HERCULES-EXTRACTION

## Translation
### Description
This Python script allows to translate a text file using the Google Translation Cloud API. 

### Requirements
Prior to run the translation module, please ensure that these packages are installed:
- googletrans : `pip install googletrans`

### Usage
src_text: Path to the text file that needs translation

src_lang: Language of the source text file

dest_text: Path to the translated text file

dest_lang: Desired language for the translated file

### Exemples
`python3 ./translation.py ./input_en.txt en ./output_fr.txt fr`


## Entity Extraction
### Google Cloud Natural Language API
The `GOOGLE_APPLICATION_CREDENTIALS` environment variable should point to a service account JSON keyfile.

### Requirements
Prior to run the entity extraction module, please ensure that these packages are installed:
- google-cloud-language : `pip install google-cloud-language`
