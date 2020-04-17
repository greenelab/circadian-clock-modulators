import re

import requests


def solr_escape(text):
    """
    Escape reserved characters for pysolr queries.
    https://lucene.apache.org/solr/guide/6_6/the-standard-query-parser.html#TheStandardQueryParser-EscapingSpecialCharacters
    https://docs.mychem.info/en/latest/doc/chem_query_service.html#escaping-reserved-characters
    """
    import re
    reserved_chars = r'+ - = && || > < ! ( ) { } [ ] ^ " ~ * ? : \ /'.split()
    pattern = re.compile('|'.join(map(re.escape, reserved_chars)))
    return pattern.sub(repl= lambda m: f"\\{m.group()}", string=text)


def get_mychem_query(name):
    """
    https://lucene.apache.org/solr/guide/6_6/the-standard-query-parser.html
    """
    escaped_name = solr_escape(name)
    search_fields = ["drugbank.name", "drugbank.synonyms"]
    query = " OR ".join(f'{field}:"{escaped_name}"' for field in search_fields)
    query = f"_exists_:drugbank AND ({query})"
    return query


def query_mychem(name):
    url = "https://mychem.info/v1/query"
    params = dict(
        q=get_mychem_query(name),
        fields="drugbank.name,drugbank.id,drugbank.synonyms,drugbank.formula,drugbank.weight",
        size=1,
    )
    response = requests.get(url, params)
    # solr doesn't have a whole target string match mode.
    # For example, "Gallic acid" will match "gallic acid bismuth basic salt"
    return response
