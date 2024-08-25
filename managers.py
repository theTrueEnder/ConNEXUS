import random
from contact import Contact
from template import Template
from os import walk
import json
#from abc import ABC, abstractmethod

'''
Manager that allows for adding, reading, and removing of the tags stored in tags.josn
'''
class TagManager():
    def __init__(self, root_path) -> None:
        self.path = root_path
        self.tags = set()
        self.TAGPATH = root_path + '/tags.json'
        self.refresh_tags()

    def refresh_tags(self):
        # open the tags.json file and add any tags that weren't in self.tags to self.tags
        with open(self.TAGPATH, 'r') as f:
            f_tags = json.loads(f.read())

        for tag in f_tags:
            self.tags.add(tag)
        
        # write the updated contents of self.tags to tags.json
        with open(self.TAGPATH, 'w') as f:
            f.write(json.dumps(self.tags))

    
    def get_tags(self) -> set:
        return self.tags
    
    def add_tag(self, tag: str) -> None:
        self.tags.add(tag)

    def remove_tag(self, tag: str) -> None:
        self.tags.remove(tag)



'''
Manager that allows for creating, editing, listing, and removing of Template objects
'''
class TemplateManager():
    def __init__(self, root_path) -> None:
        self.path = root_path
        self.templates = {}

        self.ROOT = root_path
        self.TEMPLATEPATH = root_path + '/templates'

        self.refresh_templates()

    def get_template_list(self) -> set:
        return self.templates.keys()
    
    def refresh_templates(self) -> None:
        # recursively go through the contacts directories and add all contacts into the contacts dict
        for (dir_path, dir_name, file_name) in walk(self.TEMPLATEPATH):
            self.templates.update(
                {file_name: Contact().load(dir_path, file_name)}
            )

    def new_template(self) -> None:
        ... # TODO

    def edit_template(self, id):
        ...

    def remove_template(self, id) -> None:
        ... # TODO



'''
Manager that allows for creating, editing, listing, and removing of Contact objects
'''
class ContactManager():
    def __init__(self, root_path) -> None:
        self.path = root_path
        self.contacts = {}

        self.ROOT = root_path
        self.CONTACTPATH = root_path + '/contacts'

        self.refresh_contacts()

    def refresh_contacts(self) -> int:
        # recursively go through the contacts directories and add all contacts into the contacts dict
        for (dir_path, dir_name, file_name) in walk(self.CONTACTPATH):
            self.contacts.update(
                {file_name: Contact().load(dir_path, file_name)}
            )
        return len(self.contacts)

    def get_contact_list(self):
        return self.contacts.keys()

    '''
    Find an unused id, and create a new Contact with the id
    Returns the new Contact object
    '''
    def new_contact(self, template='default') -> (str, Contact):
        # TODO: implement template
        ctr = 0
        used_ids = self.contacts.keys()
        for i in range(0,2,1):
            id = '%030x' % random.randrange(16**32) # generate 32-digit hex string ID
            if id in used_ids:
                print('ERROR: ID collision =', id)
                ctr += 1
            else:
                self.contacts.update({id: Contact(id)})
                return (id, self.contacts[id])
        
        # if three consecutive ID collisions, raise exception
        if ctr == 3:
            raise RuntimeError('ERROR: 3 consecutive ID collisions')
        

    def remove_contact(self, id):
        ... # TODO

    def edit_contat(self, id):
        ... # TODO