import os.path

projects_dir = os.path.expanduser('~/Docker-Projects')
projects = [
    {
        'name': 'baseimage',
        'url': 'git@github.com:milo-minderbinder/docker-baseimage.git',
        'branches': ['master']
    },
    {
        'name': 'python',
        'url': 'git@github.com:milo-minderbinder/docker-python.git',
        'branches': ['master']
    },
    {
        'name': 'java-jdk',
        'url': 'git@github.com:milo-minderbinder/docker-java-jdk.git',
        'branches': ['master', 'oracle-java6', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'tomcat7',
        'url': 'git@github.com:milo-minderbinder/docker-tomcat7.git',
        'branches': ['master', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'apache2',
        'url': 'git@github.com:milo-minderbinder/docker-apache2.git',
        'branches': ['master', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'gradle2',
        'url': 'git@github.com:milo-minderbinder/docker-gradle2.git',
        'branches': ['master', 'oracle-java6', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'maven',
        'url': 'git@github.com:milo-minderbinder/docker-maven.git',
        'branches': ['master', 'oracle-java7', 'oracle-java8']
    },
    {
        'name': 'spring-ref',
        'url': 'git@github.com:milo-minderbinder/docker-spring-ref.git',
        'branches': ['master']
    },
    {
        'name': 'example-apache2',
        'url': 'git@github.com:milo-minderbinder/docker-example-apache2.git',
        'branches': ['master']
    },
    {
        'name': 'openam',
        'url': 'git@github.com:milo-minderbinder/docker-openam.git',
        'branches': ['master']
    }
]
