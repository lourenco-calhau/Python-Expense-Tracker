import customtkinter as tk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

class SampleApp(tk.CTk):
    def __init__(self):
        tk.CTk.__init__(self)
        self.title("Expense Tracker")
        self.geometry('1000x600')
        self.resizable(width=False, height=False)

        self.container = tk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (LoginPage, MainPage):
            page_name = PageClass.__name__
            page = PageClass(parent=self.container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

class LoginPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Page title
        label = tk.CTkLabel(self, text="Login Page",font=('Roboto', 24, 'bold'))
        label.pack(pady=40, padx=10)

        #Username entry
        username = tk.CTkEntry(self, placeholder_text='Username', width=250)
        username.pack(pady=12, padx=10)

        #Password entry
        password = tk.CTkEntry(self, placeholder_text='Password', show='*', width=250)
        password.pack(pady=12, padx=10)

        #Frame to keep login and signup buttons on the same line
        frame_buttons = tk.CTkFrame(self, fg_color='transparent')
        frame_buttons.pack(pady=12)

        #Login button
        login_button=tk.CTkButton(master=frame_buttons, text='Login', command=self.login, width=100)
        login_button.pack(padx=25,side='left')

        #Sign up button
        signin_button=tk.CTkButton(master=frame_buttons, text='Sign Up', command=self.login, width=100)
        signin_button.pack(padx=25,side='left')

    def login(self):
        # Logic to check login credentials
        # If login is successful, move to main page
        self.controller.show_page("MainPage")

class MainPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Header
        header = tk.CTkFrame(self, height=50)
        header.pack(anchor='n', fill='x')

        page_title = tk.CTkLabel(header, text="Main Page",font=('Roboto', 24, 'bold'))
        page_title.pack(pady=40, padx=30, side='left')

        #Logout button
        logout_button = tk.CTkButton(header, text="Logout", fg_color='transparent',bg_color='transparent', command=self.logout, width=30)
        logout_button.pack(pady=40, padx=20, side='right')

        #Upper row of the main page
        upper_row = tk.CTkFrame(self,fg_color='transparent')
        upper_row.pack(pady=20)

        balance_label = tk.CTkLabel(upper_row, text='balance',anchor='nw',font=('Roboto', 24, 'bold'), fg_color='grey', width=230, height=150, corner_radius=7)
        balance_label.pack(padx=40, pady=40, side='left')

        last_expense_label = tk.CTkLabel(upper_row, text='last expense',anchor='nw',font=('Roboto', 24, 'bold'), fg_color='grey', width=230, height=150, corner_radius=7)
        last_expense_label.pack(padx=40, pady=40, side='left')

        graph_label = tk.CTkLabel(upper_row, text='last month',anchor='nw',font=('Roboto', 24, 'bold'), fg_color='grey', width=230, height=150, corner_radius=7)
        graph_label.pack(padx=40, pady=40, side='left')


        #Lower row of the main page
        lower_row = tk.CTkFrame(self,fg_color='transparent')
        lower_row.pack(pady=20)

        new_expense_button = tk.CTkButton(lower_row, text='new expense',anchor='nw',font=('Roboto', 24, 'bold'), width=230, height=150, corner_radius=7)
        new_expense_button.pack(padx=40, pady=0, side='left')

        all_expenses_button = tk.CTkButton(lower_row, text='expense list',anchor='nw',font=('Roboto', 24, 'bold'), width=230, height=150, corner_radius=7)
        all_expenses_button.pack(padx=40, pady=0, side='left')

        configure_button = tk.CTkButton(lower_row, text='configure',anchor='nw',font=('Roboto', 24, 'bold'), width=230, height=150, corner_radius=7)
        configure_button.pack(padx=40, pady=0, side='left')

    def logout(self):
        # Logic to logout
        # For simplicity, let's just go back to login page
        self.controller.show_page("LoginPage")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()