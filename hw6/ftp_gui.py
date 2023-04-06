from ftplib import FTP
from tkinter import Text, Tk, Toplevel, ttk
from tkinter.messagebox import showerror, showinfo
from io import BytesIO


def ftp_connect(ftp, server, user, passwd, output_block):
    try:
        split_server = server.split(':')
        host = split_server[0]
        port = 21
        if len(split_server) >= 2:
            port = int(split_server[1])
        ftp.connect(host, port)
        ftp.login(user, passwd)
        ftp_list(ftp, output_block)
        showinfo('Successful connection', f'Connected to server {server} as {user}.')
    except:
        showerror('Connection failed', f'Failed to connect to server {server} as {user}.')


def ftp_list(ftp, output_block):
    file_list = []
    ftp.retrlines('LIST', file_list.append)
    output_block.write('\n'.join(file_list))


def ftp_save(ftp, filename, text):
    output_binary = BytesIO(text.encode())
    ftp.storbinary(f'STOR {filename}', output_binary)


def ftp_retrieve(ftp, filename, output_block):
    try:
        input_binary = BytesIO()
        ftp.retrbinary(f'RETR {filename}', input_binary.write)
        output_block.write(input_binary.getvalue())
    except:
        output_block.write('')
        showerror('Opening failed', f'Failed to open file {filename}')


def ftp_delete(ftp: FTP, filename):
    try:
        ftp.delete(filename)
        showinfo('Successful deletion', f'File {filename} deleted.')
    except:
        showerror('Deletion failed', f'Could not delete file {filename}')


def ftp_quit(ftp, root):
    try:
        ftp.quit()
    except:
        pass
    root.destroy()


def editor_quit(master, root, ftp, output_block):
    master.deiconify()
    root.destroy()
    ftp_list(ftp, output_block)


class EditorWindow:
    def __init__(self, master, ftp, filename, output_block, mode):
        lines = []
        try:
            if mode == 'create':
                empty_output = BytesIO()
                ftp.storbinary(f'STOR {filename}', empty_output)
            ftp.retrlines(f'RETR {filename}', lines.append)
        except:
            showerror('Opening failed', f'Failed to open file {filename}.')
            return

        root = Toplevel(master)
        root.title(filename)
        master.withdraw()
        content = Text(root)
        content.insert('1.0', '\n'.join(lines))
        content.grid(row=0, column=0)
        save_button = ttk.Button(root, text='Save', command=lambda:
                                 ftp_save(ftp, filename, content.get('1.0', 'end')))
        save_button.grid(row=1, column=0)
        root.protocol("WM_DELETE_WINDOW", lambda: editor_quit(master, root, ftp, output_block))


class ConnectionBlock(ttk.Frame):
    def __init__(self, master, ftp, output_block):
        super().__init__(master)

        user_entry = ttk.Entry(self)
        user_entry.insert(0, 'TestUser')
        user_entry.grid(row=0, column=0)

        server_entry = ttk.Entry(self)
        server_entry.insert(0, '192.168.1.103:21')
        server_entry.grid(row=0, column=1)

        passwd_entry = ttk.Entry(self)
        passwd_entry.insert(0, 'qwerty')
        passwd_entry.grid(row=1, column=0)

        connect_button = ttk.Button(self, text='Connect', command=lambda:
                                    ftp_connect(ftp,
                                                server_entry.get(),
                                                user_entry.get(),
                                                passwd_entry.get(),
                                                output_block))
        connect_button.grid(row=1, column=1)


class OutputBlock(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.output = Text(self, state='disabled')
        self.output.grid(row=0, column=0)

    def write(self, text):
        self.output.configure(state='normal')
        self.output.delete('1.0', 'end')
        self.output.insert('1.0', text)
        self.output.configure(state='disabled')


class ControlBlock(ttk.Frame):
    def __init__(self, master, ftp, output_block):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=2, uniform="fred")
        self.grid_columnconfigure(1, weight=1, uniform="fred")
        self.grid_columnconfigure(2, weight=1, uniform="fred")

        file_entry = ttk.Entry(self)
        file_entry.insert(0, 'test.txt')
        file_entry.grid(row=0, column=0)

        create_button = ttk.Button(self, text='Create', command=lambda:
                                   EditorWindow(master, ftp, file_entry.get(), output_block, 'create'))
        create_button.grid(row=0, column=2)

        retrieve_button = ttk.Button(self, text='Retrieve', command=lambda:
                                     ftp_retrieve(ftp, file_entry.get(), output_block))
        retrieve_button.grid(row=1, column=2)

        update_button = ttk.Button(self, text='Update', command=lambda:
                                   EditorWindow(master, ftp, file_entry.get(), output_block, 'update'))
        update_button.grid(row=2, column=2)

        delete_button = ttk.Button(self, text='Delete', command=lambda:
                                   ftp_delete(ftp, file_entry.get()))
        delete_button.grid(row=3, column=2)


def main():
    ftp = FTP()

    root = Tk()

    root.grid_columnconfigure(0, weight=1, uniform="fred")

    output_block = OutputBlock(root)
    output_block.grid(row=1, column=0)

    connection_block = ConnectionBlock(root, ftp, output_block)
    connection_block.grid(row=0, column=0)

    control_block = ControlBlock(root, ftp, output_block)
    control_block.grid(row=2, column=0)

    root.protocol("WM_DELETE_WINDOW", lambda: ftp_quit(ftp, root))
    root.mainloop()


if __name__ == '__main__':
    main()
