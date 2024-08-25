'''
Definition of a contact object
'''


import json
from os import rename

class Contact():
    def __init__(self, id):
        self.id = id
        self.path = '' # does not include ID
        self.fields = {}
        self.tags = set()
        self.image_path = ''

    '''
    Read in a contact json file at a given directory path
    '''
    def load(self, path):
        with open(path, 'r') as f:
            contact = json.loads(f.read())

        self.id = contact["id"]
        self.path = contact["path"]
        self.fields = contact["fields"]
        self.tags = contact["tags"]
        self.image_path = contact["image_path"]

        return self
    '''
    Write a contact file to a json at its path & id
    '''
    def write(self) -> str:
        contact = {
            "id":     self.id,
            "path":   self.path,
            "fields": self.fields,
            "tags":   self.tags,
            "image_path": self.image_path
        }
        with open(self.path+'/'+self.id+'.json', 'w') as f:
            f.write(json.dumps(contact))

        return self.path+'/'+self.id+'.json'

    def __str__(self) -> str:
        s = f'''
        Contact {self.id}:
            Location: {self.path}
            Image Path: {self.image_path}
            Fields:

        '''
        for (field, value) in self.fields:
            s += f'                {field}: {value}'

        s += '            Tags:\n'
        for tag in self.tags:
            s += f'                {tag}'

        return s

    # Location Functions
    
    def get_id(self) -> str:
        return id
    
    def get_path(self) -> str:
        return self.path

    def move(self, new_path) -> str:
        rename(self.path, new_path)
        self.path = new_path
        return new_path


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



    # Image Functions

    def get_image(self) -> str:
        return self.image_path
    
    def set_image(self, path) -> None:
        self.image = path