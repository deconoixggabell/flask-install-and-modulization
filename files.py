# Import everthing from Folders
from Folders import *


# file names
server = "server.py"
read_me = "Read_Me.md"
flask_app = "__init__.py"
config = "mysqlconnection.py"
controller = "controller.py"
module = "module.py"
template_index = "index.html"
template_contact = "contact.html"
template_about = "about.html"
static_css = "style.css"
static_js = "main.js"

# messages
error_1 = "file already exists"
successful = "File Created"

# envirment server files
os.chdir(path)
if not os.path.exists(server):
    with open(server, 'w') as f:
        f.close()
        print(f"{successful}: {server}")
else:
    print(f"{error_1}: {server}")

os.chdir(path)
if not os.path.exists(read_me):
    with open(read_me, 'w') as f:
        f.close()
        print(f"{successful}: {read_me}")
else:
    print(f"{error_1}: {read_me}")

# file creation the Flask App
os.chdir(path_flask_app)
if not os.path.exists(flask_app):
    with open(flask_app, 'w') as f:
        f.close()
        print(f"{successful}: {flask_app}")
else:
    print(f"{error_1}: {flask_app}")

# file creation for the sql config
os.chdir(path_config)
if not os.path.exists(config):
    with open(config, 'w') as f:
        f.close()
        print(f"{successful}: {config}")
else:
    print(f"{error_1}: {config}")

# file creation for the module
os.chdir(path_module)
if not os.path.exists(module):
    with open(module, 'w') as f:
        f.close()
        print(f"{successful}: {module}")
else:
    print(f"{error_1}: {module}")
# file creation for the controllers
os.chdir(path_controllers)
if not os.path.exists(controller):
    with open(controller, 'w') as f:
        f.close()
        print(f"{successful}: {controller}")
else:
    print(f"{error_1}: {controller}")

# file creation for the templates HTMl
os.chdir(path_templates)
if not os.path.exists(template_index):
    with open(template_index, 'w') as f:
        f.close()
        print(f"{successful}: {template_index}")
else:
    print(f"{error_1}: {template_index}")

if not os.path.exists(template_contact):
    with open(template_contact, 'w') as f:
        f.close()
        print(f"{successful}: {template_contact}")
else:
    print(f"{error_1}: {template_contact}")

if not os.path.exists(template_about):
    with open(template_about, 'w') as f:
        f.close()
        print(f"{successful}: {template_about}")
else:
    print(f"{error_1}: {template_about}")

# file creation for the static files CSS JS
os.chdir(path_static)
if not os.path.exists(static_css):
    with open(static_css, 'w') as f:
        f.close()
        print(f"{successful}: {static_css}")
else:
    print(f"{error_1}: {static_css}")

if not os.path.exists(static_js):
    with open(static_js, 'w') as f:
        f.close()
        print(f"{successful}: {static_js}")
else:
    print(f"{error_1}: {static_js}")

# printing everthing from the path which is also the Project location
for dirpath, dirnames, filenames in os.walk(f"{project_location}/{project_name}"):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)