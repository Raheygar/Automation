def serialize(obj,file,type):
    if type == 'json':
        import json
        with open('file','w') as f:
            json.dumps(obj,f)
    elif type == 'pickle':
        import pickle
        with open('file','wb')as f:
            pickle.dumps(obj,f)
    else:
        print("Wrong serialization type file")
def deserialize(obj,file,type):
    if type == 'json':
        import json
        with open('file','r')as f:
            json.loads(f)
    elif type == 'pickle':
        import pickle
        with open('file','r')as f:
            pickle.loads(f)
    else:
        print("Wrong de-serialization file type")