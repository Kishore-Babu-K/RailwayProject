from sqlconnection import make_sql_connection

def Check_Avl_Price_Name(connection,data):
    cursor = connection.cursor()
    query = ("""select t.train_no,t.train_name, s.sleeper, p.sleeper_price,s.seating,p.seating_price,s.third_ac,
    p.third_ac_price,s.second_ac, p.second_ac_price, s.first_ac, p.first_ac_price from train_table t
    join price_table p on t.train_no = p.train_no
    join seatavl_table s on t.train_no = s.train_no
    where LOWER(t.train_name) = LOWER(%s)""")
    cursor.execute(query,(data["train_name"],))

    match_trains = []
    for (train_no, train_name,sleeper,sleeper_price,seating,seating_price,third_ac,third_ac_price,second_ac,second_ac_price,first_ac,first_ac_price) in cursor:
        match_trains.append({"train_no":train_no, "train_name":train_name, "sleeper":sleeper, "sleeper_price" : sleeper_price, "seating" : seating, "seating_price" : seating_price, "third_ac" :third_ac,"third_ac_price" : third_ac_price, "second_ac" : second_ac, "second_ac_price" : second_ac_price, "first_ac" : first_ac, "first_ac_price": first_ac_price })

    return match_trains

def Check_Avl_Price_No(connection,data):
    cursor = connection.cursor()
    query = ("""select t.train_no,t.train_name, s.sleeper, p.sleeper_price,s.seating,p.seating_price,s.third_ac,
    p.third_ac_price,s.second_ac, p.second_ac_price, s.first_ac, p.first_ac_price from train_table t
    join price_table p on t.train_no = p.train_no
    join seatavl_table s on t.train_no = s.train_no
    where t.train_no = %s""")
    cursor.execute(query,(data["train_no"],))

    match_trains = []
    for (train_no, train_name,sleeper,sleeper_price,seating,seating_price,third_ac,third_ac_price,second_ac,second_ac_price,first_ac,first_ac_price) in cursor:
        match_trains.append({"train_no":train_no, "train_name":train_name, "sleeper":sleeper, "sleeper_price" : sleeper_price, "seating" : seating, "seating_price" : seating_price, "third_ac" :third_ac,"third_ac_price" : third_ac_price, "second_ac" : second_ac, "second_ac_price" : second_ac_price, "first_ac" : first_ac, "first_ac_price": first_ac_price })

    return match_trains

if __name__ == "__main__":

    data = {"train_no" :"12793",}
    connection = make_sql_connection()
    print(Check_Avl_Price_No(connection,data))
    