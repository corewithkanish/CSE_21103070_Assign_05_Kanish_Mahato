# -------------------------Q1----------------------------
from xml.etree.ElementPath import find
import calendar
from tkinter import *
print(">>>>>>>>>>>>>>>>>Q1<<<<<<<<<<<<<<<<<<<<\n")


def findGst():

    org_1 = int(org_price.get())

    net_1 = int(net_price.get())

    # calculating GST rate
    GST_rate = ((net_1 - org_1) * 100) / org_1

    # value in the text entry box.
    gst_rateField.insert(3, str(GST_rate) + " % ")


def clearAll():

    # Deleting the content from the entry box
    org_price.delete(0, END)

    net_price.delete(0, END)

    gst_rateField.delete(0, END)


if __name__ == "__main__":
    # Create a GUI window
    win_1 = Tk()
    win_1.title(">>>Question1<<<")

    # Set the background colour of GUI window
    win_1.configure(background="yellow")

    # set the name of tkinter GUI window
    # gui.title("GST Rate Finder")

    # Set the configuration of GUI window
    win_1.geometry("400x600")

    # Create a Original Price: label
    org_price = Label(win_1, text="Original Price",
                      bg="red")

    # Create a Net Price : label
    net_price = Label(win_1, text="Net Price",
                      bg="red")

    # Create a Find Button and attached to
    # findGst function
    find = Button(win_1, text="Find", fg="Black",
                  bg="orange",
                  command=findGst)

    # Create a Gst Rate
    GST_rate = Label(win_1, text="GST Rate", bg="red")

    # Crearing button for new tax calculator for new user
    clear = Button(win_1, text="Clear", fg="Black",
                   bg="orange",
                   command=clearAll)

    # margin from the widget.
    org_price.grid(row=1, column=1, padx=10, pady=10)

    net_price.grid(row=2, column=1, padx=10, pady=10)

    find.grid(row=3, column=2, padx=10, pady=10)

    GST_rate.grid(row=4, column=1, padx=10, pady=10)

    clear.grid(row=5, column=2, padx=10, pady=10)

    # Create a text entry box for filling or typing the information.
    org_price = Entry(win_1)

    net_price = Entry(win_1)

    gst_rateField = Entry(win_1)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    org_price.grid(row=1, column=2, padx=10, pady=10)

    net_price.grid(row=2, column=2, padx=10, pady=10)

    gst_rateField.grid(row=4, column=2, padx=10, pady=10)

    # Start the GUI
    win_1.mainloop()
print("------------------------++++++---------------------------")

# ------------------------------Q2----------------------------
print(">>>>>>>>>>>>>>>>>>>>>>>Q2<<<<<<<<<<<<<<<<<<<<<<<<<<")


# import all methods and classes from the tkinter

# import calendar module


def showCal():

    # Create a GUI window
    new_gui = Tk()

    new_gui.config(background="yellow")

    new_gui.title(">>>>Q2<<<<")

    # Set the configuration of GUI window
    new_gui.geometry("600x1000")

    # get method returns current text as string
    fetch_year = int(year_field.get())

    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)

    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row=5, column=1, padx=20)

    # start the GUI
    new_gui.mainloop()


if __name__ == "__main__":

    # Create a GUI window
    gui_2 = Tk()

    # Set the background colour of GUI window
    gui_2.config(background="yellow")

    # set the name of tkinter GUI window
    gui_2.title("CALENDAR")

    # Set the configuration of GUI window
    gui_2.geometry("500x300")

    # Create a CALENDAR : label with specified font and size
    cal = Label(gui_2, text="CALENDAR", bg="light green",
                font=("times", 65, 'bold'))

    # Create a Enter Year : label
    year = Label(gui_2, text="Enter Year", bg="brown")

    # Create a text entry box for filling or typing the information.
    year_field = Entry(gui_2)

    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui_2, text="Show Calendar", fg="Black",
                  bg="brown", command=showCal)

    # Create a Exit Button and attached to exit function
    Exit = Button(gui_2, text="Exit", fg="Black", bg="brown", command=exit)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    # start the GUI
    gui_2.mainloop()

