from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km_value = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km_value}")


#create window

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#Label_miles
label = Label(text="Miles", font=("Arial", 10, "bold"))
label.grid(column=2,row=0)

#Label_is_equal
label_is_equal = Label(text="is equal to", font=("Arial", 10, "bold"))
label_is_equal.grid(column=0, row=1)

#Label_to_km
kilometer_result_label = Label(text="0", font=("Arial", 10, "bold"))
kilometer_result_label.grid(column=1, row=1)

#Label_km
label_km = Label(text="Km", font=("Arial", 10, "bold"))
label_km.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=2)

window.mainloop()