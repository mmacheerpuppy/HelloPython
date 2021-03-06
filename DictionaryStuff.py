/**
Aggregate key values for keys in a list of dicts
**/

def aggregate_key_values(dict_list: list, keys: list):
    return {k: sum(d.get(k, 0) for d in dict_list) for k in keys}



/** 

Lets say you have some values

dict_list  = [
    {
    'legs': 2,
    'paws': 2,
    'name': 'fido'
    },
    {
    'legs': 2,
    'paws': 2,
    'name': 'fido'
    },
    {
    'legs': 2,
    'paws': 2,
    'name': 'freddie'
    }
]
keys = ['legs', 'paws']
filter = "fido"


You want to say "Give me an aggregate of all dict values for dogs named fido, but do that just by scanning for the word "fido" in the values and if that value exists, then add it to the list

u can do that with this c:
**/
def aggregate_key_values_at_filter(dict_list: list, keys: list, filter: list):
    return {k: sum(d.get(k, 0) for d in dict_list if any(f in d.values() for f in filter)) for k in keys}
