import mysql.connector
import youtubeData
channel_details=youtubeData.channel_data("UChPxqdfDbulLE9PyUqhijWw")
playlist_details=youtubeData.playlist_data(channel_details['channel_pid'])
dataBase = mysql.connector.connect(
    host ="127.0.0.1",
    user="root",
    passwd="Sathu@12345",
    database = "projectyoutube"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

'''
# creating table 
CHANNELDETAILS = """CREATE TABLE Channel (
                CHANNEL_ID VARCHAR(255),
                CHANNEL_NAME VARCHAR(255),
                CHANNEL_TYPE VARCHAR(255),
                CHANNEL_DESCRIPTION TEXT,
                CHANNEL_VIEWS INT,
                CHANNEL_SUBCOUNT INT
                )"""

# table created
cursorObject.execute(CHANNELDETAILS) 
'''
#inserting into table
def check_id_exists(id_to_check):
    # Check if the ID exists in the table
    cursorObject.execute("SELECT CHANNEL_ID FROM Channel WHERE CHANNEL_ID = %s", (id_to_check,))
    result = cursorObject.fetchone()
    # Return True if the ID exists, False otherwise
    return bool(result)

if not check_id_exists("UChPxqdfDbulLE9PyUqhijWw"):
    sql = "INSERT INTO Channel (CHANNEL_ID, CHANNEL_NAME, CHANNEL_TYPE, CHANNEL_DESCRIPTION, CHANNEL_VIEWS,CHANNEL_SUBCOUNT)\
    VALUES (%s, %s, %s, %s, %s,%s)"
    val = ("UChPxqdfDbulLE9PyUqhijWw", channel_details['channel_name'], channel_details['type'], channel_details['channel_des'], channel_details['channel_vc'],channel_details['channel_sub'])
    cursorObject.execute(sql, val)
    dataBase.commit()
else:
    print("ID already present")
sql2 = "INSERT INTO Playlist (PLAYLIST_ID, CHANNEL_ID, PLAYLIST_NAME)\
VALUES (%s, %s, %s)"
val2 = (playlist_details['playlist_id'], playlist_details['channel_id'], playlist_details['playlist_name'])

cursorObject.execute(sql2, val2)
dataBase.commit()

#disconnecting from server
dataBase.close()


