# HERCULES-EXTRACTION

[HERCULES-EXTRACTION](#hercules-extraction) is a command line interface (CLI) program that can be used to extract named entities from a text using differents methods of translation, extraction, coreference resolution and exportation. Some CLI samples are available [here](/sample).

The different components of this program can be used in a Jupyter Notebook by calling them directly without using the CLI. An example is available [here](/hercules-extraction.ipynb).

## Set Up

To set up the program you must download the requirements by running:
`pip install -r requirements.txt`

Different components have different requirements see [Components](#components) for additional details.


## CLI Usage

The CLI program can be used as shown here:
```
hercules-extraction.py [-h] [--file FILE] [--config CONFIG] [--out OUT] [text]

positional arguments:
  text             text to process (optional if `--file` is specified)

optional arguments:
  -h, --help       show this help message and exit
  --file FILE      text file to process (optional if `text` is specified)
  --config CONFIG  config file
  --out OUT        out file (exporting to stdout if not specified)
```

Note: config file is described [here](#configuration-file)

## Configuration File

TODO ajouter explication du schema
TODO ajouter le default

## Components

There are four main component types in [HERCULES-EXTRACTION](#hercules-extraction):
- [Translator](#translator)
- [Entity Extractor](#entity-extractor)
- [Coreference Resolver](#coreference-resolver)
- [Exporter](#exporter)

### Translator

This component type allows to translate a text.

Any component of this type must inherite from [Translator](translation/base.py).

#### [AzureTranslator](translation/azure.py)

This translator uses the Azure Text API.

##### Requirements

This component requires to set the `AZURE_TOKEN` environment variable to an Azure Text API key. 

#### [GoogleCloudTranslator](translation/google_cloud.py)

This translator uses the Google Translation Cloud API.

##### Requirements

This component requires to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to a Google service account JSON keyfile.

#### [GoogletransTranslator](translation/googletrans.py)

This translator uses the Google Translation website.

#### [MyMemoryTranslator](translation/my_memory.py)

This translator uses the MyMemory API.

##### Requirements

This component requires to set the `MYMEMORY_TOKEN` environment variable to a MyMemory API key.

### Entity Extractor

This component type allows to extract named entities from a text.

Any component of this type must inherite from [EntityExtractor](extraction/base.py).

#### [DandelionEntityExtractor](extraction/dandelion.py)

This entity extractor uses the Dandelion API.

##### Requirements

This component requires to set the `DANDELION_TOKEN` environment variable to a Dandelion API key.

### Coreference Resolver

This component type allows to bundle coreferenced named entities together from a text.

Any component of this type must inherite from [CoreferenceResolver](coreference/base.py).

#### StanfordCoreferenceResolver

This coreference resolver uses a local intance of the Stanford CoreNLP server.

##### Requirements

TODO env var pour dire ou est le server 

*Note: to use a already started server Stanford CoreNLP you must specified the following config for the coreference resolver in the config file.* 
```
coreference:
  implementation: stanford
  stanford:
    start_server: False
    endpoint: "server endpoint"
```
Where "server endpoint" could be "http://localhost:9000"

### Exporter

This component type allows to export named entities in diffrent format such as turtle, xml, n3, etc.

Any component of this type must inherite from [Exporter](export/base.py).