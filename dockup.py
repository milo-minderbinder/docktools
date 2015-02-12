import os
import os.path
import sys
import shutil
import subprocess
import dockupconf


projects_dir = dockupconf.projects_dir
if not os.path.isdir(projects_dir):
    os.mkdir(projects_dir)
print 'Docker projects directory: %s' % projects_dir

projects = dockupconf.projects


def clone_projects():
    print 'Cloning projects...'
    for project in projects:
        project_dir = os.path.join(projects_dir, project['name'])
        if not os.path.isdir(project_dir):
            print subprocess.check_output(
                ['git', 'clone', project['url'], project_dir])
        else:
            print 'Skipping %s - directory already exists: %s' \
                % (project['name'], project_dir)
    print 'done!'


def git_info():
    for project in projects:
        print '\nGit info for %s' % project['name']
        project_dir = os.path.join(projects_dir, project['name'])
        os.chdir(project_dir)
        print subprocess.check_output(['git', 'fetch', '--all'])
        print 'Status:'
        print subprocess.check_output(['git', 'status'])
        print 'Local branch info:'
        print subprocess.check_output(['git', 'branch', '-vv'])
        print 'Remote branch info:'
        print subprocess.check_output(['git', 'branch', '-vv', '-r'])
        print '-' * 80


def build_projects():
    for project in projects:
        project_dir = os.path.join(projects_dir, project['name'])
        print 'Moving to %s' % project_dir
        os.chdir(project_dir)
        print subprocess.check_output(['git', 'fetch', '--all'])
        for branch in project['branches']:
            print 'Building branch %s of %s' % (branch, project['name'])
            print subprocess.check_output(['git', 'checkout', branch])
            print subprocess.check_output(['git', 'status'])
            if branch == 'master':
                tag = ''
            else:
                tag = ':%s' % branch
            print subprocess.check_output(
                ['docker', 'build', '-t',
                 'mminderbinder/%s%s' % (project['name'], tag),
                 project_dir])
            print '\n\n'
        print '-' * 80


def main():
    usage = '''dockup.py - Docker project manager
    python dockup.py [command]
    Commands:
        clone   - clone all projects into Docker project directory
        info    - fetch updates and print git status and branch info for projects
        build   - build all projects'''

    if not len(sys.argv) > 1:
        print usage
        sys.exit(1)
    command = sys.argv[1]
    if command == 'clone':
        clone_projects()
    elif command == 'info':
        git_info()
    elif command == 'build':
        build_projects()
    else:
        print usage


if __name__ == '__main__':
    main()
