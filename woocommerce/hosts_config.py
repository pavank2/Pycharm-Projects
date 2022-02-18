
API_HOSTS = {
    "test": "http://192.168.0.101:8888/coolsite/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}
WOO_API_HOSTS = {
    "test": "http://192.168.29.173:8888/coolsite/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
              "test": {"host": "127.0.0.1",
                       "database": "coolsite",
                       "table_prefix": "wp_",
                       "socket": "/Users/admas/Library/Application Support/Local/run/5MQbIjSnl/mysql/mysqld.sock",
                       "port": 8889
                       },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 8889
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'docker': {
              "test": {
                  "host": "host.docker.internal",
                  "database": "wp398",
                  "table_prefix": "wp2p_",
                  "socket": None,
                  "port": 3306
              },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'machine2': {
        "test": {"host": "localhost",
                 "database": "local",
                 "table_prefix": "wp_",
                 "socket": "/Users/akinfu/Library/Application Support/Local/run/d84nqkpSm/mysql/mysqld.sock",
                 "port": 3306
                 },
        "dev": {
                  "host": "host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
        "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
    }
}
