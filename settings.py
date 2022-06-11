import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")
NER_PATH = os.path.join(ROOT_DIR, "ner_data")

# Список тэгов сущностей
ENTITY_TAGS = ["CVE",
               "CWE",
               "SOFTWARE",
               "MALWARE",
               "COURSE_OF_ACTION",
               "INTRUSION_SET",
               "THREAT_ACTOR",
               "TOOL",
               "ATTACK_PATTERN",
               "INDUSTRY",
               "MITRE_ATTACK",
               "CAMPAIGN",
               "ORG",
               "COUNTRY",
               "CITY",
               "GEOLOCATION",
               "TIMESTAMP",
               ]

# Настройки flask приложения
APP_HOST = "localhost"
APP_PORT = 5000
