"""
This is an example script for how to connect GX Cloud to Microsoft Fabric.

To test, run:
pytest --docs-tests -k "cloud_docs_connect_fabric" tests/integration/test_script_runner.py
"""

# EXAMPLE SCRIPT STARTS HERE:
# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - full code example">
# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - get cloud context">
import great_expectations as gx

context = gx.get_context(mode="cloud")
# </snippet>

# Add a Fabric Data Source
# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - define source">
datasource_name = "Fabric"
host = "myworkspace.datawarehouse.fabric.microsoft.com"
database = "production"
schema = "sales"
port = 1433
encrypt = "Mandatory"
tenant_id = "${ENTRA_ID_TENANT}"
client_id = "${ENTRA_ID_CLIENT_ID}"
client_secret = "${ENTRA_ID_CLIENT_SECRET}"
# </snippet>

# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - add source">
data_source = context.data_sources.add_fabric(
    name=datasource_name,
    host=host,
    database=database,
    schema=schema,
    port=port,
    encrypt=encrypt,
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret,
)
# </snippet>

# Add a Table Data Asset
# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - define table data asset">
data_asset_name = "my_table_asset"
table_name = "my_table"
# </snippet>

# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - add table data asset">
table_data_asset = data_source.add_table_asset(
    table_name=table_name, name=data_asset_name
)
# </snippet>

# Add a Query Data Asset
# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - define query data asset">
data_asset_name = "my_query_asset"
query = "SELECT * from my_table WHERE column1 = 'value' AND column2 > 20"
# </snippet>

data_source = context.data_sources.get(datasource_name)

# <snippet name="docs/docusaurus/docs/cloud/connect/connect_fabric.py - add query data asset">
query_data_asset = data_source.add_query_asset(query=query, name=data_asset_name)
# </snippet>

# </snippet>
