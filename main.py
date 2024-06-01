# Importaciones
from tkinter import *;
from tkinter import messagebox;
from random import randint
from pyperclip import copy
import json


# Variables
ruta_file = 'C:/Users/PC/Desktop/passwords_program.json'
email = 'correo@domain.microsoft'



# ---------------------------- SEARCH ACCOUNT ------------------------------- #
def search_account():
    website = input_website.get()

    if website == '':
        messagebox.showwarning(title='Oops', message='El campo website no puede ir vacio!')
        return

    try:
        with open( ruta_file, 'r' ) as information:
            data = json.load( information ) # Leemos los datos
            data_website = data[website]
            password = data_website['Password']
            email = data_website['Email']
    except FileNotFoundError:
        messagebox.showwarning(title='Oops', message='Aún no tienes ninguna contraseña creada')
    except KeyError:
        messagebox.showwarning(title='Oops', message=f'Error 404\nWebsite: "{website}" not found :(')
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(title='Oops', message=f'Parece que el archivo esta vacio')
    else:
        messagebox.showinfo( title='Data', message=f'⬇️⬇️ Info Account ⬇️⬇️\nEmail: {email}\nPassword: {password}' )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [ random.choice(letters) for _ in range(randint(8, 10))  ]
    password_list += [ random.choice(symbols) for _ in range(randint(2, 4))  ]
    password_list += [ random.choice(numbers) for _ in range(randint(2, 4))  ]

    random.shuffle(password_list)

    password = ''.join( password_list ); # separa por lo que le escribas en las comillas
    input_password.delete( 0, END )
    copy( password )
    input_password.insert( 0, password ) # agregamos el texto en el input

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = input_password.get()
    email = input_email.get()
    website = input_website.get()
    new_data = {
        website: {
        'Password': password,
        'Email': email,
        }
    }

    if password == '' or email == '' or website == '':
        messagebox.showinfo( title='Oops', message='Todos los campos son requeridos' )
        return

    try:
        with open( ruta_file, 'r' ) as information:
            data = json.load( information ) # Leemos los datos
            data.update(new_data) # actualizamos el valor anterior con new_data
    except:
        with open( ruta_file, 'w' ) as data_file:
            json.dump( new_data, data_file, indent=4 ) # guardamos el nuevo valor actualizado
            input_password.delete( 0, END )
            input_website.delete( 0, END )
    else:
        with open( ruta_file, 'w' ) as data_file:
            json.dump( data, data_file, indent=4 ) # guardamos el nuevo valor actualizado
    finally:
        input_password.delete( 0, END )
        input_website.delete( 0, END )

# ---------------------------- UI SETUP ------------------------------- #


# Instancias
window = Tk();
text_website = Label(text='Webiste');
text_email_username= Label(text='Email/Username');
text_password = Label(text='Password');

input_website = Entry( );
input_email = Entry( width=35 );
input_password = Entry( width=21 );

btn_generate_password = Button( text='Generate Password', command=generate_password );
btn_add = Button( width=36, text='Add', command=save_password );
btn_search = Button( text='Search', command=search_account );

image = PhotoImage(file='./logo.png');

canvas = Canvas(width=200, height=200);

# Methods
window.title('Password Manager');
window.config( padx=20, pady=20 )

canvas.create_image(100, 100, image=image);
canvas.grid( column=1, row=0 );

text_website.grid(column=0, row=1);
input_website.grid( column=1, row=1 );
input_website.focus();

text_email_username.grid( column=0, row=2 )
input_email.grid( column=1, row=2, columnspan=2 )
input_email.insert( 0, email )

text_password.grid( column=0, row=3 )
input_password.grid(column=1, row=3)
btn_generate_password.grid(column=2, row=3)

btn_add.grid( row=4, column=1, columnspan=2 )

btn_search.grid( column=2, row=1 )

window.mainloop();