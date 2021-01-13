#!/bin/bash

if [[ ! -f `pwd`'/../.env.smtp' ]]; then
    touch `pwd`'/.env.smtp'
MAIL_HOST=<EMAIL SMTP>
MAIL_USER=<EMAIL ACCOUNT>
MAIL_PASSWORD=<EMAIL PASSWORD> > `pwd`'/.env.smtp'
fi

echo 'Done.'