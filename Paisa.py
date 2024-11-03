import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
import datetime
import json
import os
from tkcalendar import DateEntry
import locale
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import tkinter.font as font

ICON_DATA = {
    'income': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAYRJREFUeF7tWcFxAjEQszqhE0IlQCUJlYR0QjqBSpY4E2ZuLrlZhbPZw5a/61vbWmmt8SF1PtD5+ZMAEAM6R0AS6JwAaoKSgCTQOQKSAEsAM3th5xaadwZwLpRrMg3FADPbpZTea29mlH8P4Fh7TQHAICwGSALfDXDLsKXgnA8Ap4L5/kxF9YDam4jMLwAi0V/C2mIAW4VoJ/hzFa9H+z3MdYsUA5bgA8wsO9HsSIdjM/emEACMBMSABTjBaAmEO8FQABiZ1J4jACJvgdrVZfKLAdEMKOkEh+blH3lfU0rjd8n9lzmi3g2nDFOEEToB2Nxob2bGSGDmnCOADNavIQAYZAs7QTHgGSVQ0gleALwNegD7vyHvYTVibH4zZJrg59Q/BqoHMDKpPUc+INoH1K6wl18MEAMCn8Q8ej4iLglIApJA3LP4IzTurdF9D/AAujf+NFb43gN63wkAD6HW42JA6xX2zicGeAi1HhcDWq+wdz4xwEOo9bgY0HqFvfOJAR5Crcev7f3eQT7T7cEAAAAASUVORK5CYII=',
    'expense': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAg5JREFUeF7tmuFtxCAMhc0k7Si9SdqbpO0kvU16m/Q2ceUqSCgl8YtFFAec38Dxvjzwg0uiwZ80uH4KAOGAwQnEEhjcALEJxhJAlgAzPxPRG9K2YZt7SunecLzqUJADmFnEf+09mdn415TSbe/fDAAI4XBALIG/TfAFcUvDNrIJPhqOZ98E957EkeNDm+CRE9z7twPA3oS9jw85IJJglMGIwnEWGP0wFEnQezmzzg8qg9bBz9AvAHh9SxK+tp4GLX0gBzROgg/tqouZ5ej9TUTwtRgzS3t5pA98jEYBtMwBcs6/LDmvEJ+bqBAm8fm+Qi5SYQiuAFTEqxBm4nN7GII3AB9E9L7gjn9OWBAv3WUJXJCl4AqAzJyZIQiKeIEF/aeAAmiZBGUTXJ2cBoGIXhfuKOXNw+IFOATgiFKpQKhNabN41wCA5VBCMIl3DwCEYBZ/CgAThB8ikn2o9txSSlfrMnW7B2RBK7t9qVkNS0uAXAMAxathac0dbgFsFG+G4BKAFnKmDAAnxlM5QBOfQ5QWlrQTZ4biygHMLF+h1D7FqZY6BYKcBdQ47A2AlDo515clb7XOL0CAS6MrAFPNLyFAIWcGARbvNghNN1CyHD4RGxeJ8WlrKHLnAGuis/YLAFZyvfQLB/TyJq06wgFWcr30Cwf08iatOsIBVnK99AsH9PImrTrCAVZyvfQb3gG/ucUBUNvsrw4AAAAASUVORK5CYII=',
    'budget': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAA2lJREFUeF7tmo2NFDEMhX2VAJUAlQCVAJUAldxRCVAJ7EMbKVhO/JvbDDuR0J24JBN/fnEczzzQnbeHO7efTgCnAu6cwLkFDiKAN0T08vrvBRH9uvz+lYh+Zte/swJg9DsiasZLtr7KQtgVwJeLYe8N3n0ioreGfsMuuwGAtx+dBqVsSA12LlTrHjEeMQDbINyqAECur6+rQLCKNACYNRjL5/58GfAp8rA2JgMARn8UFpVZDx8Lo2EkIv5vYeLM+v9OF5kAnoLhmseyIPoAB8//YBOmA2AEQGSfRkBw46TnQhUfIpP3YzwKgORxPK1uUmAbPfvZYoDmeXjj+zUpgQHpDI1RnsWbFASLAqT919YHqWIB+Lm6IdojM5ROmTAECwAkJlLACz80QaocggZg5H2L8ZAtPOZpFjWVQtAASDm5Nfuy5vM9IOT1lu2kQZDmEOfVAEjJh3WRKwEA2gwCV93wyJwBkORv9T4WsBqAB0IIAAgj4+ubZe+3/s8BwArhJgA8wW/WF0qEIxBU272A5xnadigDYN3/VcY3D/dKRPoLg3hrN1IA48d2CIAk4VsAwCWoT360S5Dr3jALglL+PaJf6XE+F49FWhz67wAASJM37huS/HtoZQCkiTT6K5VgnXspgJI7uNWSYL8yAMuqMEHDrMPKAOCBS+pwVkuC/UoB8CMIa0q/jQkaZh1WCkDKBW5xFHqMb0XbfkwoEWrHD68D7hQIcTwiVuGF6ewdYhjAzoFQuqyNlBIGgAl3jQNSgF4CYMc4MCvUcgjw/rdRpUmrCO0aB0byb2kyUmZcmtTyvAXAiLZlrDV6e/tJlerQTdVqxE5xIFuq+we2FYAkuVvlA1Kio9UIhgqzAih9qFfvrH+2VhlSQOQ4bF91ReydvRso3Y5WBcAIb4ksUhXGc2ZyLt3/eJgHgFQimxVIVgAolb8XgHQ9nnlrBQCvCtXt51GANw6sAFBen/ACkCTYPo7gtNtXnv3/S9kZ/yCyfRgleY/fTD2v6kQ1eAFoX4pokpOyNc+lhs+fLtJ6AYy2gWZ4+3s1gFD62y82AmD0xYgFQiWAtPwjp8DodmgxHn0qAaTlHwUgvXy0ArAEQetcUIDla5LpfJEtYF3gIfqdAA7hpoWLPBWwEO4hpj4VcAg3LVzkqYCFcA8x9R843+BBQeCBkwAAAABJRU5ErkJggg==',
    'close': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAmNJREFUeF7tmuFtxCAMhfEmvUnaTtJ2knaTXifpdZPbxO2TQEJRkrOLTeDgpPtHwP54tsEJhcF/NLj/YQKYChicwAyBwQUwk+AMAW0IMPNDfOZJ+6zz+CsRXbRrqBTAzHD6W7tIxfHXEMIXEX1I1xQD6MD53Oc3IjpLIGgAsGTCRsYgHE4SW0QAOtv95PezJCdIAbyGED4XRCGxHwnlCmMeQwiwUR0GJQDEceYNgJnXNkhk3wQg2Z0SwpL5S8eU2DcVIKFfQng5PzPjkHImIhxaTH4l9lVVADOjkiBhwXmUKRMIXQDInE+7bgaheQA7BykTCD0AwA0S0n9fCfpiCM0DgNPxGu0CoQYAXINfFruHa6fq/u0FwR2ASa2Kk3hA6AqARzh0B8AagjuAKFuPHiCqA3JL6jPm0SauDjUArF03LVPD1lwiCPcMAGBuQhgBAJobmyX3ngFg93edjwnVvSOEJOWRBGE/jsdbSfCm81UAeGU7ZsZLljWwop1PdrmHgAcAK+e7VICl81UAxPt88WUoGmsi+1yV7iFQssDCUHPnayng32UmS1QuzncBYENB6ZQnKnV7ibhEodW6wrEdnrfEVKWuewBRqngnAAhmzncRAotECAgXbTvtLhTgcaDqTgEeELpIgh6OV7sLlBD2dPxoAEN9ItP694FrQjtJ3j5LD0JoWOAou9a4qKFy9Rr097Wk5CHRoJ1SI1njiDGiT+RgmBhABmGrhXWEo8s11SdMFYAIAWGQ/i04nWzw/1i6JW+tbFErwGrhVuaZAFrZiaPsmAo4inwr604FtLITR9kxvAJ+AdsQ81AVqqGVAAAAAElFTkSuQmCC',
    'month': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAArJJREFUeF7tW4tNAzEMdScBJgEmASYBJqFMAkwCTAJ9UoMi17m8y6eX4xwJVbQ5x3n+5MXJ7WTjbbfx+YsD4B6wcQQ8BBo7wL2IXCuZD5VjvKjnvw//P1XK/Hu8tQe8iciNUq52jB8l711Ebh2ARgjUWker4R7gIbChHHApIviLGzK2/q42YSGs4oYk+GykAHw/u83NAZjco4hguRuxfR1XCHxSbQ4AWN60NahBztwJkwf3oDxiDgBWhj/z3OjhAMIV05sFYC3Wj+eM3JP1AhYAxLympBBOxxpjjYo+yE2agSIM9jmZNQBQA+QUaPS7ZSBKPweAtEAxwqT82m7F+rkHkNAXI0zKr+1WrJ97AAm9hTD56GLduq8Ci82MHNgB6E2ESEMs1q27B4AGj0SFdR2iOwDUAGeyvy+DxmaNMpDzANJFi12MlF/brVi/Xh4AhbJ78WMBFckrV7gI+/2UzGEAiCtHWCFQvU0pHZfYpkpYWqZV7xsGAFSN4opxamJWiS1VwtK1SACqD1yHBSB1kAmX/lSB/y8A0BObKkzG3jJ14htbN1XyHsYDYNRcwooNH9hbjlHmZA4FQO2SVvK8A+BM8PTcwqkwQ8Z6MEFcYMJFqY9DME9dZkJiQ+xeHM7xXifYYOgHmehnEathcoBWxCItIcmBB8SrQOowU5Mra2kdBoAeTDAGCuANzQRZD7CYYCocNahWchvGA0K84hZJ2AilSA6UvjuGwdSmKdxKwf4BOcDKK8MAUEJiWjzjADgRciJ0coOlOxNE4sqVslrENyMDCRKJN25NAVjjJammAFjrNmOZJfuAWebqDLNemlrTETnCk3qpgt0MBUtCqI61Ja1sjU1PHg/PBSAueelXY5YEAq/RhH1C1u1jRUsAWHKizcd2AJpDujKB7gErM1hzdTfvAb/bUfJBVCfg1wAAAABJRU5ErkJggg==',
    'refresh': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAxBJREFUeF7tmolt3DAQReVKEneSdOJUYruSJJXErsTpJN5vaAKGGV5zarEiICxsiSv+NxePvdtuvN3duP7tBHB6wI0TyA6Bzzv/31l2yAQA8d+3bcPn123bUiBkASDxXwoPSIGQAaAWT94PDwiHkAXg1+76deiHQ8gAANHwgkNAyAJwGAjZAMpKkBIOUQAg9OFS9j7tn7Nl3z0neANoZfxZAHjOFYIXAAvhJSSUx5cVarPPegCAq2OGZ9XcxGOA1gAgHABGDW5NV+95V/HWAFDXaWrLAXjeRf8obvaAuYu3BNATgtj9xix20sVbAYDVYX2uQXhpcXrmEOItACDbvzXEt1y4ByzE7cvxapNgK+5HQrhKMeozSqyi+xoALUvOCikhzPbhRD5d/olL1DQAOOsj4UHMbAMElEPpJIdyCSqMCIIGwB9GpcaSs9C4RAqI96tfoEmCXAwj2yPrRzRY+7F6kQi+1AO4MtYqeR5AzAwgBYDSR1vaJBAuGLWzy5Xf1fzzMW4pgDr+xTGocI86CYvGYAVARF8hHl25KrSsZ7nD7vr17C8yAXJVQByGVgAyPIBLxMt5SAIAtOsckAGAC4EwAHUVECUgZQ7gKtGyQZc77IM2oa8EYFKJpABufiLErQTFCxKBJ5gZQOoBdR2OLIOtZfhyAtTMBNGX5uMa8RCDa2Upy+Uf8Rg0HoD5OFZk0hUgWRIV5OckBO0mzH/RpgEgCN2/XWohMxBa4sXW14aAFEBLSO8MsLeRKop9Gny0B0i20HtHbaJNkNJykQBWxVOOaR2dmZTdKACz4iEaF56vt7xKw5mtPSIA9MTTjjDtLvXOFgmAKunVicsbQE+8JIma7zt6ArAU3zpglUD8p48ngN5P4WYHjhCB1aUHJ8P3eALAy1ch0I8mXidnhkOBowe8AcxAUNfykcje/QgAIwiuvwIbwYkCcFgIkQAOCSEaQA9Cxsaq+GhsFFqj+3V1SBGftRwmOAQBf4vO9keUZ+5nhEA5LkCIOlFmeWQDmDGS6zMnAFe8V/DlpwdcgZFch/gOIo+9QUkwgCwAAAAASUVORK5CYII=',
    'graph': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAkJJREFUeF7tmetNQzEMhd1NYBPYBCYBJgEmgVHYBHqkWrKiOHHSpDfBjtQ/vbdJzhc/0xM5Hyfn+ikAhAU4JxAu4NwAIgiGC4QLOCcQLvDPDOCOiH5aNP0nC3gnok8i+vYIAOKfiOjRIwAWj4N3B0CKdwcgFe8KQE780gCw4bfWFKVEc008Xr9vXeMWafDrHJkfLhtDkGrK0wmEkvjmAIi5ZwNg8awD4nshDBc/G0Aq/hoIU8TPBKCJ74EwTfwsADXxLRCmip8BwCreAqFH/KHNUMnnkQJfiAgbTEcuMPaIx/pY55BmqCT++bIpiMd7NQi94pFqm1PhiDRoEc+nXoOA00NXlxuaOLn+zQG0iLdA0Fp5i/ibl8I94nsgaOIPbYauEd8CoWTShwFAsAGAXDTngCefwe+RAfAsHaWYUPPnpQAglWnisVFA0wJuDkJNPEAuA8AivlZ0SQia+NfzJPjwWAKAVXwNAJ4DAj65QoZdDnCWAaCJ18xTugDfD1juBjjgAswyAGB+OZ/n08llCQkAxQ4CY+1uQM6zFAAILdXcFgCAWLogSedYBoBWrcnvrQDwGw3Cb7LQsgAQuODTH2LDLQA0CFsAgHg2ZVnotAIABPxeQlweAIvn03cFQIrH6eHkXAFITdwVgFwzFAA8uUBYQOY+IFwgXMBRGuS+XZbqqOdla4s4kQ7ZPPXMka6Rm6PpTxHLJYWl8dn6nRF/jASAnQmEBex8eiP2HhYwguLOc4QF7Hx6I/YeFjCC4s5zuLeAP/7hEVAoFlqCAAAAAElFTkSuQmCC',
    'back': 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAepJREFUeF7tmN1RBCEQhOcy0UhOM9FIvItEjUQz0VC8rlqqqD1ugWGQ3mN42YctfvqbHhg4yOTtMLl+cQDugMkJeApMbgDfBD0FPAUmJ+ApMLkB/BTwFPAU6EfgQUTeROQsIr/9pmkbuVcKQPy7iDwt4p9ZIfQAEIsP4YEDKCFYA0iJDxC+FwhtnjXubQlgSzwc8Gi8dpPhrADsUjwIWgDYrXgLALsW3wpg9+JbANyFeC2AuxGvAbAlHuO9mpxN6UFCOY2vWWldcwrkxHfUfjU0iqrPS6mNbxOMUgBM4mMaEI/L1oeWfg2Ar8tEAMHYAoRqN5QCgGiIZ4aAdMAeVAWhBkAJhJ53fwTguATilhMx/6nGorUAchD+69ob3hpSIKogaACwQMBjC0CsIVQFQQuAHUKxC1oAsEBAzuPtMW7Fjy+tAFgg/CRSAQ8w2RPBAgADBBzP2BPihjdIOGGzWQEYDQGb4ctKKWqCbIVoCSAHoTgvc1FL/Id4QIjbEAC3ICAXsaCsJRXi0YUKwBpCb/GUAAIE2BJncq/IB8PQOUDpZHU3B8C0CarD2NDRHeAOIKoDGpys7jp9CqjJWZfC6oWM6ugARpFnmdcdwBKJUetwB4wizzKvO4AlEqPW4Q4YRZ5lXncASyRGreMPhlBvQRJuMeoAAAAASUVORK5CYII='
}

