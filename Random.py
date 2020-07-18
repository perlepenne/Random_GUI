from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    PhotoImage,
    IntVar,
    Canvas,
    StringVar,
    BooleanVar,
    Scrollbar,
    Text,
    Scrollbar,
    Listbox,
)
from random import randint, choice, shuffle
import os


def sidebar():

    random_number_button = Button(
        root,
        bg="#091f36",
        activebackground="#091f36",
        text="Random Number",
        command=lambda: random_number_generator(),
        borderwidth=0,
        fg="#b3d7da",
        font=("Berlin Sans FB", 13, "italic"),
    )
    random_choice_button = Button(
        root,
        bg="#091f36",
        activebackground="#091f36",
        text="Random Choice",
        command=lambda: random_choice(),
        borderwidth=0,
        fg="#b3d7da",
        font=("Berlin Sans FB", 13, "italic"),
    )

    root.bind("<Control_L>n", lambda event: random_number_generator())
    root.bind("<Control_L>c", lambda event: random_choice())
    sidebar_canva.create_window((70, 30), window=random_number_button)
    sidebar_canva.create_window((70, 70), window=random_choice_button)


def random_number_generator():
    main_canva.delete("all")
    on_start = BooleanVar()
    on_start.set(True)
    previous = Listbox(
        root,
        bd=0,
        highlightthickness=0,
        bg="#4f5f76",
        width=15,
        height=23,
        font=("Berlin Sans FB", 13),
    )
    previous.config(yscrollcommand=scrolly.set)
    previous.configure(justify="left")
    scrolly.config(command=previous.yview)
    previous.config(xscrollcommand=scrollx.set)
    scrollx.config(command=previous.xview)
    previous.config(
        activestyle="none",
        selectbackground="#4f5f76",
        selectforeground="black",
        highlightthickness=0,
    )
    ind = IntVar()
    ind.set(1)

    # Functions

    def esc():
        root.focus()
        on_start.set(False)

    def generate_number(start, end):
        try:
            number = str(randint(int(start), int(end)))
        except ValueError:
            number = "/"

        label = Label(root, text=number, bg="#4f5f76", font=("Berlin Sans FB", 13),)

        main_canva.create_window((170, 400), anchor="center", window=label)
        previous.insert(ind.get(), number)
        previous.yview("end")
        ind.set(ind.get() + 1)

    def switch():
        if on_start.get():
            end_entry.focus()
            on_start.set(False)
        else:
            start_entry.focus()
            on_start.set(True)

    entries = PhotoImage(file="entries.png")
    start_img = Label(root, image=entries, bg="#4f5f76")
    end_img = Label(root, image=entries, bg="#4f5f76")
    start_img.image = entries
    end_img.image = entries
    start_label = Label(
        root, text="Starting number:", bg="#4f5f76", font=("Berlin Sans FB", 13)
    )
    start_entry = Entry(
        root, width=5, bg="#4f5f76", borderwidth=0, font=("Berlin Sans FB", 13)
    )
    main_canva.create_window((100, 100), window=start_label)
    main_canva.create_window((200, 100), window=start_entry)
    main_canva.create_window((200, 100), window=start_img)

    start_entry.focus()

    end_label = Label(
        root, text="Ending number:", bg="#4f5f76", font=("Berlin Sans FB", 13)
    )
    end_entry = Entry(
        root, width=5, bg="#4f5f76", borderwidth=0, font=("Berlin Sans FB", 13)
    )

    main_canva.create_window((100, 175), window=end_label)
    main_canva.create_window((200, 175), window=end_entry)
    main_canva.create_window((200, 175), window=end_img)

    main_canva.create_window((310, 12), anchor="nw", window=previous)

    extract_img = PhotoImage(
        file="extract.png"
    )
    button_generate = Button(
        root,
        text="Generate Number",
        image=extract_img,
        compound="center",
        command=lambda: generate_number(start_entry.get(), end_entry.get()),
        bg="#4f5f76",
        activebackground="#4f5f76",
        font=("Berlin Sans FB", 13),
        border=0,
    )
    button_generate.image = extract_img

    main_canva.create_window((175, 250), window=button_generate)

    root.bind("<Down>", lambda event: switch())
    root.bind("<Up>", lambda event: switch())
    root.bind(
        "<Return>", lambda event: generate_number(start_entry.get(), end_entry.get())
    )
    root.bind("<Escape>", lambda event: esc())
    start_entry.bind(
        "<Control_L><BackSpace>", lambda event: start_entry.delete(0, "end")
    )
    start_entry.bind(
        "<Control_R><BackSpace>", lambda event: start_entry.delete(0, "end")
    )
    end_entry.bind("<Control_L><BackSpace>", lambda event: end_entry.delete(0, "end"))
    end_entry.bind("<Control_R><BackSpace>", lambda event: end_entry.delete(0, "end"))


def random_choice():
    main_canva.delete("all")

    def get_element():
        if had_shuffle.get() == True:
            previous.delete(0, "end")
            had_shuffle.set(False)
        list_.append(word_entry.get())
        previous.insert(ind.get(), word_entry.get())
        ind.set(ind.get() + 1)

        word_entry.delete(0, "end")
        main_canva.create_window((310, 12), anchor="nw", window=previous)
        previous.yview("end")

    def extract_element():
        if had_shuffle.get() == True:
            previous.delete(0, "end")
            had_shuffle.set(False)
        try:
            word = choice(list_)
        except IndexError:
            word = "/"
        list_.clear()
        previous.delete(0, "end")

        previous.insert(1, word)
        had_shuffle.set(True)

    def shuffle_list():
        previous.delete(0, "end")
        shuffle(list_)
        copy = list_.copy()
        list_.clear()
        for index in range(len(copy)):
            previous.insert(index, copy[index])
        main_canva.create_window((310, 12), anchor="nw", window=previous)
        had_shuffle.set(True)

    list_ = []
    had_shuffle = BooleanVar()
    had_shuffle.set(False)
    previous = Listbox(
        root,
        bd=0,
        highlightthickness=0,
        bg="#4f5f76",
        height=23,
        width=15,
        font=("Berlin Sans FB", 13),
    )
    ind = IntVar()
    ind.set(1)
    previous.config(yscrollcommand=scrolly.set)
    previous.configure(justify="left")
    scrolly.config(command=previous.yview)
    previous.config(xscrollcommand=scrollx.set)
    scrollx.config(command=previous.xview)
    previous.config(
        activestyle="none",
        selectbackground="#4f5f76",
        selectforeground="black",
        highlightthickness=0,
    )

    word_entry_img = PhotoImage(
        file="word_entry.png"
    )
    word_entry_label = Label(root, image=word_entry_img, bg="#4f5f76")
    word_entry_label.image = word_entry_img
    word_entry = Entry(
        root, width=22, font=("Berlin Sans FB", 13), bg="#4f5f76", borderwidth=0
    )
    word_entry.focus()

    extract_img = PhotoImage(
        file="extract.png"
    )
    go_button_img = PhotoImage(
        file="confirm_button.png"
    )
    go_button = Button(
        root,
        text="Confirm",
        image=go_button_img,
        compound="center",
        command=get_element,
        bg="#4f5f76",
        border=0,
        activebackground="#4f5f76",
        font=("Berlin Sans FB", 13),
    )
    go_button.image = go_button_img

    extract = Button(
        root,
        text="Extract Element",
        command=extract_element,
        bg="#4f5f76",
        compound="center",
        border=0,
        image=extract_img,
        activebackground="#4f5f76",
        font=("Berlin Sans FB", 13),
    )
    extract.image = extract_img
    extract_img2 = PhotoImage(
        file="extract2.png"
    )
    shuffle_list_button = Button(
        root,
        text="Shuffle List",
        command=shuffle_list,
        bg="#4f5f76",
        image=extract_img2,
        border=0,
        compound="center",
        activebackground="#4f5f76",
        font=("Berlin Sans FB", 13),
    )
    shuffle_list_button.image = extract_img2

    main_canva.create_window((170, 50), anchor="center", window=word_entry)
    main_canva.create_window((170, 50), anchor="center", window=word_entry_label)
    main_canva.create_window((170, 150), anchor="center", window=go_button)
    main_canva.create_window((170, 250), anchor="center", window=extract)
    main_canva.create_window((170, 350), anchor="center", window=shuffle_list_button)

    root.bind("<Return>", lambda event: get_element())

    root.bind("<Control_L>e", lambda event: extract_element())
    root.bind("<Control_L>s", lambda event: shuffle_list())

    root.bind("<Control_R>e", lambda event: extract_element())
    root.bind("<Control_R>s", lambda event: shuffle_list())
    word_entry.bind("<Control_L><BackSpace>", lambda event: word_entry.delete(0, "end"))


root = Tk()
sidebar_canva = Canvas(
    root, width=155, height=500, bg="#091f36", bd=0, highlightthickness=0
)
sidebar_canva.create_line((155, 0), (155, 500), width=5, fill="white")
sidebar_canva.place(x=0, y=0, anchor="nw")

main_canva = Canvas(
    root, width=500, height=500, bg="#4f5f76", bd=0, highlightthickness=0
)
main_canva.place(x=155, y=0, anchor="nw")

root.iconbitmap("icon.ico")
root.geometry("650x500+216-116")

root.title("Random Choices")
root.resizable(False, False)

scrolly = Scrollbar(root, orient="vertical")
scrolly.pack(side="right", fill="y")

scrollx = Scrollbar(root, orient="horizontal")
scrollx.pack(side="bottom", fill="x")

sidebar()
root.mainloop()
