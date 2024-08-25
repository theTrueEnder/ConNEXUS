from managers import ContactManager, TemplateManager, TagManager
from os import getcwd
from contact import Contact
cwd = getcwd()
cm = ContactManager(cwd) # imports contacts and templates into memory

'''

Root[]
  |
  |- Contacts[]
  |
  |- Templates[]
  |
  |- Journal/Memories[]
  |
  |- tags.json
  |
  |- config.json





'''


def list_contacts():
    print(cm.get_contact_list())

def add_new_contact():
    (id, contact) = cm.new_contact()
    directory = input('Enter target directory path: ')
    contact.move(directory)
    #self.fields = {}
    #self.tags = set()
    #self.image_path = ''
    ...

def edit_contact():
    ...


def list_templates():
    print(cm.get_template_list())

def add_new_template():
    ...

def edit_template():
    ...







actions = []

while(actions[-1] != 'quit'):
    print('''
          Select an action:
            c - View Contact actions
                cv - View list of Contacts
                ca - Add new Contact
                ce - Edit a Contact
          
            t - View Template actions
                tv - View list of Templates
                ta - Add new Template
                te - Edit a Template
          
            d - View Directory actions
                dv - View list of directories
                da - Add new directory (unimplemented)
                dr - Remove a directory (unimplemented)
            q - Quit
          ''')
    
    match input().lower():
        # Contact options
        case 'c': 
            actions += ['contact']
            print('''
                Select a Contact action:
                    cv - View list of Contacts
                    ca - Add new Contact
                    ce - Edit a contact
                    q - Quit
            ''')

        case 'cv':
            actions += ['contact-list']
            list_contacts()
        
        case 'ca':
            actions += ['contact-add']
            add_new_contact()

        case 'ce':
            actions += ['contact-edit']
            edit_contact()


        # Template options
        case 't':
            actions += ['template']
            print('''
                t - View Template actions
                    tv - View list of Templates
                    ta - Add new Template
                    te - Edit a Template
            ''')

        case 'tv':
            actions += ['template-list']
            list_templates()
        
        case 'ta':
            actions += ['template-add']
            add_new_template()
        
        case 'te':
            actions += ['template-edit']
            edit_template()

        # Directory options
        case 'd':
            actions += ['directory']
            print('''
                d - View Directory actions
                    dv - View list of directories (unimplemented)
                    da - Add new directory (unimplemented)
                    dr - Remove a directory (unimplemented)
            ''')
        case 'q':
            actions += ['quit']
            continue
        case _:
            break