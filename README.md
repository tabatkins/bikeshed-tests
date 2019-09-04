# Bikeshed tests auto-updater

This repo collects *.bs files from GitHub repos and creates PRs to update
[bikeshed's tests](https://github.com/tabatkins/bikeshed/tree/master/tests/github).

## Adding Your Specs

If you'd like to add your own specs to Bikeshed's regression test-suite,
submit a PR for the [`specs.data`](https://github.com/foolip/bikeshed-tests/blob/master/specs.data) file.

This file format is line-based:
to add your entire organization, add a `+org: orgname` line;
to add a single repo, add a `+repo: user/repo` line.
to add a single *file*, add a `+file: user/repo/path/to/file.bs` line.
If you need to exclude any repos or files, use a `-repo` or `-file` line instead.
(`-file` lines can use shell wildcarding conventions to exclude multiple files,
as implemented by the Python [fnmatch](https://docs.python.org/2/library/fnmatch.html) module.)

The files to be processed by this tool must have the `.bs` extension;
if you specify a repo or an org,
the entire repo/org will be crawled for `.bs` files.

Indentation does not matter, but can be used for readability,
to group some `-` lines underneath the larger `+` line that would include them.

Lines starting with `#` are comments and are ignored;
blank lines are also ignored.

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
