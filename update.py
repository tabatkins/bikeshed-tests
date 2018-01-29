import base64
import os
import sys

from github import Github

# skip files that use <pre class=include>
# https://github.com/foolip/bikeshed-tests/issues/1
SKIP_FILES = {
    'w3c/dom': '*',
    'w3c/fxtf-drafts': 'filter-effects/Overview.bs',
    'w3c/html': '*',
    'w3c/mnx': '*',
    'w3c/uievents': '*',
}

def process_org(org):
    for repo in org.get_repos():
        print 'searching {}'.format(repo.full_name)
        process_repo(repo)

def process_repo(repo):
    try:
        tree = repo.get_git_tree(repo.default_branch, recursive=True)
    except Exception as err:
        if err.status == 409: # "Git Repository is empty"
            return
        raise
    skip_files = SKIP_FILES.get(repo.full_name)
    for entry in tree.tree:
        if entry.type == 'blob' and entry.path.endswith('.bs'):
            if skip_files == '*' or skip_files == entry.path:
                print '  skipping {}'.format(entry.path)
                continue

            print '  found {}'.format(entry.path)

            blob = repo.get_git_blob(entry.sha)
            assert blob.encoding == 'base64'
            text = base64.b64decode(blob.content)

            path = os.path.join('tests', repo.full_name, entry.path)
            dirname = os.path.dirname(path)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            with open(path, 'w+') as f:
                f.write(text)

def main():
    token = os.environ['GH_TOKEN']
    g = Github(token)
    for name in ['w3c', 'whatwg', 'wicg']:
        org = g.get_organization(name)
        process_org(org)

if __name__ == '__main__':
    main()
