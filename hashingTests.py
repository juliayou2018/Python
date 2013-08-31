def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results

def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets

def hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        h += ord(c)
    return h % buckets

def make_hashtable(nbuckets):
    hash_table = []
    for i in range(nbuckets):
        hash_table.append([])
    return hash_table

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable, key).append([key, value])
    return htable 

def hashtable_lookup(htable,key):
    value = None
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            value = entry[1]
    return value

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return htable
    bucket.append([key, value])

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def involved(courses, person):
    output = {}
    for hexamester in courses:
        for course in courses[hexamester]:
            for key in courses[hexamester][course]:
                if courses[hexamester][course][key] == person:
                    if hexamester in output:
                        output[hexamester].append(course)
                    else:
                        output[hexamester] = [course]
    return output