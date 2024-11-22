from sqlconnection import make_sql_connection

def allrec(connection):
    cursor = connection.cursor()
    cursor.execute("select * from User_table")
    c=cursor.fetchall()
    print(c)


def login_check(connection,data):
    cursor = connection.cursor()

    query = "select user_id, pass_word from User_table where user_id = %s"
    cursor.execute(query, (data["user_id"].lower(),))
    result = cursor.fetchone()
    
    if result:
        if data["pass_word"] == result[1]:
            print("Login successful")
            return True
        else:
            print("Invalid password")
            return False
    else:
        print("Username not found")
        return False
                
def Register_new(connection,data):
    cursor = connection.cursor()

    query = """insert into User_table (user_id, user_name, pass_word, role_of_user, phone_num, email) 
               values (%s, %s, %s, %s, %s, %s)"""
    
    values = (data["user_id"], data["user_name"], data["pass_word"], data["role_of_user"], data["phone_num"], data["email"])
    
    try:
        cursor.execute(query, values)
        connection.commit()
        print("user added successfully")
        return {"success": True}
        
    except Exception as e:
        print("Error in user_id")
        return {"success":False}





if __name__ == "__main__":
    connection = make_sql_connection()
    allrec(connection)
    data = {"user_id":"kish10","user_name":"Babu","pass_word":"kish1","role_of_user":"user","phone_num":91,"email":"babu@gmail.com"}
    #print(login_check(connection,data))
    Register_new(connection,data)

