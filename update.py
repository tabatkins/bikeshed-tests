import base64
import os
import sys

from github import Github

def main():
    token = os.environ['GH_TOKEN']
    g = Github(token)
    for name in ['w3c', 'whatwg', 'wicg']:
        for repo in g.get_organization(name).get_repos():
            print 'searching {}'.format(repo.full_name)
            tree = repo.get_git_tree(repo.default_branch, recursive=True)
            for entry in tree.tree:
                if entry.type == 'blob' and entry.path.endswith('.bs'):
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

if __name__ == '__main__':
    main()