print("-----------------------++++++------------------------------------")


# --------------------Q3---------------------------
print(">>>>>>>>>>>>>>>>>Q3<<<<<<<<<<<<<<<<<<<<\n")


expression = ""


def press(num):

    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalpress():

    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:

        equation.set(" error ")
        expression = ""


# Fo clearing all input and output value
def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    gui.configure(background="light yellow")

    gui.title(">>>Q3<<<")

    gui.geometry("500x800")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    # expression_field.geometry("500x500")
    expression_field.grid(columnspan=4, ipadx=70)

    button_1 = Button(gui, text=' 1 ', fg='black', bg='red',
                      command=lambda: press(1), height=1, width=7)
    button_1.grid(row=2, column=0)

    button_2 = Button(gui, text=' 2 ', fg='black', bg='red',
                      command=lambda: press(2), height=1, width=7)
    button_2.grid(row=2, column=1)

    button_3 = Button(gui, text=' 3 ', fg='black', bg='red',
                      command=lambda: press(3), height=1, width=7)
    button_3.grid(row=2, column=2)

    button_4 = Button(gui, text=' 4 ', fg='black', bg='red',
                      command=lambda: press(4), height=1, width=7)
    button_4.grid(row=3, column=0)

    button_5 = Button(gui, text=' 5 ', fg='black', bg='red',
                      command=lambda: press(5), height=1, width=7)
    button_5.grid(row=3, column=1)

    button_6 = Button(gui, text=' 6 ', fg='black', bg='red',
                      command=lambda: press(6), height=1, width=7)
    button_6.grid(row=3, column=2)

    button_7 = Button(gui, text=' 7 ', fg='black', bg='red',
                      command=lambda: press(7), height=1, width=7)
    button_7.grid(row=4, column=0)

    button_8 = Button(gui, text=' 8 ', fg='black', bg='red',
                      command=lambda: press(8), height=1, width=7)
    button_8.grid(row=4, column=1)

    button_9 = Button(gui, text=' 9 ', fg='black', bg='red',
                      command=lambda: press(9), height=1, width=7)
    button_9.grid(row=4, column=2)

    button_0 = Button(gui, text=' 0 ', fg='black', bg='red',
                      command=lambda: press(0), height=1, width=7)
    button_0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                            command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
print("------------------------++++++---------------------------")


# -------------------------Q4----------------------------
print(">>>>>>>>>>>>>>>>>>>>>Q4<<<<<<<<<<<<<<<<<<<<<<<<<\n")
lst = []


num_1 = int(input("Enter no. of students entering their input  \n"))


for i in range(0, num_1):
    print("Enter marks of students:--")
    ele = int(input())
    lst.append(ele)


def bubble_sort(nums):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:

                nums[i], nums[i + 1] = nums[i + 1], nums[i]

                swapped = True


print("Sortinng list")
bubble_sort(lst)
print(lst)
print("------------------------++++++---------------------------")


# -------------------------Q5----------------------------
print(">>>>>>>>>>>>>>>>>Q5<<<<<<<<<<<<<<<<<<<<\n")


kist = []

# number of elements as input
num_1 = int(input("How many number you are entering  \n"))

# iterating till the range
for i in range(0, num_1):
    ele = int(input())

    kist.append(ele)  # adding the element

list_dup = kist
print(list_dup)


# a)part:==>
print("a)part:==>")
print("Ascending Order:==>")
list_dup.sort()
print(list_dup)

# b)part:==>
print("b)part:==>")
find_1 = int(input("Enter number you want to find it:--\n"))

# Returns index of x in arr if present, else -1


def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Function call
result = binary_search(list_dup, 0, len(list_dup)-1, find_1)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# c)part:--
ask_1 = int(input("Number you want to ask\n"))


def count_number(list_dup, find):
    count = 0
    for ele in list_dup:
        if (ele == find):
            count = count + 1
    return count


print("c)part:--")
print("The number %d has occured %d times" %
      (find_1, count_number(list_dup, find_1)))
print("------------------------++++++---------------------------")
