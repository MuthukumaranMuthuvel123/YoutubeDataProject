import mysql.connector

dataBase = mysql.connector.connect(
    host ="127.0.0.1",
    user="root",
    passwd="Sathu@12345",
    database = "projectyoutube"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table 
CHANNELDETAILS = """CREATE TABLE Channel (
                CHANNEL_ID VARCHAR(255) UNIQUE,
                CHANNEL_NAME VARCHAR(255),
                CHANNEL_TYPE VARCHAR(255),
                CHANNEL_DESCRIPTION TEXT,
                CHANNEL_VIEWS INT,
                CHANNEL_SUBCOUNT INT
                )"""

PLAYLIST = """CREATE TABLE Playlist (
    PLAYLIST_ID VARCHAR(255) UNIQUE,
    CHANNEL_ID VARCHAR(255),
    PLAYLIST_NAME VARCHAR(255)
)"""

COMMENT = """CREATE TABLE Comment(
    COMMENT_ID VARCHAR(255) UNIQUE,
    VIDEO_ID VARCHAR(255),
    COMMENT_TEXT TEXT,
    COMMENT_AUTHOR VARCHAR(255),
    COMMENT_PUB_DATE DATETIME
)"""

VIDEO = """CREATE TABLE Video(
    VIDEO_ID VARCHAR(255) UNIQUE,
    PLAYLIST_ID VARCHAR(255),
    VIDEO_NAME VARCHAR(255),
    VIDEO_DESC TEXT,
    PUB_DATE DATETIME,
    VIEW_COUNT INT,
    LIKE_COUNT INT,
    FAV_COUNT INT,
    COMMENT_COUNT INT,
    DURATION INT,
    THUMBNAIL VARCHAR(255),
    CAPTION_STATUS VARCHAR(255)
)"""
# table created
cursorObject.execute(CHANNELDETAILS) 
cursorObject.execute(PLAYLIST) 
cursorObject.execute(COMMENT) 
cursorObject.execute(VIDEO) 

#disconnecting from server
dataBase.close()