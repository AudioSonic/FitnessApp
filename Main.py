import tkinter as tk
import mysql.connector

def connect_to_database():
    host = 'sql11.freesqldatabase.com'
    database = 'sql11665817'
    username = 'sql11665817'
    password = 'aYsmePsf1F'
    port = 3306

    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        print("Verbindung zur MySQL-Datenbank hergestellt.")
        return connection, cursor
    except Exception as e:
        print(f"Fehler bei der Verbindung zur MySQL-Datenbank: {str(e)}")
        return None, None

def insert_user_data(username, password, connection, cursor):
    try:
        # SQL-Befehl zum Einfügen von Daten
        sql_query = f"INSERT INTO Kunden (Benutzername, Passwort) VALUES ('{username}', '{password}')"
        cursor.execute(sql_query)
        connection.commit()
        print("Benutzerdaten erfolgreich in die Datenbank eingefuegt.")
    except Exception as e:
        print(f"Fehler beim Einfuegen von Benutzerdaten: {str(e)}")

def on_submit():
    # Funktion, die aufgerufen wird, wenn der "Submit"-Button geklickt wird
    username = entry_username.get()
    password = entry_password.get()

    # Hier kannst du weitere Aktionen durchführen, z.B. die Daten in die Datenbank speichern
    connection, cursor = connect_to_database()
    if connection and cursor:
        insert_user_data(username, password, connection, cursor)
        connection.close()
        print("Verbindung zur MySQL-Datenbank geschlossen.")
    else:
        print("Konnte keine Verbindung zur MySQL-Datenbank herstellen.")

# Rest des Codes bleibt unverändert
root = tk.Tk()
root.title("Login Form")
root.geometry("200x200")

label_username = tk.Label(root, text="Benutzername:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Passwort:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
