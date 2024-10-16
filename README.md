# Workspace Template

## How to Contribute

### Install poetry dependencies

```shell
poetry cache clear --all pypi

poetry update

poetry install --all-extras
```

### Install pre-commit hooks

This project uses [pre-commit](https://pre-commit.com/) to enforce code quality and consistency. To install the pre-commit hooks, run the following command:

```shell
poetry run pre-commit install
```

## How to Add a New Workspace Template

1. Create a new directory in the `templates` directory.
2. Configure template structure in the new directory.
3. Add the template metadata to the `template-metadata.yaml` file.
