CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  name     TEXT NOT NULL,
  password TEXT NOT NULL,
  email    TEXT NOT NULL
);