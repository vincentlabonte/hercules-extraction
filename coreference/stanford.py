from stanfordnlp.server import CoreNLPClient

from coreference.base import CoreferenceResolver


class StanfordCoreferenceResolver(CoreferenceResolver):

    def __init__(self, start_server=True, endpoint=CoreNLPClient.DEFAULT_ENDPOINT):
        self.__client = CoreNLPClient(start_server=start_server, endpoint=endpoint, annotators=[
                                      'tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse', 'coref'], output_format='json')
        self.__client.start()

    def __del__(self):
        self.__client.stop()

    def resolve_coreferences(self, text, entities):
        annotations = self.__client.annotate(text)

        entity_mention_indices = []
        for chain in annotations.corefChain:
            mention_indices = []
            for mention in chain.mention:
                sentence = annotations.sentence[mention.sentenceIndex]
                token_start = sentence.token[mention.beginIndex]
                token_end = sentence.token[mention.endIndex - 1]
                char_start = token_start.beginChar
                char_end = token_end.endChar
                mention_indices.append((char_start, char_end))
            entity_mention_indices.append(mention_indices)

        entity_sets = [list() for _ in range(len(entity_mention_indices))]
        for entity in entities:
            is_coreferred = False
            for i, mention_indices in enumerate(entity_mention_indices):
                for start_index, end_index in mention_indices:
                    if entity.start_offset >= start_index and entity.end_offset <= end_index:
                        entity_sets[i].append(entity)
                        is_coreferred = True
            if not is_coreferred:
                entity_sets.append([entity])
        return entity_sets
