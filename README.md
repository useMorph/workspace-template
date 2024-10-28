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

## How to Add a New Template

1. Create a new directory in the `template` directory with the name of the template.
2. Add the necessary files and directories to the new template directory.
3. Make sure `.env` file is added because if it may be ignored by '.gitignore' file in the template directory.
    ```shell
    git add -f template/${TEMPLATE_DIR}/.env
    ```

### Special Directories in the Template

- `init/sql`: Directory for storing SQL scripts that will be executed when the workspace is initialized.

Example:

```text
├── templates/
    └─ template-name/
        └─ init/
            └─ sql/
                ├─ 0_create_user_table.sql
                └─ 1_insert_sample_data.sql
```

In the above example, the SQL scripts will be executed in the order specified by the prefix number.

If the SQL scripts are not prefixed with numbers, they will be executed in random order.

NB!) In Morph cloud environment, `init` directory will be deleted soon after the scripts are executed.
