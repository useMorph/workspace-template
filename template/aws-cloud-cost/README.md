# Welcome to your Morph project!

This document explains the basic structure and files of the Morph project. Please read through it before starting the
operation of your project.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Morph YAML File](#morph-yaml-file)
- [Editing and Updating Files](#editing-and-updating-files)
- [Applying Settings in Local Environment](#applying-settings-in-local-environment)
- [Support](#support)

## Project Overview

This project is a Morph project for building and managing data pipelines. It was created using `morph-cli` and includes
the basic structure and files necessary for project setup and management.

## Directory Structure

```plaintext
├── canvases/
│   └─ sample_canvas.json // An example canvas file
├── src/
│   ├─ pages
│   │  └─ page1.mdx // An example MDX application page
│   ├─ python
│   │  └─ visualize.py // An example visualization script
│   ├─ sql
│   │  │─ get_all_orders.sql
│   │  └─ calculate_customer_orders.sql
│   └─ visualization
│      └─ get_orders.vg.json // An example Vega-Lite visualization file
├── templates/
├── .env
├── .gitignore
├── morph_project.sqlite3
├── morph.yaml
├── pyproject.toml
└── README.md
```

- `canvases/`: Directory for storing canvas files.
- `src/`: Directory for storing source files.
  - `pages/`: Directory for storing MDX application pages.
  - `python/`: Directory for storing Python scripts.
  - `sql/`: Directory for storing SQL scripts.
  - `visualization/`: Directory for storing visualization files.
- `templates/`: Directory for storing user-defined custom templates.
- `.env`: File for setting environment variables.
- `.gitignore`: File for specifying files and directories to exclude from Git.
- `morph_project.sqlite3`: SQLite database file for the project.
- `morph.yaml`: Project configuration file.
- `pyproject.toml`: Python project configuration file.
- `README.md`: Project description file.

## Morph YAML File

The `morph.yaml` file is the management file for this project and describes the basic configuration of the project. This
file includes information about the configuration of the data pipeline, the paths to each cell, and the output
destinations.

## Editing and Updating Files

When editing or creating new files in the project, you may need to manually update the `morph.yaml` file. This ensures
that new or modified files are correctly reflected in the project settings.

## Applying Settings in Local Environment

This step is unnecessary for the cloud version, but if you are operating this project in a local environment, you need
to run the following command after editing the `morph.yaml` file to apply the project settings:

```bash
morph sync
```

This command reflects the contents of `morph.yaml` in the project and applies the settings correctly.

## Support

If you have any questions or need support regarding the project, please refer to the [official documentation](https://docs.morphdb.io) or contact the support team on our [Discord server](https://discord.gg/BGmpQQUEUZ).
