import tkinter as tk

window = tk.Tk()

# Initialize the main window
window.geometry("600x400")
window.title("Naija Dictionary")
# Set the background color to bl
window.configure(bg="blue")

# Dictionaries for different Nigerian languages
dictionaries = {
 "Michika": {
        'hwada': "tree", 'tsatsa': "stone", 'nanga': "house", 'fako': "child", 'bwala': "food",
        'challa': "water", 'kaka': "firewood", 'sikala': "day", 'suwi': "night", 'kwang': "goat",
        'mbala': "road", 'wila': "fish", 'nyanya': "mother", 'baba': "father", 'jaka': "donkey",
        'lumba': "rice", 'dala': "friend", 'hwapa': "work", 'yawi': "brother", 'mwanwa': "sister"
    },
    "Hausa": {
        'kujera': "chair", 'mangwaro': "mango", 'gida': "house", 'yaro': "child", 'abunci': "food",
        'ruwa': "water", 'kaka': "grandfather", 'safe': "day", 'dare': "night", 'akuya': "goat",
        'hanya': "road", 'kifi': "fish", 'mama': "mother", 'baba': "father", 'jaki': "donkey",
        'cinkafa': "rice", 'aboki': "friend", 'aiki': "work", 'dadi': "enjoyment", 'Yesu': "Jesus"
    },
    "Igbo": {
        'aku': "wealth", 'ije': "journey", 'mmanu': "oil", 'mkpuruosisi': "fruit", 'uburu': "brain",
        'nna': "Father", 'ihe': "thing", 'igba oso': "running", 'ndi': "people", 'onumu': "boundary",
        'akwukwo': "book", 'mkpuru nmadu': "offspring", 'Ebe mmiri': "river bank", 'Mmadụbịa': "settlers", 'oge': "time",
        'ebe': "place", 'akwa': "great", 'Chi': "God", 'otu': "one", 'ike': "can"
    },
    "Yoruba": {
        'ile': "house", 'omo': "child", 'ounje': "food", 'omi': "water", 'ina': "fire",
        'ojo': "day", 'orun': "sun", 'osu': "moon", 'awon': "people", 'iwa': "character",
        'ade': "crown", 'oju': "eye", 'ese': "foot", 'ori': "head", 'ohun': "voice",
        'oba': "king", 'aya': "wife", 'oko': "husband", 'oruko': "name", 'ifa': "divination"
    },
    "Igala": {
        'ara': "boy", 'ulo': "house", 'ẹkpola': "stone", 'ọmọ': "child", 'anọ': "food",
        'omi': "water", 'ọkọ': "boat", 'anọki': "river", 'ocho': "day", 'ọjọ': "night",
        'ikpakpa': "medicine", 'ehi': "market", 'ohimi': "chief", 'ami': "friend", 'onuwe': "garden",
        'eka': "clan", 'lọjọ': "hill", 'ojiji': "shadow", 'ẹnyọ': "hill", 'abọ': "pot"
    },
}

# Variables
selected_language = tk.StringVar(value="Select a Language")
result = tk.StringVar()

def show_search_ui():
    if selected_language.get() == "Select a Language":
        result.set("Please select a language first.")
        return
    search_frame.pack(pady=20)
    # Set search frame background to white
    search_frame.config(bg="white")
def search():
    word = entry_text.get().lower()
    if word in dictionaries[selected_language.get()]:
        result.set(dictionaries[selected_language.get()][word])
    else:
        result.set("Not found")

tk.Label(window, text="Select a Language:", font=("Arial", 14), bg="blue", fg="white").pack(pady=10)
language_menu = tk.OptionMenu(window, selected_language, *dictionaries.keys(), command=lambda _: show_search_ui())
language_menu.config(bg="blue", fg="black")
language_menu.pack()

search_frame = tk.Frame(window, bg="blue")

entry_text = tk.Entry(search_frame, font=("Arial", 12), bg="black", fg="white")
entry_text.pack(pady=5)

search_btn = tk.Button(search_frame, text="Search", font=("Arial", 12), command=search, bg="blue", fg="black")
search_btn.pack(pady=5)

result_label = tk.Label(search_frame, textvariable=result, font=("Arial", 12), bg="white", fg="black")
result_label.pack(pady=10)

window.mainloop()
