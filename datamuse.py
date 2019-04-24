"""Provides functions for making requests to the datamuse API.

URL: https://www.datamuse.com/api/
"""

import urllib.request
import urllib.parse
import json

ENDPOINTS = (
    'words',
    'sug'
)

QUERY_PARAMATERS = (
    'ml',
    'sl',
    'sp',
    'rel_jja',
    'rel_jjb',
    'rel_syn',
    'rel_trg',
    'rel_ant',
    'rel_spc',
    'rel_gen',
    'rel_com',
    'rel_par',
    'rel_bga',
    'rel_bgb',
    'rel_rhy',
    'rel_nry',
    'rel_hom',
    'rel_cns',
    'v',
    'topics',
    'lc',
    'rc',
    'max',
    'md',
    'qe',
    'ipa'
)

METADATA_FLAGS = (
    'd',
    'p',
    's',
    'r',
    'f'
)


def _validate_params(endpoint='words', **kwargs):
    """Raises an error if any of the query parameters in kwargs is invalid.

    Raises:
        ValueError: invalid endpoint "{endpoint}"
        ValueError: invalid query paramater "{param}"
        ValueError: invalid metadata flag "{flag}"
    """

    if endpoint not in ENDPOINTS:
        raise ValueError(f'invalid endpoint "{endpoint}""')

    for param in kwargs:
        if param not in QUERY_PARAMATERS:
            raise ValueError(f'invalid query paramater "{param}"')

    if 'md' in kwargs:
        for flag in kwargs['md']:
            if flag not in METADATA_FLAGS:
                raise ValueError(f'invalid metadata flag "{flag}"')

    return True


def _create_URL(endpoint='words', **kwargs):
    """Returns a datamuse API compliant URL containing the given endpoint and
    query paramaters.
    """

    scheme = 'https'
    netloc = 'api.datamuse.com'
    path = endpoint
    params = ''
    query = urllib.parse.urlencode(kwargs)
    fragment = ''
    components = (scheme, netloc, path, params, query, fragment)

    return urllib.parse.urlunparse(components)


def request(endpoint='words', **kwargs):
    """Makes a request to the datamuse API with the given query paramaters.
    
    Args:
        endpoint (str): either 'words' or 'sug'
        kwargs: query paramaters with their corresponding value

    Example call:
        request(ml='duck', sp='b*', max=10)
    """

    _validate_params(endpoint, **kwargs)

    for param in kwargs:
        kwargs[param] = str(kwargs[param])

    url = _create_URL(endpoint, **kwargs)
    print(url)

    results = urllib.request.urlopen(url).read()
    results = json.loads(results)

    return results

