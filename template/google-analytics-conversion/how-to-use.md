# How to Use

## Step 1: Create a Connection

In the "Data" section, set up a connection to BigQuery using your Google Analytics data.
Ensure you name the connection `bq_google_analytics`, as defined in [`./src/sql/ga_data_extraction.sql`].

After creating the connection, you can update the connection name in Data section.

## Step 2: Modify .sql / .py Files

- [`src/sql/ga_data_extraction.sql`]: Update the `FROM` clause to reference your Google Analytics dataset.
- [`src/python/calculate_traffic_flow.py`]: Set the default target link to your conversion URL.
- [`src/python/visualize_traffic_flow.py`]: Set the default target link here as well.

The target link is the URL representing your conversion goal.

If you get some errors, please run each files one by one.

## Step 3: Edit this File (index.mdx)

- Update the `targetLink` variable with your default target link (e.g., `"https://www.morph-data.io/pricing"`).

