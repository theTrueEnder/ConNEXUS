'''
Definition of a template object
'''


import json
from os import rename

class Template():
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.path = '' # does not include ID
        self.fields = {}
        self.tags = set()
        self.image_path = ''

    '''
    Read in a contact json file at a given directory path
    '''
    def load(self, path) -> None:
        with open(path, 'r') as f:
            template = json.loads(f.read())

        self.id = template["id"]
        self.name = template["name"]
        self.path = template["path"]
        self.fields = template["fields"]
        self.tags = template["tags"]

    '''
    Write a contact file to a json at its path & id
    '''
    def write(self):
        contact = {
            "id":     self.id,
            "name":   self.name,
            "path":   self.path,
            "fields": self.fields,
            "tags":   self.tags,
        }
        with open(self.path+'/'+self.id+'.json', 'w') as f:
            f.write(json.dumps(contact))

        return self.path+'/'+self.id+'.json'
    

    # Location Functions
    
    def get_id(self) -> str:
        return id
    
    def get_path(self) -> str:
        return self.path

    def move(self, new_path) -> str:
        rename(self.path, new_path)
        self.path = new_path
        return new_path


    # Name functions

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name) -> str:
        self.name = name


    # Field functions

    def edit(self, field, value) -> None:
        self.fields[field] = value
    
    def edit(self, pairs) -> None:
        for field, value in pairs:
            self.fields[field] = value

    def get_fields(self) -> set:
        return self.fields.keys()

    def remove_field(self, *fields) -> None:
        for field in self.fields:
            self.fields.pop(field)

    def add_field(self, **fields) -> None:
        self.fields.update(fields)


    # Tag Functions

    def get_tags(self) -> set:
        return self.tags

    def add_tags(self, *tags) -> None:
        for tag in tags:
            self.tags.add(tag)

    def remove_tags(self, *tags) -> None:
        for tag in tags:
            self.tags.remove(tag)

