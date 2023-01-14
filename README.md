# Python package "mypackage"

## Let's get started!

**First, you should create a directory in the src directory with the name to be used during import like 'mypkg'.**

### Directory structure
**src-layout**
```
package_root
├── pyproject.toml
├── ...
└── src/
    └── mypkg/
        ├── __init__.py
        ├── ...
        ├── module.py
        └── subpkg1/
            ├── __init__.py
            ├── ...
            └── module1.py
```


## To upload package to PyPI
If you would like to upload this package to pypi.org or test.pypi.org, you must set the API key for test.pypi.org as TEST_PYPI_API_TOKEN and the API key for pypi.org as PYPI_API_TOKEN in the GitHub Actions Secret.

If you wouldn't like to upload this package to PyPI, you need to remove .github/workflows/Publish-to-PyPI.yml or disable it.
