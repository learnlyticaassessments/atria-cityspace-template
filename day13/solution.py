def s3_uri(bucket, key):
    # TODO: build "s3://<bucket>/<key>"; a leading "/" on key must be stripped
    raise NotImplementedError

def put_object(store, key, value):
    # TODO: return a NEW dict with key set to value (do not mutate store)
    raise NotImplementedError

def get_object(store, key):
    # TODO: return the stored value, or None if key is absent
    raise NotImplementedError

def list_prefix(store, prefix):
    # TODO: return the sorted list of keys that start with prefix
    raise NotImplementedError
