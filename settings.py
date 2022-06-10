import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")

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
