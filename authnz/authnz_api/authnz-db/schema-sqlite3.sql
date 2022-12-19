CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id  TEXT UNIQUE NOT NULL,
  name     TEXT NOT NULL,
  email    TEXT NOT NULL,
  password TEXT NOT NULL,
  token    TEXT UNIQUE,
  token_expiration TEXT
);
