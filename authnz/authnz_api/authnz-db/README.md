# authnz-db

This directory contains a script which is a command-line interface to the database.
This abstracts away any logic specific to databases, so applications can be written
to merely call the command-line tool and forget about database specifics.

The default is for the script to use an SQLite database. In the future it might
support other databases, such as Postgres. In this way, databases can be changed
without ever changing application code.
