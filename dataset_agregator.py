import logging
import os
import re
from collections import OrderedDict
from typing import List

import pandas as pd

from settings import ENTITY_TAGS


def create_df_from_files(source_dir: str,
                         save_to_scv: bool = False,
                         output_filename: str = "dataset",
                         ) -> pd.DataFrame:
    """
    Создать pandas.Dataframe из текстовых файлов директории датасета

    :param source_dir: путь до директории датасета
    :param save_to_scv: флаг, для сохранения результата в csv файл
    :param output_filename: имя для сохраняемого файла результата, если выбран флаг save_to_scv
    :return: pandas.Dataframe с колонками ["filename", "text"]
    """
    try:
        logging.info(f"Convert txt-files from {source_dir} to pandas.Dataframe")
        filepath_list = os.listdir(source_dir)
        file_texts = []
        for file_path in filepath_list:
            with open(os.path.join(source_dir, file_path), 'r', encoding='utf-8') as file:
                file_data = file.read().strip('\n')

            file_texts.append(file_data)

        marked_df = pd.DataFrame({"filename": filepath_list,
                                  "text": file_texts
                                  },
                                 )
        if save_to_scv:
            marked_df.to_csv(f"{output_filename}.csv",
                             index=False,
                             )
            logging.info(f"Result DataFrame successful saved to {output_filename}.csv")

        return marked_df

    except Exception as ex:
        logging.error(ex, exc_info=True)


def get_entities_by_tag(tag, source_text) -> List[str]:
    """
    Получить из строки размеченные сущности по имени тэга
    Размеченная сущность в строке имеет вид <TAG>entity text</TAG>

    :param tag: имя тэга
    :param source_text: исходная строка
    :return: список извлеченных сущностей(без повторений)
    """
    all_entities = re.findall(f'<{tag}>([\w\s\d?!:;,]+)</{tag}>', source_text)
    stripped_res = list(OrderedDict.fromkeys(all_entities))
    return stripped_res


def create_entities_df(source_df: pd.DataFrame,
                       save_to_scv: bool = False,
                       output_filename: str = "entities_dataset",
                       ) -> pd.DataFrame:
    """
    Создать pandas.Dataframe из исходного pandas.Dataframe
    с извлеченными размеченными сущностями

    :param source_df: исходный pandas.Dataframe(columns=["filename", "text"])
    :param save_to_scv: флаг, для сохранения результата в csv файл
    :param output_filename: имя для сохраняемого файла результата, если выбран флаг save_to_scv
    :return: pandas.Dataframe с колонками ["filename", "tag", "entity"]
    """
    try:
        logging.info(f"Convert source pandas.Dataframe(columns=['filename', 'text']) to entities Dataframe")
        entity_df = pd.DataFrame(columns=["filename", "tag", "entity"])
        for index, row in source_df.iterrows():
            for tag in ENTITY_TAGS:
                entity_list = get_entities_by_tag(tag, row['text'])
                if entity_list:
                    res_df = pd.DataFrame({"filename": [row["filename"]] * len(entity_list),
                                           "tag": [tag] * len(entity_list),
                                           "entity": entity_list
                                           }
                                          )
                    entity_df = pd.concat([entity_df, res_df], ignore_index=True)

        if save_to_scv:
            entity_df.to_csv(f"{output_filename}.csv",
                             index=False,
                             )
            logging.info(f"Result DataFrame successful saved to {output_filename}.csv")

        return entity_df

    except Exception as ex:
        logging.error(ex, exc_info=True)
