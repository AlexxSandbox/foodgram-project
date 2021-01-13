#!/bin/bash

if [[ ! -f `pwd`'/../.env.db' ]]; then

    function get_random {
        base=$(openssl rand -base64 16)
        base_clear=${base/+//}
        base_clear=${base_clear////}
        base_clear=${base_clear//=/}
        echo $base_clear
    }

    touch `pwd`'/.env.db'
    echo "SECRET_KEY=$(get_random)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432" > `pwd`'/.env.db'
fi

echo 'Done.'