import tkinter

class mpgGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.top_frame2 = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text='Enter how many gallons your car holds:')
        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label2 = tkinter.Label(self.top_frame, text='Enter the distance you have traveled in miles:')
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='top')
        self.gallon_entry.pack(side='top')

        self.prompt_label2.pack(side='top')
        self.miles_entry.pack(side='top')

        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to miles per gallon:')
        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
#        self.top_frame2.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        gallons = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles/gallons
        self.value.set(mpg)

if __name__ == '__main__':
    mpg = mpgGUI()