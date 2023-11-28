import tkinter as tk
import pyodbc

def connect_to_database():
    server = 'DESKTOP-6AK4AG6'
    database = 'UserDB'
    username = 'SA'
    password = 'test'
    connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        print("Verbindung zur Datenbank hergestellt.")
        return connection, cursor
    except Exception as e:
        print(f"Fehler bei der Verbindung zur Datenbank: {str(e)}")
        return None, None
   
def insert_user_data(username, password, connection, cursor):
    try:
        # SQL-Befehl zum Einfügen von Daten
        sql_query = f"INSERT INTO Benutzer (Benutzername, Passwort) VALUES ('{username}', '{password}')"
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
        print("Verbindung zur Datenbank geschlossen.")
    else:
        print("Konnte keine Verbindung zur Datenbank herstellen.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Login Form")
root.geometry("200x200")

# Benutzername Label und Eingabefeld
label_username = tk.Label(root, text="Benutzername:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

# Passwort Label und Eingabefeld (Passwort-Feld für verdeckte Eingabe)
label_password = tk.Label(root, text="Passwort:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Submit-Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Tkinter-Schleife starten
root.mainloop()
