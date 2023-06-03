"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num = simpledialog.askstring('',"give me a number")
    not_prime= False
    for i in range(int(num)-1):
        if (int(num))%(i + 1)==0 and i!=0 and i!=int(num):
            not_prime = True

    if not_prime:
        messagebox.showinfo('', "not prime")
    else:
        messagebox.showinfo('',"prime")
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass
