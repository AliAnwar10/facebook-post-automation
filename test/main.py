import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from db_Insert import insert_credential, insert_group, insert_post, insert_post_selection, get_credentials, get_groups, get_posts, clear_selections
from playwright_runner import run_automation

# Create main window
root = tk.Tk()
root.title("Easy Facebook Group Poster")
root.geometry("600x400")

# Create notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill="both", expand=True)

# Variables for entries
email_var = tk.StringVar()
password_var = tk.StringVar()
group_name_var = tk.StringVar()
group_url_var = tk.StringVar()
post_title_var = tk.StringVar()
post_hashtags_var = tk.StringVar()
image_path_var = tk.StringVar()
check_vars = []

# Tab 1: Credentials
cred_frame = ttk.Frame(notebook)
notebook.add(cred_frame, text="Credentials")

tk.Label(cred_frame, text="Email").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(cred_frame, textvariable=email_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(cred_frame, text="Password").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(cred_frame, textvariable=password_var, show="*").grid(row=1, column=1, padx=5, pady=5)

def save_credentials():
    email = email_var.get()
    password = password_var.get()
    if email and password:
        insert_credential(email, password)
        email_var.set("")
        password_var.set("")
        messagebox.showinfo("Success", "Credentials saved!")
    else:
        messagebox.showerror("Error", "Please fill in both fields.")

tk.Button(cred_frame, text="Save", command=save_credentials).grid(row=2, column=0, columnspan=2, pady=10)

# Tab 2: Groups
group_frame = ttk.Frame(notebook)
notebook.add(group_frame, text="Groups")

tk.Label(group_frame, text="Group Name").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(group_frame, textvariable=group_name_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(group_frame, text="Group URL").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(group_frame, textvariable=group_url_var).grid(row=1, column=1, padx=5, pady=5)

def save_group():
    name = group_name_var.get()
    url = group_url_var.get()
    if name and url:
        insert_group(name, url)
        group_name_var.set("")
        group_url_var.set("")
        messagebox.showinfo("Success", "Group saved!")
    else:
        messagebox.showerror("Error", "Please fill in both fields.")

tk.Button(group_frame, text="Save", command=save_group).grid(row=2, column=0, columnspan=2, pady=10)

# Tab 3: Posts
post_frame = ttk.Frame(notebook)
notebook.add(post_frame, text="Posts")

tk.Label(post_frame, text="Title").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(post_frame, textvariable=post_title_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(post_frame, text="Description").grid(row=1, column=0, padx=5, pady=5)
post_desc_text = tk.Text(post_frame, height=3, width=20)
post_desc_text.grid(row=1, column=1, padx=5, pady=5)

tk.Label(post_frame, text="Hashtags").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(post_frame, textvariable=post_hashtags_var).grid(row=2, column=1, padx=5, pady=5)

tk.Label(post_frame, text="Image").grid(row=3, column=0, padx=5, pady=5)
tk.Entry(post_frame, textvariable=image_path_var).grid(row=3, column=1, padx=5, pady=5)

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        image_path_var.set(file_path)

tk.Button(post_frame, text="Browse Image", command=browse_image).grid(row=3, column=2, padx=5, pady=5)

def save_post():
    title = post_title_var.get()
    description = post_desc_text.get("1.0", tk.END).strip()
    hashtags = post_hashtags_var.get()
    image_path = image_path_var.get()
    if title and description:
        insert_post(title, description, hashtags, image_path)
        post_title_var.set("")
        post_desc_text.delete("1.0", tk.END)
        post_hashtags_var.set("")
        image_path_var.set("")
        messagebox.showinfo("Success", "Post saved!")
    else:
        messagebox.showerror("Error", "Please fill in title and description.")

tk.Button(post_frame, text="Save", command=save_post).grid(row=4, column=0, columnspan=3, pady=10)

# Tab 4: Load Data
load_frame = ttk.Frame(notebook)
notebook.add(load_frame, text="Load Data")

cred_combo = ttk.Combobox(load_frame, state="readonly")
cred_combo.grid(row=0, column=1, padx=5, pady=5)
tk.Label(load_frame, text="Choose Credential").grid(row=0, column=0, padx=5, pady=5)

# checkboxes
check_frame = ttk.Frame(load_frame)
check_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def load_data():
    global check_vars
    # Clear previous checkboxes
    for widget in check_frame.winfo_children():
        widget.destroy()
    check_vars = []

    # Load credentials
    credentials = get_credentials()
    cred_combo["values"] = [c[1] for c in credentials]
    if credentials:
        cred_combo.current(0)

    # Load groups and posts
    groups = get_groups()
    posts = get_posts()

    # Create checkbox grid
    tk.Label(check_frame, text="Posts / Groups").grid(row=0, column=0, padx=5, pady=5)
    for j, group in enumerate(groups):
        tk.Label(check_frame, text=group[1]).grid(row=0, column=j+1, padx=5, pady=5)

    for i, post in enumerate(posts):
        tk.Label(check_frame, text=post[1]).grid(row=i+1, column=0, padx=5, pady=5)
        row_vars = []
        for j, group in enumerate(groups):
            var = tk.BooleanVar()
            tk.Checkbutton(check_frame, variable=var).grid(row=i+1, column=j+1, padx=5, pady=5)
            row_vars.append((group[0], post[0], var))
        check_vars.append(row_vars)

tk.Button(load_frame, text="Load Data", command=load_data).grid(row=1, column=0, columnspan=2, pady=10)

def save_selections():
    clear_selections()
    credentials = get_credentials()
    if credentials and cred_combo.current() >= 0:
        credential_id = credentials[cred_combo.current()][0]
        for row in check_vars:
            for group_id, post_id, var in row:
                if var.get():
                    insert_post_selection(credential_id, group_id, post_id)
        messagebox.showinfo("Success", "Selections saved!")
    else:
        messagebox.showerror("Error", "No credential selected.")

tk.Button(load_frame, text="Save Selections", command=save_selections).grid(row=3, column=0, columnspan=2, pady=10)

# Tab 5: Automation
auto_frame = ttk.Frame(notebook)
notebook.add(auto_frame, text="Automation")

def start_automation():
    credentials = get_credentials()
    if not credentials:
        messagebox.showerror("Error", "No credentials found.")
        return
    if cred_combo.current() < 0:
        messagebox.showerror("Error", "Please select a credential in Load Data tab.")
        return
    credential_id = credentials[cred_combo.current()][0]
    import asyncio
    asyncio.run(run_automation(credential_id))
    messagebox.showinfo("Success", "Automation completed!")

tk.Button(auto_frame, text="Start Automation", command=start_automation).grid(row=0, column=0, pady=10)

# Start the app
root.mainloop()