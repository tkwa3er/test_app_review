import os

# The template for the project folder structure
template1 = {
    "project_folder": {
        "data": {},
        "docs": {
            "reports": {},
            "presentations": {}
        },
        "src": {
            "code": {},
            "tests": {}
        }
    }
}
template2 = {
    "project_folder": {
        "data": {},
        "docs": {
            "specifications": {},
            "presentations": {}
        },
        "src": {
            "code": {},
            "tests": {}
        }
    }
}
# The templates
templates = {
    'template1': template1,
    'template2': template2
}

# The path to the parent directory where the project folder will be created
parent_directory = "~"

with open("~/.vscode-insiders/extensions/tekab.dev.tekabfoldgen-0.0.1/fff.txt","w") as f:
	f.write('656565656565565')
	f.close()

# The name of the project folder to be created
project_folder_name = "my_project"

def create_project_folder(parent_directory, project_folder_name, template=None):
    """
    Creates a project folder structure using the given template.

    :param parent_directory: The path to the parent directory where the project folder will be created
    :param project_folder_name: The name of the project folder to be created
    :param template: A dictionary representing the template for the project folder structure
    """
    project_folder_path = os.path.join(parent_directory, project_folder_name)
    os.makedirs(project_folder_path)

    for folder_name, subfolders in template.items():
        current_folder_path = os.path.join(project_folder_path, folder_name)
        os.makedirs(current_folder_path)
        create_project_folder(current_folder_path, subfolders)


# create project using the template of your choice
template_name = 'template1'
create_project_folder(parent_directory, project_folder_name, templates[template_name])
