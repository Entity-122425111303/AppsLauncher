def choose_file(filetypes: list[tuple[str, str]], title='选择文件'):
    import tkinter
    from tkinter import filedialog
    root = tkinter.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    root.destroy()
    return file_path if file_path else None


def choose(title='选择文件夹'):
    import tkinter
    from tkinter import filedialog
    root = tkinter.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory(title=title)
    root.destroy()
    return file_path if file_path else None


if __name__ == '__main__':
    choose_file([('可执行文件', '*.bat;*.exe'), ('所有文件', '*.*')])
    choose()
