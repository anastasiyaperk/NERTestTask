import logging
import os

from dataset_agregator import create_df_from_files, create_entities_df
from settings import DATASET_DIR

if __name__ == '__main__':
    logging.basicConfig(format=u'[%(asctime)s] %(filename)s [%(levelname)s] %(message)s',
                        level=logging.INFO, )
    marked_data_dir = os.path.join(DATASET_DIR, "marked")
    source_df = create_df_from_files(marked_data_dir, save_to_scv=True)
    entities_df = create_entities_df(source_df, save_to_scv=True)
