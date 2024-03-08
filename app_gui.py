import customtkinter as tk
from tkinter import messagebox
from authentication import login, sign_up
from expenses_tracker import add_expense, list_expenses

tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

class App(tk.CTk):
    def __init__(self):
        tk.CTk.__init__(self)
        self.title("Expense Tracker")
        self.geometry('1000x600')
        self.resizable(width=False, height=False)

        self.container = tk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.current_username = None # Attribute to store the current username

        self.pages = {}
        for PageClass in (LoginPage, MainPage, SignUpPage, NewExpensePage, AllExpensesPage):
            page_name = PageClass.__name__
            page = PageClass(parent=self.container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

        if hasattr(page, 'on_page_show'):
            page.on_page_show()

class LoginPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Page title
        label = tk.CTkLabel(self, text="Login Page",font=('Roboto', 24, 'bold'))
        label.pack(pady=40, padx=10)

        #Username entry
        self.username = tk.CTkEntry(self, placeholder_text='Username', width=250)
        self.username.pack(pady=12, padx=10)

        #Password entry
        self.password = tk.CTkEntry(self, placeholder_text='Password', show='*', width=250)
        self.password.pack(pady=12, padx=10)

        #Frame to keep login and signup buttons on the same line
        frame_buttons = tk.CTkFrame(self, fg_color='transparent')
        frame_buttons.pack(pady=12)

        #Login button
        login_button=tk.CTkButton(master=frame_buttons, text='Login', command=self.login, width=100)
        login_button.pack(padx=25,side='left')

        #Sign up button
        signin_button=tk.CTkButton(master=frame_buttons, text='Sign Up', command=self.sign_up, width=100)
        signin_button.pack(padx=25,side='left')

    def login(self):
        # Logic to check login credentials
        # If login is successful, move to main page
        username=self.username.get()
        password=self.password.get()
        login_success = login(username,password)
        if login_success:
            # Store the current username
            self.controller.current_username = username
            # Login successful, navigate to the main page
            self.controller.show_page("MainPage")
        else:
            # Login unsuccessful, show error message
            messagebox.showerror("Login Failed", "Wrong username or password")

    def sign_up(self):
        self.controller.show_page("SignUpPage")

class SignUpPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Page title
        label = tk.CTkLabel(self, text="Create New Account",font=('Roboto', 24, 'bold'))
        label.pack(pady=40, padx=10)

        #Username entry
        self.username = tk.CTkEntry(self, placeholder_text='Username', width=250)
        self.username.pack(pady=12, padx=10)

        #Password entry
        self.password = tk.CTkEntry(self, placeholder_text='Password', show='*', width=250)
        self.password.pack(pady=12, padx=10)

        #Frame to keep back and create account buttons on the same line
        frame_buttons = tk.CTkFrame(self, fg_color='transparent')
        frame_buttons.pack(pady=12)

        #Back button
        back_button=tk.CTkButton(master=frame_buttons, text='Back', command=self.back, width=100)
        back_button.pack(padx=25,side='left')

        #Create account button
        create_button=tk.CTkButton(master=frame_buttons, text='Create Account', command=self.create, width=100)
        create_button.pack(padx=25,side='left')

    def back(self):
        self.controller.show_page("LoginPage")

    def create(self):
        username=str(self.username.get())
        password=str(self.password.get())
        sign_up_success = sign_up(username,password)
        if sign_up_success:
            # Store the current username
            self.controller.current_username = username
            # Sign up successfull, navigate to the main page
            messagebox.showinfo('Sign Up', 'Successfully created new account')
            self.controller.show_page("MainPage")
        else:
            # Sign up unsuccessfull, new username
            messagebox.showerror("Sign Up Failed", "Already existing username")

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

        new_expense_button = tk.CTkButton(lower_row, text='new expense',anchor='nw',font=('Roboto', 24, 'bold'), width=230, height=150, corner_radius=7, command=self.add_new_expense_button)
        new_expense_button.pack(padx=40, pady=0, side='left')

        all_expenses_button = tk.CTkButton(lower_row, text='expense list',anchor='nw',font=('Roboto', 24, 'bold'), width=230, height=150, corner_radius=7, command=self.all_expenses_button)
        all_expenses_button.pack(padx=40, pady=0, side='left')

        configure_button = tk.CTkButton(lower_row, text='configure',anchor='nw',font=('Roboto', 24, 'bold'), width=230, height=150, corner_radius=7)
        configure_button.pack(padx=40, pady=0, side='left')

    #Logout function
    def logout(self):
        # Logic to logout
        # For simplicity, let's just go back to login page
        result = messagebox.askyesno(title='Logout',message='Are you sure you want to logout?')
        if result:
            # Update the current username
            self.controller.current_username = None
            self.controller.show_page("LoginPage")
        else:
            pass
        
    def add_new_expense_button(self):
        self.controller.show_page("NewExpensePage")

    def all_expenses_button(self):
        self.controller.show_page("AllExpensesPage")

class NewExpensePage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Header
        header = tk.CTkFrame(self, height=50)
        header.pack(anchor='n', fill='x')

        page_title = tk.CTkLabel(header, text="Add new expense",font=('Roboto', 24, 'bold'))
        page_title.pack(pady=40, padx=30, side='left')

        #Back button
        back_button = tk.CTkButton(header, text="Back", fg_color='transparent',bg_color='transparent', command=self.back, width=30)
        back_button.pack(pady=40, padx=20, side='right')

        #Expense description
        self.description = tk.CTkEntry(self, placeholder_text='Description', width=250)
        self.description.pack(pady=12, padx=10)

        #Expense amount
        self.amount = tk.CTkEntry(self, placeholder_text='Amount', width=250)
        self.amount.pack(pady=12, padx=10)

        #Category options
        self.options = tk.CTkOptionMenu(self,values=['Food','Fun','Work','House'], width=250, fg_color='#343638', button_color='#343638', button_hover_color='#565B5E')
        self.options.pack(pady=12,padx=10)

        #Add expense button
        add = tk.CTkButton(self, text='Add Expense', command=self.add_expense)
        add.pack(pady=12,padx=10)

    def back(self):
        self.controller.show_page("MainPage")

    def add_expense(self):
        username = self.controller.current_username
        description = str(self.description.get())
        amount = float(self.amount.get())
        category = str(self.options.get())

        add_expense(username,amount,description,category)

class AllExpensesPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        # Header
        header = tk.CTkFrame(self, height=50)
        header.pack(anchor='n', fill='x')

        page_title = tk.CTkLabel(header, text="All expenses", font=('Roboto', 24, 'bold'))
        page_title.pack(pady=40, padx=30, side='left')

        # Back button
        back_button = tk.CTkButton(header, text="Back", fg_color='transparent', bg_color='transparent',
                                    command=self.back, width=30)
        back_button.pack(pady=40, padx=20, side='right')

        self.text = tk.CTkTextbox(self, width=300, height=450, font=('Roboto', 16))
        self.text.pack(pady=30, padx=10, anchor='center')

    def update_expenses_text(self):
        # Clear the text widget
        self.text.delete(1.0, tk.END)

        # Get expenses text after updating username
        expenses_text = list_expenses(self.controller.current_username)

        # Insert the updated expenses text
        self.text.insert(tk.END, expenses_text)

    def back(self):
        self.controller.show_page("MainPage")

    def on_page_show(self):
        # Call this method whenever this page is shown
        self.update_expenses_text()

if __name__ == "__main__":
    app = App()
    app.mainloop()