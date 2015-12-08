def format_string(string):
    string = string + '                  '
    return string[:18]


def empty(name=None, street=None, city=None, country=None):

    empty_postcard = \
"""--------------------------------------------------------------------
|                                         |                 #####  |
|                                         |                 #####  |
|                                         |                 #####  |
|                                         |                        |
|                                         |                        |
|                                         |                        |
|                                         |  NAME             .    |
|                                         |                        |
|                                         |  STREET           .    |
|                                         |                        |
|                                         |  CITY             .    |
|                                         |                        |
|                                         |  COUNTRY          .    |
|                                         |                        |
--------------------------------------------------------------------""".split('\n')

    if name:
        name = format_string(name)
        empty_postcard[7] = empty_postcard[7].replace('NAME             .', name)
    if street:
        street = format_string(street)
        empty_postcard[9] = empty_postcard[9].replace('STREET           .', street)
    if city:
        city = format_string(city)
        empty_postcard[11] = empty_postcard[11].replace('CITY             .', city)
    if country:
        country = format_string(country)
        empty_postcard[13] = empty_postcard[13].replace('COUNTRY          .', country)

    return empty_postcard
