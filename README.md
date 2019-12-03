# HERCULES-EXTRACTION

[HERCULES-EXTRACTION](#hercules-extraction) is a command line interface (CLI) program that can be used to extract named entities from a text using differents methods of translation, extraction, coreference resolution and exportation. Some CLI samples are available [here](/sample).

The different components of this program can be used in a Jupyter Notebook by calling them directly without using the CLI. An example is available [here](/hercules-extraction.ipynb).

## Set Up

To set up the program you must download the requirements by running:
`pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html`

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

The configuration file enables to change the different components that will be used by [HERCULES-EXTRACTION](#hercules-extraction).

The configuration file must follow this patern:
```YAML
translation:
  implementation: translator-implementation
  language:
    text: text-language
    extraction: extraction-language
extraction:
  implementation: extractor-implementation
coreference:
  implementation: coreference-resolver-implementation
export:
  implementation: exporter-implementation
  language: exportation-language
  namespaces:
    entity: http://culture.gouv.qc.ca/entity/
    ontology: http://erlangen-crm.org/170309/
```
Where `translation` and `coreference` are optional.
All the implementation requirements and details can be found in the [Components](#components) section.


If no configuration file is specified, the default one used by the program is the following:
```YAML
translation:
  implementation: googletrans
  language:
    text: fr
    extraction: en
extraction:
  implementation: google
export:
  implementation: cidoccrm
  language: turtle
  namespaces:
    entity: http://culture.gouv.qc.ca/entity/
    ontology: http://erlangen-crm.org/170309/
```

## Components

There are four main component types in [HERCULES-EXTRACTION](#hercules-extraction):
- [Translator](#translator)
- [Entity Extractor](#entity-extractor)
- [Coreference Resolver](#coreference-resolver)
- [Exporter](#exporter)

### Translator

This component type allows to translate a text from the `text-language` to the `extraction-language` and to translate it back.

Any component of this type must inherit from [Translator](translation/base.py).

#### [AzureTranslator](translation/azure.py)

This translator uses the Azure Text API.
To use this component, should use this configuration:
```YAML
translation:
  implementation: azure
```

##### Requirements

This component requires to set the `AZURE_TOKEN` environment variable to an Azure Text API key. 

#### [GoogleCloudTranslator](translation/google_cloud.py)

This translator uses the Google Translation Cloud API.
To use this component, should use this configuration:
```YAML
translation:
  implementation: google
```

##### Requirements

This component requires to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to a Google service account JSON keyfile.

#### [GoogletransTranslator](translation/googletrans.py)

This translator uses the Google Translation website.
To use this component, should use this configuration:
```YAML
translation:
  implementation: googletrans
```

#### [MyMemoryTranslator](translation/my_memory.py)

This translator uses the MyMemory API.
To use this component, should use this configuration:
```YAML
translation:
  implementation: mymemory
```

##### Requirements

This component requires to set the `MYMEMORY_TOKEN` environment variable to a MyMemory API key.

### Entity Extractor

This component type allows to extract named entities from a text.

Any component of this type must inherit from [EntityExtractor](extraction/base.py).

#### [DandelionEntityExtractor](extraction/dandelion.py)

This entity extractor uses the Dandelion API.
To use this component, should use this configuration:
```YAML
extraction:
  implementation: dandelion
```

##### Requirements

This component requires to set the `DANDELION_TOKEN` environment variable to a Dandelion API key.

#### [GoogleEntityExtractor](extraction/google.py)

This entity extractor uses the Google Natural Language API.
To use this component, should use this configuration:
```YAML
extraction:
  implementation: google
```

##### Requirements

This component requires to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to a Google service account JSON keyfile.

##### Limitations

Currently this component cannot be used with a [Coreference Resolver](#coreference-resolver).

### Coreference Resolver

This component type allows to bundle coreferenced named entities together from a text.

Any component of this type must inherit from [CoreferenceResolver](coreference/base.py).

#### [StanfordCoreferenceResolver](coreference/stanford.py)

This coreference resolver uses a local intance of the Stanford CoreNLP server.
To use this component, should use this configuration:
```YAML
coreference:
  implementation: stanford
```

##### Requirements

Prerequisites:
- Java 1.8+

This component requires to:
1. Download [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) and models for the language you wish to use.
2. Put the model jars in the distribution folder.
3. Set the `CORENLP_HOME` environment variable to the path of the Stanford CoreNLP. Example: `CORENLP_HOME=/path/to/stanford-corenlp-full-2018-10-05`.

##### Use an aldready started Stanford CoreNLP server

If you want this coreference resolver to run multiple times, you should consider starting the server beforehand so it does not need to restart the server at every step. To do so, you can use the following commands:
1. `cd /path/to/stanford-corenlp-full-2018-10-05`
2. `java -mx16g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000`

To use an already started Stanford CoreNLP server you must specified the following config for the coreference resolver in the config file:
```YAML
coreference:
  implementation: stanford
  stanford:
    start_server: False
    endpoint: "server endpoint"
```
Where `"server endpoint"` could be `"http://localhost:9000"`

##### Limitations

The program cannot start a server at runtime. Please follow [Use an aldready started Stanford CoreNLP server](#use-an-aldready-started-stanford-corenlp-server).

### Exporter

This component type allows to export named entities in diffrent RDF format such as turtle, xml, n3, etc.

Any component of this type must inherit from [Exporter](export/base.py).

#### [CIDOCCRMExporter](export/cidoc_crm.py)

This exporter is specifically crafted to work with the [CIDOC CRM ontology](http://www.cidoc-crm.org/).
