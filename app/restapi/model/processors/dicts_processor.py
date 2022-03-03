from haystack.nodes import PreProcessor

processor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=True,
    split_respect_sentence_boundary=True,
    split_overlap=0
)


def process_dicts(_dicts):
    dicts = processor.process(_dicts)
    return dicts
