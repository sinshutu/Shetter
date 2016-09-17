import sqlite3
import sys

if __name__ == "__main__":
    db_name = "shetter.db"
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()

    if len(sys.argv) == 2:
        date = sys.argv[1]
        start_hour = None
        end_hour = None
        sql = 'select id from schedules where date = {0};'.format(date, start_hour, end_hour)
    elif len(sys.argv) == 4:
        date = sys.argv[1]
        start_hour = sys.argv[2]
        end_hour = sys.argv[3]
        sql = 'select id from schedules where date = {0} and ({1} >= start_hour and {2} <= end_hour);'.format(date, start_hour, end_hour)

    cur.execute(sql)
    result_ids = [record[0] for record in cur.fetchall()]

    sql = 'select * from profile where id in ('
    place_holder = '?,'*len(result_ids)
    sql = sql + place_holder[:-1] + ')'

    cur.execute(sql, result_ids)
    profiles = [record for record in cur.fetchall()]
    for record in profiles:
        print(record)

    connection.close()
