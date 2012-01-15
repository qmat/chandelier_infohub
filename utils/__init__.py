import uuid

def uuid_key():
    return str(uuid.uuid4()).replace('-', '')