def load_icon(base64_data):
    try:
        image_data = base64.b64decode(base64_data)
        image = PhotoImage(data=image_data)
        return image.subsample(3, 3)
    except Exception as e:
        print(f"İkon yüklenirken hata oluştu: {e}")
        return None

locale.setlocale(locale.LC_ALL, 'tr_TR')
root = tk.Tk()
root.title("Paisa")
root.state("zoomed")
root.configure(bg="#F8F8F8")

app_font = font.Font(family="Arial", size=10)
bold_font = font.Font(family="Arial", size=10, weight="bold")
text_font = font.Font(family="Arial", size=10, weight="bold", underline=True)

style = ttk.Style()
style.theme_use('default')

style.configure('Treeview.Heading',
    background="#2C3E50",  
    foreground="white",    
    relief="flat",         
    font=('Arial', 10, 'bold'),  
    padding=(10, 5)        
)

style.map('Treeview.Heading',
    background=[('hover', '#34495E')]  
)

style.configure('Treeview',
    background="white",
    fieldbackground="white",
    rowheight=30,         
    font=('Arial', 10)    
)

transactions = []
balance = 0
data_file = "Paisa.json"

try:
    income_icon = load_icon(ICON_DATA['income'])
    expense_icon = load_icon(ICON_DATA['expense'])
    budget_icon = load_icon(ICON_DATA['budget'])
    close_icon = load_icon(ICON_DATA['close'])
    month_icon = load_icon(ICON_DATA['month'])
    refresh_icon = load_icon(ICON_DATA['refresh'])
    graph_icon = load_icon(ICON_DATA['graph'])
    back_icon = load_icon(ICON_DATA['back'])

