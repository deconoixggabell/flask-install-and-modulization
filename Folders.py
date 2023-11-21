import os

# The location where our flask folders will be created
project_location = "enter the file location here"

project_name = "Task"
flask_app = "flask_app"
config = "config"
module = "module"
controllers = "controller"
templates = "templates"
static = "static"


# messages definitions
error_folder_1 = "Folder already exists"
successful_folder = "Folders Created"

# folder creation
path = f"{project_location}/{project_name}"
path_flask_app = f"{project_location}/{project_name}/{flask_app}"
path_config = f"{project_location}/{project_name}/{flask_app}/{config}"
path_module = f"{project_location}/{project_name}/{flask_app}/{module}"
path_controllers = f"{project_location}/{project_name}/{flask_app}/{controllers}"
path_templates = f"{project_location}/{project_name}/{flask_app}/{templates}"
path_static = f"{project_location}/{project_name}/{flask_app}/{static}"

# conditional statement To make sure that the Project doesn't exist
if not os.path.exists(path):
    os.makedirs(path)
    os.makedirs(path_flask_app)
    os.makedirs(path_config)
    os.makedirs(path_module)
    os.makedirs(path_controllers)
    os.makedirs(path_templates)
    os.makedirs(path_static)
    print(successful_folder)
else:
    print(error_folder_1)
