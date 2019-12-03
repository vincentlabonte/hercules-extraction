from export.base import Exporter
from rdflib import Graph, Literal, URIRef, Namespace, BNode
from rdflib.namespace import RDF, RDFS
from urllib import parse
from extraction.base import EntityType
import uuid


class CIDOCCRMExporter(Exporter):

    __entity_type_to_ontlogy_type = {
        EntityType.EVENT: 'E5_Event',
        EntityType.ACTIVITY: 'E7_Activity',
        EntityType.MANMADEOBJECT: 'E22_Man-Made_Object',
        EntityType.ADDRESS: 'E45_Address',
        EntityType.DATE: 'E50_Date',
        EntityType.PLACE: 'E53_Place',
        EntityType.PERSON: 'E21_Person',
        EntityType.THING: 'E70_Thing',
        EntityType.GROUP: 'E74_Group',
    }

    def export(self, entities, entity_namespace, ontology_namespace, export_language):
        entity_namespace = Namespace(entity_namespace)
        ontology_namespace = Namespace(ontology_namespace)
        g = Graph()

        for entity in entities:
            entity_uuid = str(uuid.uuid4())
            g.add((entity_namespace.term(entity_uuid), RDF.type, ontology_namespace.term(
                CIDOCCRMExporter.__entity_type_to_ontlogy_type[entity.entity_type])))
            g.add((entity_namespace.term(entity_uuid),
                   RDFS.label, Literal(entity.name, lang='fr')))
        return g.serialize(format=export_language).decode('utf-8')