except Exception as e:
    print(f"İkonlar yüklenirken hata oluştu: {e}")
    income_icon = None
    expense_icon = None
    budget_icon = None
    close_icon = None
    month_icon = None
    refresh_icon = None
    graph_icon = None
    back_icon = None
    print("İkon verilerini yüklerken hata oluştu!")

def save_data():
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump({"balance": balance, "transactions": transactions}, f, ensure_ascii=False)

def load_data():
    global balance, transactions

    if os.path.exists(data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            balance = data["balance"]
            transactions = data["transactions"]
    else:
        balance = 0
        transactions = []

def load_data_for_month(year, month):
    filtered_transactions = [t for t in transactions if t[2].split('-')[1] == f"{month:02}" and t[2].split('-')[0] == str(year)]
    return filtered_transactions

def load_current_month():
    now = datetime.datetime.now()
    return load_data_for_month(now.year, now.month)

def convert_comma_to_dot(amount_str):
    return amount_str.replace(',', '.')

def add_income():
    global balance

    try:
        amount = float(convert_comma_to_dot(entry_amount.get()))
        date = entry_date.get()
        description = entry_description.get()
        timestamp = datetime.datetime.now().isoformat()
        transactions.append(('Gelir', amount, date, description, timestamp))
        balance += amount
        save_data()
        entry_amount.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        messagebox.showinfo("Paisa", "Gelir eklendi!")
    except ValueError:
        messagebox.showerror("Paisa", "Geçersiz miktar!")

def add_expense():
    global balance

    try:
        amount = float(convert_comma_to_dot(entry_amount.get()))
        date = entry_date.get()
        description = entry_description.get()
        timestamp = datetime.datetime.now().isoformat()
        transactions.append(('Gider', amount, date, description, timestamp))
        balance -= amount
        save_data()
        entry_amount.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        messagebox.showinfo("Paisa", "Gider eklendi!")
    except ValueError:
        messagebox.showerror("Paisa", "Geçersiz miktar!")

def show_budget():
    budget_window = tk.Toplevel(root)
    budget_window.title("Bütçe")
    budget_window.state("zoomed")
    budget_window.configure(bg="#F8F8F8")

    def load_selected_month():
        selected_year = year_combo.get()
        selected_month = month_combo.current() + 1
        selected_transactions = load_data_for_month(selected_year, selected_month)
        update_table(selected_transactions)

    def load_current_month_data():
        update_table(transactions) 
        month_combo.current(datetime.datetime.now().month - 1) 
        year_combo.set(datetime.datetime.now().year) 

    def update_table(transaction_list):
        table.delete(*table.get_children())
        sorted_transactions = sorted(transaction_list, key=lambda t: t[4], reverse=True)

        for i, transaction in enumerate(sorted_transactions):
            transaction_data = list(transaction[:4])
            transaction_data[1] = f"{transaction_data[1]:.2f} ₺"
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            table.insert('', tk.END, values=transaction_data, tags=(tag,))

    def show_chart():
        income_total = sum(t[1] for t in transactions if t[0] == 'Gelir')
        expense_total = sum(t[1] for t in transactions if t[0] == 'Gider')
        categories = ['Gelir', 'Gider']
        values = [income_total, expense_total]

        fig = plt.figure(figsize=(8, 5))
        fig.canvas.manager.set_window_title('Gelir-Gider Grafiği')
    
        ax = fig.add_subplot(111)
        bars = plt.bar(categories, values, color=['#41B3A2', '#C94D4D'])
        plt.title('Gelir ve Gider Durumu', fontsize=16)
        plt.ylabel('Toplam (₺)', fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='y')

        annot = ax.annotate("", 
                   xy=(0,0), 
                   xytext=(10,10), 
                   textcoords="offset points",
                   bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.9),
                   fontsize=10)
        
        annot.set_visible(False)

        def update_annot(bar, value):
            x = bar.get_x() + bar.get_width()/2.
            y = bar.get_height()
            annot.xy = (x, y)
            text = f'{value:,.2f} ₺'
            annot.set_text(text)

        def hover(event):
            if event.inaxes == ax:
                for i, bar in enumerate(bars):
                    cont, _ = bar.contains(event)

                    if cont:
                        update_annot(bar, values[i])
                        annot.set_visible(True)
                        fig.canvas.draw_idle()
                        return
            
            annot.set_visible(False)
            fig.canvas.draw_idle()

        fig.canvas.mpl_connect("motion_notify_event", hover)

        manager = plt.get_current_fig_manager()
        manager.window.wm_geometry("+%d+%d" % ((manager.window.winfo_screenwidth() // 2) - (800 // 2), (manager.window.winfo_screenheight() // 2) - (550 // 2)))

        plt.show()

    lbl_balance = tk.Label(budget_window, text=f"Bütçe: {balance:.2f} ₺", font=("Arial", 14), bg="#F8F8F8", fg="#333")
    lbl_balance.pack(pady=10)

    selection_frame = tk.Frame(budget_window, bg="#F8F8F8")
    selection_frame.pack(pady=5)

    lbl_select_year = tk.Label(selection_frame, text="Yıl:", bg="#F8F8F8", font=text_font)
    lbl_select_year.grid(row=0, column=0, padx=5)

    year_combo = ttk.Combobox(selection_frame, values=[str(year) for year in range(2024, 2099)], width=10)
    year_combo.current(0)
    year_combo.grid(row=0, column=1, padx=5)

    lbl_select_month = tk.Label(selection_frame, text="Ay:", bg="#F8F8F8", font=text_font)
    lbl_select_month.grid(row=0, column=2, padx=5)

    month_combo = ttk.Combobox(selection_frame, values=["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"], width=10)
    month_combo.current(datetime.datetime.now().month - 1) 
    month_combo.grid(row=0, column=3, padx=5)

    button_width = 100

    btn_load_month = tk.Button(
        selection_frame,
        text="Ayı Yükle",
        bg="#EADFB4",
        fg="black",
        font=bold_font,
        command=load_selected_month,
        width=button_width,
        image=month_icon,
        compound='left',
        padx=10
    )
    btn_load_month.grid(row=0, column=4, padx=5)

    btn_load_current = tk.Button(
        selection_frame,
        text="Güncel",
        bg="#9DBC98",
        fg="black",
        font=bold_font,
        command=load_current_month_data,
        width=button_width,
        image=refresh_icon,
        compound='left',
        padx=10
    )
    btn_load_current.grid(row=0, column=5, padx=5)

    btn_chart = tk.Button(
        selection_frame,
        text="Grafik",
        bg="#9BB8CD",
        fg="black",
        font=bold_font,
        command=show_chart,
        width=button_width,
        image=graph_icon,
        compound='left',
        padx=10
    )
    btn_chart.grid(row=0, column=6, padx=5)

    btn_back = tk.Button(
        budget_window,
        text="Geri",
        bg="#D4BDAC",
        fg="black",
        font=bold_font,
        command=budget_window.destroy,
        width=100,
        image=back_icon,
        compound='left',
        padx=10
    )
    btn_back.pack(side=tk.BOTTOM, pady=10)

    table_frame = tk.Frame(budget_window)
    table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(table_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    table = ttk.Treeview(table_frame, columns=('İşlem', 'Tutar', 'Tarih', 'Açıklama'), 
                        show='headings', 
                        yscrollcommand=scrollbar.set)
    
    scrollbar.config(command=table.yview)

    table.heading('İşlem', text='İŞLEM TÜRÜ')
    table.heading('Tutar', text='TUTAR')
    table.heading('Tarih', text='TARİH')
    table.heading('Açıklama', text='AÇIKLAMA')

    screen_width = budget_window.winfo_screenwidth()
    column_width = int((screen_width - 40) / 4) 

    table.column('İşlem', width=column_width, anchor='center', minwidth=150)
    table.column('Tutar', width=column_width, anchor='center', minwidth=150)
    table.column('Tarih', width=column_width, anchor='center', minwidth=150)
    table.column('Açıklama', width=column_width, anchor='center', minwidth=150)

    table.tag_configure('evenrow', background='white')
    table.tag_configure('oddrow', background='#E2DFD0')

    table.pack(fill=tk.BOTH, expand=True)

    update_table(transactions)

load_data()

frame = tk.Frame(root, bg="#F8F8F8")
frame.pack(expand=True, pady=10)

tk.Label(frame, text="Tutar:", bg="#F8F8F8", font=text_font).grid(row=0, column=0, pady=5, padx=5)
entry_amount = tk.Entry(frame, font=app_font)
entry_amount.grid(row=0, column=1, pady=5, padx=5)

tk.Label(frame, text="Tarih:", bg="#F8F8F8", font=text_font).grid(row=1, column=0, pady=5, padx=5)
entry_date = DateEntry(frame, width=12, background='#295F98', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
entry_date.grid(row=1, column=1, pady=5, padx=5)

tk.Label(frame, text="Açıklama:", bg="#F8F8F8", font=text_font).grid(row=2, column=0, pady=5, padx=5)
entry_description = tk.Entry(frame, font=app_font)
entry_description.grid(row=2, column=1, pady=5, padx=5)

button_frame = tk.Frame(frame, bg="#F8F8F8")
button_frame.grid(row=3, columnspan=2, pady=10)

btn_income = tk.Button(
    button_frame, 
    text="Gelir Ekle",
    bg="#41B3A2", 
    fg="white", 
    font=bold_font, 
    command=add_income, 
    width=145,
    image=income_icon,
    compound='left',
    padx=10 
)

btn_income.pack(side=tk.LEFT, padx=10)

btn_expense = tk.Button(
    button_frame, 
    text="Gider Ekle",
    bg="#C94D4D", 
    fg="white", 
    font=bold_font, 
    command=add_expense, 
    width=145,
    image=expense_icon,
    compound='left',
    padx=10
)

btn_expense.pack(side=tk.LEFT, padx=10)

btn_budget = tk.Button(
    button_frame, 
    text="Bütçe Görüntüle",
    bg="#EF9C66", 
    fg="black", 
    font=bold_font, 
    command=show_budget, 
    width=145,
    image=budget_icon,
    compound='left',
    padx=10
)

btn_budget.pack(side=tk.LEFT, padx=10)

btn_close = tk.Button(
    frame,
    text="Kapat",
    command=root.quit,
    bg="#295F98",
    fg="white",
    font=bold_font,
    width=526,
    image=close_icon,
    compound='left',
    padx=10
)

btn_close.grid(row=5, columnspan=2, pady=10)

root.income_icon = income_icon
root.expense_icon = expense_icon
root.budget_icon = budget_icon
root.close_icon = close_icon
root.month_icon = month_icon
root.refresh_icon = refresh_icon
root.graph_icon = graph_icon
root.back_icon = back_icon

def clear_entries(event=None):
    entry_amount.delete(0, tk.END)
    entry_description.delete(0, tk.END)

root.bind('<Escape>', clear_entries)

root.mainloop()