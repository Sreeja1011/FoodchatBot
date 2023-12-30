import mysql.connector
global cnx
cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sreeja@1011",
        database='pandeyji_eatery'
    )

def insert_order_item(food_item,quantity,order_id):
    try:
        cursor = cnx.cursor()
        cursor.callproc('insert_order_item',(food_item,quantity,order_id))
        cnx.commit()

        cursor.close()

        print("Order Item inserted successfully")
        return 1
    except mysql.connector.Error as err:
        print(f"Error inserting order item:{err}")
        cnx.rollback()

        return -1
    except Exception as e:
        print(f"Error occured:{e}")
        cnx.rollback()
        return -1

def get_total_order_price(order_id):
    cursor = cnx.cursor()
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    result = cursor.fetchone()[0]
    cursor.close()
    return result

def insert_order_tracking(order_id,status):
    cursor = cnx.cursor()

    insert_query = "Insert into order_tracking (order_id,status) values (%s,%s)"
    cursor.execute(insert_query,(order_id,status))

    cnx.commit()

    cursor.close()
def get_next_order_id():
    cursor=cnx.cursor()
    query="SELECT max(order_id) from orders"
    cursor.execute(query)

    result = cursor.fetchone()[0]

    cursor.close()

    if result is None:
        return 1
    else:
        return result+1
def get_order_status(order_id: int):

    cursor=cnx.cursor()
    query=("SELECT status FROM order_tracking WHERE order_id=%s")

    cursor.execute(query,(order_id,))
    result=cursor.fetchone()
    cursor.close()

    if result is not None:
        return result[0]
    else:
        return None