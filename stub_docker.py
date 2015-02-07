import os
import os.path
import sys


project_dir = os.path.realpath(sys.argv[1])
project_name = os.path.basename(project_dir)
dockerfile_text = '''\
FROM mminderbinder/baseimage
MAINTAINER Milo Minderbinder <minderbinder.enterprises@gmail.com>



# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
CMD ["/sbin/my_init"]
'''
gitignore_text = '''\
*.swp
*.log
'''
readme_text = '# %s' % project_name
if os.path.isdir(project_dir):
    print 'Project already exists!'
    sys.exit(1)
os.mkdir(project_dir)
dockerfile = os.path.join(project_dir, 'Dockerfile')
with open(dockerfile, 'w') as f:
    f.write(dockerfile_text)
gitignore_file = os.path.join(project_dir, '.gitignore')
with open(gitignore_file, 'w') as f:
    f.write(gitignore_text)
dockerignore_file = os.path.join(project_dir, '.dockerignore')
with open(dockerignore_file, 'w') as f:
    f.write(gitignore_text + '\n')
    f.write('.git')
readme_file = os.path.join(project_dir, 'README.md')
with open(readme_file, 'w') as f:
    f.write(readme_text)
