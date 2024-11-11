from sqlconnection import make_sql_connection

def allrec(connection):
    cursor = connection.cursor()
    cursor.execute("select * from Train_table")
    c=cursor.fetchall()
    print(c)

def Search_train_by_station(connection,data):
    cursor = connection.cursor()
    query = ("select train_no,train_name,arrival_time,departure_time,initial_avl, route from Train_table")
    cursor.execute(query)

    s_from = data["from"]
    s_to = data["to"]
    match_trains = []

    for (train_no, train_name, arrival_time,departure_time, initial_avl,route) in cursor:
        if s_from in route and s_to in route:
            from_ind = route.index(s_from)
            to_ind = route.index(s_to)

            if from_ind < to_ind:
                match_trains.append({"train_no":train_no, "train_name":train_name,"arrival_time":arrival_time, "departure_time":departure_time, "initial_avl": initial_avl })


    return match_trains

def Search_train_by_name(connection,data):
    cursor = connection.cursor()
    src = (data["search"],)
    if "all" in src:
        query=("select train_no,train_name,arrival_time,departure_time,initial_avl from Train_table")
        cursor.execute(query)
    else:
        query = ("select train_no,train_name,arrival_time,departure_time,initial_avl from Train_table where lower(train_name) = lower(%s)")
        cursor.execute(query,(data["search"],))

    match_trains = []
    for (train_no, train_name, arrival_time,departure_time, initial_avl) in cursor:
        match_trains.append({"train_no":train_no, "train_name":train_name,"arrival_time":arrival_time, "departure_time":departure_time, "initial_avl": initial_avl })
    
    return match_trains

def Train_schedule_by_name(connection,data):
    cursor = connection.cursor()
    query = ("select train_no,train_name,route,running_dates from Train_table where lower(train_name) = lower(%s)")
    cursor.execute(query,(data["train_name"],))

    match_trains = []
    for(train_no, train_name,route,running_dates) in cursor:
        match_trains.extend([train_no,train_name,route,running_dates])

    return match_trains

def Train_schedule_by_no(connection,data):
    cursor = connection.cursor()
    query = ("select train_no,train_name,route,running_dates from Train_table where train_no = %s")
    cursor.execute(query,(data["train_no"],))

    match_trains = []
    for(train_no, train_name,route,running_dates) in cursor:
        match_trains.extend([train_no,train_name,route,running_dates])

    return match_trains


if __name__ == "__main__":
    connection = make_sql_connection()


    sea = {"train_name":"Uzhavan",}
    sa = {"train_no":"12345",}
    # fe=[]
    # ku=[]
    fe = Train_schedule_by_name(connection,sea)
    ku =Train_schedule_by_no(connection,sa)
    print(fe)
    print(ku)

  