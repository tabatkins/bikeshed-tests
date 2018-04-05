# Bikeshed tests auto-updater

This repo collects *.bs files from GitHub repos and creates PRs to update
(bikeshed's tests)[https://github.com/tabatkins/bikeshed/tree/master/tests/github].

## Running locally

You need Python 2 and pip:
```bash
sudo apt install python python-pip
```

Then install the dependencies:
```bash
pip install --user -r requirements.txt
```

The python scripts need `GH_TOKEN` environment variable set to a
[personal access token](https://github.com/settings/tokens/new) with the
"Access public repositories" (public_repo) scope enabled.

To emulate what the Travis job does, execute each step in .travis.yml manually.
