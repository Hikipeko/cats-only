PRAGMA foreign_keys = ON;

CREATE TABLE users(
    username VARCHAR(20) PRIMARY KEY,
    fullname VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    filename VARCHAR(64) NOT NULL,
    password VARCHAR(256) NOT NULL,
    created DATETIME DEFAULT (datetime('now')) -- 'localtime'
);

CREATE TABLE posts(
    postid INTEGER PRIMARY KEY AUTOINCREMENT,
    filename VARCHAR(64) NOT NULL,
    owner VARCHAR(20) REFERENCES users(username) ON DELETE CASCADE,
    created DATETIME DEFAULT (datetime('now'))
);

CREATE TABLE following(
    username1 VARCHAR(20) REFERENCES users(username) ON DELETE CASCADE,
    username2 VARCHAR(20) REFERENCES users(username) ON DELETE CASCADE,
    created DATETIME DEFAULT (datetime('now')),
    PRIMARY KEY (username1, username2)
);

CREATE TABLE comments(
    commentid INTEGER PRIMARY KEY AUTOINCREMENT,
    owner VARCHAR(20) REFERENCES users(username) ON DELETE CASCADE,
    postid INTEGER REFERENCES posts(postid) ON DELETE CASCADE,
    text VARCHAR(1024),
    created DATETIME DEFAULT (datetime('now'))
);

CREATE TABLE likes(
    likeid INTEGER PRIMARY KEY AUTOINCREMENT,
    owner VARCHAR(20) REFERENCES users(username) ON DELETE CASCADE,
    postid INTEGER REFERENCES posts(postid) ON DELETE CASCADE,
    created DATETIME DEFAULT (datetime('now'))
);