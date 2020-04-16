import logging
import re
import urllib.parse

import requests


def query_pubchem(compound, by="name"):
    """
    by: either "name" or "smiles"
    https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial$_Toc458584416
    https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Pharmakon1600-01500621/xrefs/SBURL/JSON
    """
    compound_quoted = urllib.parse.quote(compound, safe='')
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/{by}/{compound_quoted}/xrefs/SBURL/JSON"
    response = requests.get(url)
    if not response.ok:
        logging.info(f"query for {compound} returned status code {response.status_code}\n{response.url}")
        return None
    return response.json()


def url_to_drugbank_id(url):
    pattern = re.compile(
        r"https?://(www.)?drugbank.ca/drugs/(?P<drugbank_id>DB[0-9]+)")
    match = pattern.match(url)
    if match:
        return match.group("drugbank_id")


def query_pubchem_for_drugbank(compound, by="name"):
    results = query_pubchem(compound, by=by)
    if not results:
        return None
    results = results["InformationList"]["Information"][0]
    drugbank_ids = sorted(set(filter(None, map(url_to_drugbank_id, results["SBURL"]))))
    if len(drugbank_ids) > 1:
        logging.info(f"{compound} maps to multiple DrugBank IDs: {drugbank_ids}")
    row = dict(
        query_compound=compound,
        pubchem_cid=results["CID"],
        drugbank_id=drugbank_ids[0] if drugbank_ids else None,
    )
    return row
