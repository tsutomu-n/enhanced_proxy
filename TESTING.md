# Testing in This Project

## Table of Contents

- [Testing in This Project](#testing-in-this-project)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Environment List](#environment-list)
  - [Common Configuration](#common-configuration)
    - [Defining Dependencies](#defining-dependencies)
    - [Base Environment](#base-environment)
    - [Unit Test Environment](#unit-test-environment)
    - [Integration Test Environment](#integration-test-environment)
    - [Other Environments](#other-environments)
    - [Code Coverage Configuration](#code-coverage-configuration)
    - [flake8 Configuration](#flake8-configuration)
    - [GitHub Actions Configuration](#github-actions-configuration)
    - [Glossary](#glossary)
    - [References](#references)

## Overview

In this project, we use [tox](https://tox.readthedocs.io/) to manage various tasks such as running tests, checking code conventions, and cleaning up temporary files. The `tox.ini` file contains the configuration for executing these tasks.

## Environment List

- `py37`, `py38`, `py39`, `py310`, `py311`: Test execution environments for different Python versions
- `flake8`: Code convention checking environment
- `clean`: Temporary file cleanup environment

## Common Configuration

### Defining Dependencies

The common dependencies are defined in the `[tox:vars]` section using the `deps` variable.

```ini
[tox:vars]
deps =
    pytest
    pytest-cov
    pytest-xdist
```

### Base Environment
The [testenv:base] section defines the common configuration for test execution. Other environments inherit this configuration.

```ini
[testenv:base]
deps = {[tox:vars]deps}
commands =
    pytest --cov=enhanced_proxy --cov-report=html --cov-report=term --log-file={envtmpdir}/{envname}.log --log-file-level=DEBUG -n auto {posargs}
```
deps: Inherits the common dependencies.
commands: Defines the pytest execution command.
--cov: Enables code coverage measurement.
--cov-report: Generates reports in HTML and terminal output formats.
--log-file: Outputs the execution log to a file with the environment name included.
--log-file-level: Sets the log level to DEBUG.
-n auto: Runs tests in parallel.
{posargs}: Accepts additional command-line options.

### Unit Test Environment
The [testenv] section defines the environment for running unit tests.

```ini
[testenv]
basepython = {env:TOXPYTHON:python}
deps = {[testenv:base]deps}
commands = {[testenv:base]commands} -m "not integration" tests/unit
```
basepython: Specifies the Python version to run.
deps: Inherits dependencies from the base environment.
commands: Inherits commands from the base environment and adds the -m "not integration" option to run tests without the integration marker. Tests in the tests/unit directory are targeted.

### Integration Test Environment

The [testenv:integration] section defines the environment for running integration tests.

```ini
[testenv:integration]
basepython = {env:TOXPYTHON:python}
deps =
    {[testenv:base]deps}
    requests
    responses
commands = {[testenv:base]commands} -m "integration" tests/integration
```

deps: In addition to the base environment dependencies, requests and responses are installed.
commands: Inherits commands from the base environment and adds the -m "integration" option to run tests with the integration marker. Tests in the tests/integration directory are targeted.

### Other Environments
[testenv:flake8]: Environment for running code convention checks.
[testenv:clean]: Environment for cleaning up temporary files.

###　pytest Configuration
The `[pytest]` section configures pytest.

```ini
[pytest]
addopts = -ra
markers =
    integration: Integration tests  # Marker for integration tests
    unit: Unit tests  # Marker for unit tests
```
addopts: Additional command-line options are specified. -ra displays the results of all tests.
markers: Defines markers for integration and unit tests.

### Code Coverage Configuration
The [coverage:run], [coverage:report], and [coverage:html] sections configure code coverage measurement and reporting.

```ini
[coverage:run]
source =
    enhanced_proxy

[coverage:report]
show_missing = True
precision = 2
omit =
    */tests/*
    */site-packages/*

[coverage:html]
directory = htmlcov
```
[coverage:run]: Limits code coverage measurement to the enhanced_proxy package.
[coverage:report]: Shows missing coverage, displays precision up to two decimal places, and omits the tests and site-packages directories from coverage measurement.
[coverage:html]: Outputs the HTML code coverage report to the htmlcov directory.

### flake8 Configuration
The [flake8] section configures the flake8 tool.

```ini
[flake8]
max-line-length = 120
extend-ignore = E203  # Ignored error code
ignore-comments = TODO  # Ignores TODO comments
exclude =
    .git,
    .tox,
    build,
    dist,
    *.egg-info
    htmlcov
```
max-line-length: Sets the maximum line length to 120 characters.
extend-ignore: Ignores the E203 error code.
ignore-comments: Ignores TODO comments.
exclude: Excludes specified directories and files from code convention checks.

### GitHub Actions Configuration
The [gh-actions] section configures tox execution on GitHub Actions.

```ini
[gh-actions]
python =
    3.7: py37
    3.8: py38
    3.9: py39
    3.10: py310
    3.11: py311, flake8, clean
```

This configuration specifies the Python versions and environments to run on GitHub Actions. For example, for Python 3.11, the py311, flake8, and clean environments will be executed.

### Glossary
deps: Dependencies to be installed in the environment.
basepython: The Python version to run in the environment.
envlist: The list of environments to be executed by tox.

### References
tox documentation
pytest documentation
Code Coverage in Python
flake8 documentation

