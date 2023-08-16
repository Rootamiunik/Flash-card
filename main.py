from tkinter import *
from tkinter import messagebox
import pandas
import random
from threading import Timer

#!----------------------Global variable---------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

#!--------------------------func-----------------------#
def filp():
    global random_frech_word_key
    try:
        Label( text=f'𝒆𝒏𝒈𝒍𝒊𝒔𝒉\n\n\n{data[random_frech_word_key]}',font=(FONT_NAME,18), image=back_image, compound='center',background=BACKGROUND_COLOR).grid(row=0,column=2)
    except KeyError:
        pass
    finally:
        random_frech_word_key = random.choice(list_of_france)

def run():
    Label( text=f'𝒇𝒓𝒆𝒏𝒄𝒉\n\n\n{random_frech_word_key}',font=(FONT_NAME,18,'bold'), image=front_image, compound='center',background=BACKGROUND_COLOR).grid(row=0,column=2)
    Timer(3,filp).start()
    
def right_tick():
    global random_frech_word_key
    try:
        del data[random_frech_word_key]
        list_of_france.remove(random_frech_word_key)

        
        random_frech_word_key =random.choice(list_of_france)
    except IndexError:
        messagebox.showinfo("Completed","You now know all words.")
    else:
        run()

#!-------------------------Main---------------------------------#
try:
    raw_data = pandas.read_csv("french_words.csv")
except FileNotFoundError:
    messagebox.showerror('Error',"No file have been found.\nInsert a file and try agian.")
else:
    #?Creating required data
    data = {row.French:row.English for (index,row) in raw_data.iterrows()} 
    list_of_france = [key for key,value in data.items()]
    random_frech_word_key = random.choice(list_of_france)
    #?--------------------------------------------UI-----------------------------#
    window = Tk()
    window.config(bg=BACKGROUND_COLOR,padx=40,pady=20)

    #?Front back image
    front_image = PhotoImage(file='card_front.png')
    back_image = PhotoImage(file='card_back.png')

    #?right button..
    right_image = PhotoImage(file='right.png')
    right = Button(image=right_image,highlightthickness=0,command=right_tick)
    right.grid(row=1,column=3)

    #?wrong button
    wrong_image = PhotoImage(file='wrong.png')
    wrong = Button(image=wrong_image,command=run)
    wrong.grid(row=1,column=1)
    run()
    window.mainloop()

    #?Saving data
    new_data = {'French':[value for key,value in data.items()],
                          'English':[value for key,value in data.items()]}
    new_data_frame = pandas.DataFrame(new_data).to_csv('french_words.csv',index=False)

