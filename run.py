import gitlab
import re

from gitlab.config import GitlabConfigMissingError
from config.gitlab import GitlabConfig
from repo import Elastic

glconfig = GitlabConfig()
elastic = Elastic()
gl = gitlab.Gitlab(glconfig.GL_HOST, private_token=glconfig.GL_KEY)

def get_projects(group_id):
    list_projects = []
    for project in group.projects.list():
        list_projects.append(project.attributes)

    return list_projects

def get_gitflow_projects(project_id, project_name, path_with_namespace):
    gitflow_branches = ['feature', 'release', 'hotfix']
    project = gl.projects.get(project_id)

    for branch in project.branches.list():
        if re.compile('|'.join(gitflow_branches),re.IGNORECASE).search(branch.name):
            data = branch.__dict__['_attrs']
            data["project_id"] = project_id
            data["project_name"] = project_name
            data["path_with_namespace"] = path_with_namespace
            elastic.insert(data, "gitflow")

for group in gl.groups.list():
    list_projects = get_projects(group.attributes['id'])
    print(list_projects)
    for project in list_projects:
        get_gitflow_projects(project['id'], project['name'], project['path_with_namespace'])
