from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # اللوب السحري اللي هيرفع الـ 8 جداول
    for table_name, table_data in data.items():
        table_id = f'encoded-breaker-483217-e5.uber_dataset.{table_name}'
        
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(table_data),
            table_id,
            if_exists='replace',
        )