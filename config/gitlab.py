import os

class GitlabConfig:
    GL_HOST = os.environ.get('GL_HOST')
    GL_KEY = os.environ.get('GL_KEY')