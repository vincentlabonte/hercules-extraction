# HERCULES-EXTRACTION - Sample

This folder contains some CLI samples. Each sample uses different components to show different use cases.

## [Default](/default)

This sample uses the default configuration file.

### Components

- **Translator**: GoogletransTranslator
- **Entity Extractor**: GoogleEntityExtractor
- **Coreference Resolver**: None
- **Exporter**: CIDOCCRMExporter

### Execution Command

`python ../hercules-extraction.py --file ./default/text.txt --out ./default_sample.ttl`

### Configuration File

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
    entity: http://www.hercules.gouv.qc.ca/instances/entities/
    ontology: http://www.cidoc-crm.org/cidoc-crm/
```
  
## [Entity extraction and export](/extraction_export)

### Components

- **Translator**: GoogleCloudTranslator
- **Entity Extractor**: None
- **Coreference Resolver**: None
- **Exporter**: CIDOCCRMExporter

### Execution Command

`python ../hercules-extraction.py --file ./extraction_export/text.txt --config ./extraction_export/config.yml --out ./extraction_export_sample.ttl`

### Configuration File


```YAML
extraction:
  implementation: google
export:
  implementation: cidoccrm
  language: turtle
  namespaces:
    entity: http://www.hercules.gouv.qc.ca/instances/entities/
    ontology: http://www.cidoc-crm.org/cidoc-crm/
```
  
## [Translation, entity extraction, coreference resolution and export](/translation_extraction_coreference_export)

### Components

- **Translator**: AzureTranslator
- **Entity Extractor**: DandelionEntityExtractor
- **Coreference Resolver**: StanfordCoreferenceResolver
- **Exporter**: CIDOCCRMExporter

### Execution Command

`python ../hercules-extraction.py --file ./translation_extraction_coreference_export/text.txt --config ./translation_extraction_coreference_export/config.yml --out ./translation_extraction_coreference_export_sample.ttl`

### Configuration File


```YAML
translation:
  implementation: azure
  language:
    text: fr
    extraction: en
extraction:
  implementation: dandelion
coreference:
  implementation: stanford
  stanford:
    start_server: False
    endpoint: "http://localhost:9000"
export:
  implementation: cidoccrm
  language: turtle
  namespaces:
    entity: http://www.hercules.gouv.qc.ca/instances/entities/
    ontology: http://www.cidoc-crm.org/cidoc-crm/
```
  
## [Translation, entity extraction and export](/translation_extraction_export)

### Components

- **Translator**: GoogletransTranslator
- **Entity Extractor**: GoogleEntityExtractor
- **Coreference Resolver**: None
- **Exporter**: CIDOCCRMExporter

### Execution Command

`python ../hercules-extraction.py --file ./translation_extraction_export/text.txt --config ./translation_extraction_export/config.yml --out ./translation_extraction_export_sample.ttl`

### Configuration File


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
    entity: http://www.hercules.gouv.qc.ca/instances/entities/
    ontology: http://www.cidoc-crm.org/cidoc-crm/
```
