import argparse
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from pathlib import Path
import sys
import yaml
from extraction.base import Entity

import translation
import extraction
import coreference
import export

DEFAULT_CONFIG_FILE = Path('utils', 'default_config.yml')
SCHEMA_CONFIG_FILE = Path('utils', 'schema.yml')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, nargs='?',
                        help='text to process (optional if `--file` is specified)', default=None)
    parser.add_argument('--file', dest='file', type=str,
                        help='text file to process (optional if `text` is specified)', default=None)
    parser.add_argument('--config', dest='config', type=str,
                        help='config file', default=DEFAULT_CONFIG_FILE)
    parser.add_argument('--out', dest='out', type=str,
                        help='out file (exporting to stdout if not specified)', default=None)
    args = parser.parse_args()

    text = None
    if args.text is not None and args.file is not None:
        print('Should not specify a text and a text file at the same time. Exiting...', file=sys.stderr)
        exit(1)
    elif args.text is not None:
        text = args.text
    elif args.file is not None:
        in_path = Path(args.file)
        if not in_path.is_file():
            print(
                f'Unable to locate file {in_path}. Exiting...', file=sys.stderr)
            exit(1)

        text = in_path.read_text()
    else:
        print('Should specify at least a text or a text file. Exiting...',
              file=sys.stderr)
        exit(1)

    config_file = Path(args.config)
    config = read_yaml_file(config_file)

    schema = read_yaml_file(SCHEMA_CONFIG_FILE)

    try:
        validate(config, schema)
    except ValidationError as e:
        print(
            f'Config file does not follow schema: {e.message}. Exiting...', file=sys.stderr)
        exit(1)

    translation_config = config.get('translation')
    if translation_config is not None:
        text = translate_text(text, translation_config)

    extraction_config = config.get('extraction')
    entities = extract_entities(text, extraction_config)

    coreference_config = config.get('coreference')
    if coreference_config is not None:
        entities = resolve_coreference(text, entities, coreference_config)

    translator_name = translation_config.get('implementation')
    language_config = translation_config.get('language')
    language_extraction = language_config.get('extraction')
    language_text = language_config.get('text')
    translator_type = registered_translator.get(translator_name)
    translator = translator_type()
    
    translated_entities = []
    for entity in entities:
        print("Name: " + entity.name + " From: " + language_extraction + " To: " + language_text)
        entity_name = translator.translate(entity.name, language_extraction, language_text)
        print("Translated name: " + entity_name)
        translated_entities.append(Entity(entity_name, entity.entity_type, entity.start_offset, entity.end_offset))
    
    export_config = config.get('export')
    if export_config is not None:
        exported_rdf = export_entities(translated_entities, export_config)

    if args.out is not None:
        out_path = Path(args.out)
        out_path.write_text(exported_rdf)
    else:
        print(exported_rdf)

def read_yaml_file(path):
    if not path.is_file():
        print(f'Unable to locate file {path}. Exiting...', file=sys.stderr)
        exit(1)

    yml_file = None
    with path.open() as f:
        try:
            yml_file = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f'Unable to read file {path}. Exiting...', file=sys.stderr)
            exit(1)
    return yml_file


registered_translator = {
    'google': translation.GoogleCloudTranslator,
    'googletrans': translation.GoogletransTranslator,
    'mymemory': translation.MyMemoryTranslator,
    'azure': translation.AzureTranslator
}

def translate_text(text, translation_config):
    translator_name = translation_config.get('implementation')
    language_config = translation_config.get('language')
    language_text = language_config.get('text')
    language_extraction = language_config.get('extraction')

    translator_type = registered_translator.get(translator_name)
    translator = translator_type()
    translated_text = translator.translate(text, language_text, language_extraction)
    return translated_text

registered_entity_extractor = {
    'dandelion': extraction.DandelionEntityExtractor
}

def extract_entities(text, extraction_config):
    entity_extractor_name = extraction_config.get('implementation')
    entity_extractor_type = registered_entity_extractor.get(entity_extractor_name)
    entity_extractor = entity_extractor_type()
    entities = entity_extractor.extract_entities(text)
    return entities

registered_coreference_resolver = {
    'stanford': coreference.StanfordCoreferenceResolver
}

def resolve_coreference(text, entities, coreference_config):
    coreference_resolver_name = coreference_config.get('implementation')
    coreference_resolver_type = registered_coreference_resolver.get(coreference_resolver_name)
    if coreference_resolver_type == coreference.StanfordCoreferenceResolver:
        stanford_args = coreference_config.get('stanford') or dict()
        coreference_resolver = coreference.StanfordCoreferenceResolver(**stanford_args)
    else:
        coreference_resolver = coreference_resolver_type()
    mentions = coreference_resolver.resolve_coreferences(text, entities)

    ret_entities = []
    for mention in mentions:
        entity = get_relevant_entity_from_mention(mention)
        if entity is not None:
            ret_entities.append(entity)
    return ret_entities

def get_relevant_entity_from_mention(mention):
    if len(mention) <= 0:
        return None
    for entity in mention:
        if entity.entity_type != extraction.EntityType.THING:
            return entity
    return mention[0]

registered_exporter = {
    'cidoccrm': export.CIDOCCRMExporter
}

def export_entities(entities, export_config):
    exporter_name = export_config.get('implementation')
    exporter_type = registered_exporter.get(exporter_name)
    exporter_namespace = export_config.get('namespaces')
    entity_namespace = exporter_namespace.get('entity')
    ontology_namespace = exporter_namespace.get('ontology')
    export_language = export_config.get('language')
    exporter = exporter_type()
    
    rdf_export = exporter.export(entities, entity_namespace, ontology_namespace, export_language)
    return rdf_export

if __name__ == '__main__':
    main()
