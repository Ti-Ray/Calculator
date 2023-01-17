from tkinter import*
from tkinter import messagebox
import fileinput
from tkinter import filedialog 

page = Tk()
page.title("Ian Ray Calc")
page.config(bg="grey51")
page.geometry("530x500")
page.maxsize(500, 500)
page.minsize(500, 500)

global check 
#
leng_space = [
    "Decimiter",
    "Millimeter",
    "Kilometer",
    "Centimeter",
    "Meter",
    "Micrometer",
    "Yard",
    "Nautical mile",
    "Foot",
    "Mile",
    "Inch"
]
#
area_space = [
    "Square_meter",
    "Square_decimeter",
    "Square_centimeter",
    "Square_kilometer",
    "Square_millimeter",
    "Are",
    "Hectare",
    "Squre_mile",
    "Square_yard",
    "Square_foot",
    "Acre",
    "Square_inch"
]
#
vol_space = [
    "Cubic_meter",
    "Cubic_centimeter",
    "Deciliter",
    "Centiliter",
    "Cubic_decimeter",
    "Liter",
    "Cubic_millimeter",
    "Milliliter"
    "Uk_gallon",
    "Us_gallon"
]
#
speed_space = [
    "Light_speed",
    "Miles/hour",
    "Mach",
    "Meter/second",
    "kilometer/hour"
]
#
weight_space = [
    "Grams",
    "Micrograms",
    "Tonne",
    "Milligram",
    "Kilogram",
    "Pound",
    "Ounce"
]
#
temp_space = [
    "Celsius",
    "Fahrenheit",
    "Kelvin"
]
#
power_space = [
    "Joule/second",
    "Metric_horsepower",
    "Kilocaloric/second",
    "Watt",
    "Imperial_horsepower",
    "Foot_pound/second",
    "Newton_meter/second",
    "Kilowatt"
]

pressure_space = [
    "Pounds/square_foot",
    "Pounds/square_inch",
    "Millimeter_of_mercury",
    "Bar",
    "Inch_of_mercury",
    "Millibar",
    "Hectopascal",
    "Standard_atmosphere",
    "Kilopascal",
    "Megapascal"
]
#
def leng():
    conv_frame.destroy()
    global len_frame
    len_frame = Frame(page, bg="grey")
    len_frame.pack(padx=10, pady=10)
    Button(len_frame, text=" < Back ", font="bold", command=bck_leng, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    pg_frame = Frame(len_frame)
    pg_frame.pack(padx=10, pady=10)
    sec_frame = Frame(len_frame)
    sec_frame.pack()
    ans_frame = LabelFrame(len_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
        ck = clicked.get()
        ck1 = clicked2.get()
        try:
                    num = int(frm_ent.get())
                    if ck == "Decimiter" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Millimeter":
                        con = (ck,"To",ck1,"=")
                        summ = int(num) * int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(9.144)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(18520)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(3.048)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(16090)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Decimiter" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(3.937)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(914.4)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1852000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(304.8)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1609000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Millimeter" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(25.4)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1094)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1.852)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(3281)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(9.461e+16)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Kilometer" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(39370)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(91.44)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(185200)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(30.48)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(160900)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Centimeter" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(2.54)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1.094)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1852)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(3.821)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1609)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Meter" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(39.97)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(914400)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Millimeter":
                        print("Micrometer To Millimeter")
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1852000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(304800)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1609000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Micrometer" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(25400)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(9.144)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(914.4)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1094)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(91.44)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1094)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(914400)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(2025)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(3)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1760)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Yard" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(36)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(2025)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(18520)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1852000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1.852)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(185200)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1852)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1852000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(6076)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1.151)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Nautical mile" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(72910)
                        tt = (num,con,summ)
                        ans.config(text=tt) 
                    elif ck == "Foot" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(3)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(3.048)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(304.8)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(3281)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(30.48)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(3.281)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(304800)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(6076)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(5280)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Foot" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(12)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1760)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(16090)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1609000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1.609)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(160900)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1609)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1609000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1.151)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(5280)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Mile" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(63360)
                        tt = (num,con,summ)
                        ans.config(text=tt) 
                    elif ck == "Inch" and ck1 == "Yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(36)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Decimiter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(3.937)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(25.4)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(39370)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(2.54)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(39.37)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Micrometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(25400)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Nautical mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(72910)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(12)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(63360)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Inch" and ck1 == "Inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)      
                    else:
                        messagebox.showinfo("Error", "Enter a Number:")
        except:
            messagebox.showinfo("Error", "Enter a Number:")
            bck_leng()
            leng()
            
        #print(ck)
        #print(ck1)

    label = Label(sec_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(sec_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(leng_space[0])
    opt = OptionMenu(pg_frame,clicked , *leng_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(pg_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(leng_space[0])
    opt_to = OptionMenu(pg_frame, clicked2, *leng_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(sec_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)
# 
def area():
    conv_frame.destroy()
    global area_frame
    area_frame = Frame(page, bg="grey")
    area_frame.pack(padx=10, pady=10)
    Button(area_frame, text=" < Back ", font="bold", command=bck_area, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    sec_frame = Frame(area_frame)
    sec_frame.pack(padx=10, pady=10)
    min_frame = Frame(area_frame)
    min_frame.pack(padx=10, pady=10)
    ans_frame = LabelFrame(area_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
                ck = clicked.get()
                ck1 = clicked2.get()
                try:
                    num = int(frm_ent.get())
                    if ck == "Square_meter" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1,"=")
                        summ = int(num) * int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(2590000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1.196)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10.764)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(4047)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_meter" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1550)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(259000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(83.613)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(9.29)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(404700)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_decimeter" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(15.5)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(25900000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(8361)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(929)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(40470000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_centimeter" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(6.452)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000) 
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(2.59)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1196000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10760000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(247.1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_kilometer" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1550000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1000000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(2590000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(836100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(92900)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(4047000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_millimeter" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(645.2)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(25900)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(119.6)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1076)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(40.469)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Are" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(155000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(10000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(259)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(11960)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(107600)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(2.471)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Hectare" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(15500000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(2590000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(259000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(25900000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(259)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(2590000000000)
                        tt = (num,con,summ)
                        ans.config(text=tt) 
                    elif ck == "Squre_mile" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(25900)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(25900)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(3098000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(27880000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(640)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Squre_mile" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(4014000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1.196)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(83.613)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(8361)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1196000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(836100)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(119.6)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(11960)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(3098000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(9)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(4840)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_yard" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1296)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10.764)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(9.29)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(929)
                        tt = (num,con,summ)
                        ans.config(text=tt) 
                    elif ck == "Square_foot" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(10760000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(92900)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1076)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(107600)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(27880000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(9)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(43560)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_foot" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(6273000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(4047)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(404700)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(40470000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(247.1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(4047000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(40.469)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(2.471)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(640)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(4840)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(43560)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Acre" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(6273000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_meter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1550)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_decimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(15.5)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_centimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(6.452)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_kilometer":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1550000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_millimeter":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(645.2)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Are":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(155000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Hectare":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(15500000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Squre_mile":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(4014000000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_yard":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(1296)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_foot":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(144)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Acre":
                        con = (ck,"To",ck1)
                        summ = int(num) / int(6273000)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    elif ck == "Square_inch" and ck1 == "Square_inch":
                        con = (ck,"To",ck1)
                        summ = int(num) * int(1)
                        tt = (num,con,summ)
                        ans.config(text=tt)
                    else:
                        messagebox.showinfo("Error", "Enter a Number:")
                except:
                    messagebox.showinfo("Error", "Enter a Number:")
                    bck_leng()
                    leng()

    label = Label(min_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(min_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(area_space[0])
    opt = OptionMenu(sec_frame,clicked , *area_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(sec_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(area_space[0])
    opt_to = OptionMenu(sec_frame, clicked2, *area_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(min_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)
#
def vol():
    conv_frame.destroy()
    global vol_frame
    vol_frame = Frame(page, bg="grey")
    vol_frame.pack(padx=10, pady=10)
    Button(vol_frame, text=" < Back ", font="bold", command=bck_vol, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    sec_frame = Frame(vol_frame)
    sec_frame.pack(padx=10, pady=10)
    min_frame = Frame(vol_frame)
    min_frame.pack(padx=10, pady=10)
    ans_frame = LabelFrame(vol_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
        ck = clicked.get()
        ck1 = clicked2.get()
        try:
            num = int(frm_ent.get())
            if ck == "Cubic_meter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(100000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) * int(220)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_meter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) * int(264.2)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Cubic_centimeter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int()
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(4546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_centimeter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(3785)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Deciliter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(100000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(45.461)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Deciliter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(37.854)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Centiliter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(100000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) / int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) / int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(454.6)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Centiliter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(378.5)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Cubic_decimeter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(4.546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_decimeter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(3.785)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Liter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(4.546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Liter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(3.785)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Cubic_millimeter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(100000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(4546000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Cubic_millimeter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(3785000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Milliliter" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int()
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(4546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milliliter" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(3785)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Uk_gallon" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(220)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(4546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(45.461)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(454.6)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(4.546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) * int(4.546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(4546000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(4546)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Uk_gallon" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) * int(1.201)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Us_gallon" and ck1 == "Cubic_meter":
                con = (ck,"To",ck1)
                summ = int(num) / int(264.2)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Cubic_centimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(3785)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Deciliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(37.854)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Centiliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(378.5)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Cubic_decimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(3.785)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Liter":
                con = (ck,"To",ck1)
                summ = int(num) * int(3.785)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Cubic_millimeter":
                con = (ck,"To",ck1)
                summ = int(num) * int(3785000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Milliliter":
                con = (ck,"To",ck1)
                summ = int(num) * int(3785)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Uk_gallon":
                con = (ck,"To",ck1)
                summ = int(num) / int(1.201)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Us_gallon" and ck1 == "Us_gallon":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            else:
                messagebox.showinfo("Error", "Please enter a number: ")
        except:
            messagebox.showinfo("Error", "Please enter a number: ")
            bck_vol()
            vol()

    label = Label(min_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(min_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(vol_space[0])
    opt = OptionMenu(sec_frame,clicked , *vol_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(sec_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(vol_space[0])
    opt_to = OptionMenu(sec_frame, clicked2, *vol_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(min_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)
#
def speed():
    conv_frame.destroy()
    global speed_frame
    speed_frame = Frame(page, bg="grey")
    speed_frame.pack(padx=10, pady=10)
    Button(speed_frame, text=" < Back ", font="bold", command=bck_speed, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    sec_frame = Frame(speed_frame)
    sec_frame.pack(padx=10, pady=10)
    min_frame = Frame(speed_frame)
    min_frame.pack(padx=10, pady=10)
    ans_frame = LabelFrame(speed_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
        ck = clicked.get()
        ck1 = clicked2.get()
        try:
            num = int(frm_ent.get())
            if ck == "Light_speed" and ck1 == "Light_speed":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Light_speed" and ck1 == "Miles/hour":
                con = ("=")
                summ = int(num) * int(670600000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Light_speed" and ck1 == "Mach":
                con = ("=")
                summ = int(num) * int(874030)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Light_speed" and ck1 == "Meter/second":
                con = ("=")
                summ = int(num) * int(299800000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Light_speed" and ck1 == "kilometer/hour":
                con = ("=")
                summ = int(num) * int(1079000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Miles/hour" and ck1 == "Light_speed":
                con = ("=")
                summ = int(num) / int(670600000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Miles/hour" and ck1 == "Miles/hour":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Miles/hour" and ck1 == "Mach":
                con = ("=")
                summ = int(num) / int(767.3)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Miles/hour" and ck1 == "Meter/second":
                con = ("=")
                summ = int(num) * int(2.237)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Miles/hour" and ck1 == "kilometer/hour":
                con = ("=")
                summ = int(num) * int(1.609)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Mach" and ck1 == "Light_speed":
                con = ("=")
                summ = int(num) / int(874030)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Mach" and ck1 == "Miles/hour":
                con = ("=")
                summ = int(num) * int(767.3)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Mach" and ck1 == "Mach":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Mach" and ck1 == "Meter/second":
                con = ("=")
                summ = int(num) * int(343)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Mach" and ck1 == "kilometer/hour":
                con = ("=")
                summ = int(num) * int(1235)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Meter/second" and ck1 == "Light_speed":
                con = ("=")
                summ = int(num) / int(299800000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Meter/second" and ck1 == "Miles/hour":
                con = ("=")
                summ = int(num) * int(2.237)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Meter/second" and ck1 == "Mach":
                con = ("=")
                summ = int(num) / int(343)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Meter/second" and ck1 == "Meter/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Meter/second" and ck1 == "kilometer/hour":
                con = ("=")
                summ = int(num) * int(3.6)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "kilometer/hour" and ck1 == "Light_speed":
                con = ("=")
                summ = int(num) / int(1079000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "kilometer/hour" and ck1 == "Miles/hour":
                con = ("=")
                summ = int(num) / int(1.609)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "kilometer/hour" and ck1 == "Mach":
                con = ("=")
                summ = int(num) / int(1235)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "kilometer/hour" and ck1 == "Meter/second":
                con = ("=")
                summ = int(num) / int(3.6)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "kilometer/hour" and ck1 == "kilometer/hour":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            else:
                messagebox.showinfo("Error", "Plz insert a number :")
        except:
            messagebox.showinfo("Error", "Plz insert a number :")
            bck_speed()
            speed()

    label = Label(min_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(min_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(speed_space[0])
    opt = OptionMenu(sec_frame,clicked , *speed_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(sec_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(speed_space[0])
    opt_to = OptionMenu(sec_frame, clicked2, *speed_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(min_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)
#
def weight():
    conv_frame.destroy()
    global weight_frame
    weight_frame = Frame(page, bg="grey")
    weight_frame.pack(padx=10, pady=10)
    Button(weight_frame, text=" < Back ", font="bold", command=bck_weight, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    sec_frame = Frame(weight_frame)
    sec_frame.pack(padx=10, pady=10)
    min_frame = Frame(weight_frame)
    min_frame.pack(padx=10, pady=10)
    ans_frame = LabelFrame(weight_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
        ck = clicked.get()
        ck1 = clicked2.get()
        try:
            num = int(frm_ent.get())
            if ck == "Grams" and ck1 == "Grams":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Grams" and ck1 == "Micrograms":
                con = ("=")
                summ = int(num) * int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Grams" and ck1 == "Tonne":
                con = ("=")
                summ = int(num) / int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Grams" and ck1 == "Milligram":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Grams" and ck1 == "Kilogram":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Grams" and ck1 == "Pound":
                con = ("=")
                summ = int(num) / int(453.6)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Grams" and ck1 == "Ounce":
                con = ("=")
                summ = int(num) / int(28.35)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Micrograms" and ck1 == "Grams":
                con = ("=")
                summ = int(num) / int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Micrograms" and ck1 == "Micrograms":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Micrograms" and ck1 == "Tonne":
                con = ("=")
                summ = int(num) / int(1000000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Micrograms" and ck1 == "Milligram":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Micrograms" and ck1 == "Kilogram":
                con = ("=")
                summ = int(num) / int(1000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Micrograms" and ck1 == "Pound":
                con = ("=")
                summ = int(num) / int(453600000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Micrograms" and ck1 == "Ounce":
                con = ("=")
                summ = int(num) / int(28350000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Tonne" and ck1 == "Grams":
                con = ("=")
                summ = int(num) * int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Tonne" and ck1 == "Micrograms":
                con = ("=")
                summ = int(num) * int(1000000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Tonne" and ck1 == "Tonne":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Tonne" and ck1 == "Milligram":
                con = ("=")
                summ = int(num) * int(1000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Tonne" and ck1 == "Kilogram":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Tonne" and ck1 == "Pound":
                con = ("=")
                summ = int(num) * int(2205)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Tonne" and ck1 == "Ounce":
                con = ("=")
                summ = int(num) * int(35270)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Milligram" and ck1 == "Grams":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milligram" and ck1 == "Micrograms":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milligram" and ck1 == "Tonne":
                con = ("=")
                summ = int(num) / int(1000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milligram" and ck1 == "Milligram":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milligram" and ck1 == "Kilogram":
                con = ("=")
                summ = int(num) / int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milligram" and ck1 == "Pound":
                con = ("=")
                summ = int(num) / int(453600)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Milligram" and ck1 == "Ounce":
                con = ("=")
                summ = int(num) / int(28350)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Kilogram" and ck1 == "Grams":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilogram" and ck1 == "Micrograms":
                con = ("=")
                summ = int(num) * int(1000000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilogram" and ck1 == "Tonne":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilogram" and ck1 == "Milligram":
                con = ("=")
                summ = int(num) * int(1000000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilogram" and ck1 == "Kilogram":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilogram" and ck1 == "Pound":
                con = ("=")
                summ = int(num) * int(2.205)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilogram" and ck1 == "Ounce":
                con = ("=")
                summ = int(num) * int(35.274)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Pound" and ck1 == "Grams":
                con = ("=")
                summ = int(num) * int(453.6)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pound" and ck1 == "Micrograms":
                con = ("=")
                summ = int(num) * int(453600000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pound" and ck1 == "Tonne":
                con = ("=")
                summ = int(num) / int(2205)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pound" and ck1 == "Milligram":
                con = ("=")
                summ = int(num) * int(453600)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pound" and ck1 == "Kilogram":
                con = ("=")
                summ = int(num) / int(2.205)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pound" and ck1 == "Pound":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pound" and ck1 == "Ounce":
                con = ("=")
                summ = int(num) * int(16)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Ounce" and ck1 == "Grams":
                con = ("=")
                summ = int(num) * int(28.35)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Ounce" and ck1 == "Micrograms":
                con = ("=")
                summ = int(num) * int(28350000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Ounce" and ck1 == "Tonne":
                con = ("=")
                summ = int(num) / int(35270)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Ounce" and ck1 == "Milligram":
                con = ("=")
                summ = int(num) * int(28350)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Ounce" and ck1 == "Kilogram":
                con = ("=")
                summ = int(num) / int(35.274)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Ounce" and ck1 == "Pound":
                con = ("=")
                summ = int(num) / int(16)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Ounce" and ck1 == "Ounce":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            else:
                messagebox.showinfo("Error", "Please enter a number: ")
        except:
            messagebox.showinfo("Error", "Please enter a number: ")
            bck_weight()
            weight()       

    label = Label(min_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(min_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(weight_space[0])
    opt = OptionMenu(sec_frame,clicked , *weight_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(sec_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(weight_space[0])
    opt_to = OptionMenu(sec_frame, clicked2, *weight_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(min_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)
#
def temp():
    conv_frame.destroy()
    global temp_frame
    temp_frame = Frame(page, bg="grey")
    temp_frame.pack(padx=10, pady=10)
    Button(temp_frame, text=" < Back ", font="bold", command=bck_temp, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    sec_frame = Frame(temp_frame)
    sec_frame.pack(padx=10, pady=10)
    min_frame = Frame(temp_frame)
    min_frame.pack(padx=10, pady=10)
    ans_frame = LabelFrame(temp_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
        ck = clicked.get()
        ck1 = clicked2.get()
        try:
            num = int(frm_ent.get())
            if ck == "Celsius" and ck1 == "Celsius":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Celsius" and ck1 == "Fahrenheit":
                con = (ck,"To",ck1)
                summ = int(num) * int(9/5) + int(32)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Celsius" and ck1 == "Kelvin":
                con = (ck,"To",ck1)
                summ = int(num) + int(273)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Fahrenheit" and ck1 == "Celsius":
                con = (ck,"To",ck1)
                summ = int(num) - int(32) * int(5/9)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Fahrenheit" and ck1 == "Fahrenheit":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Fahrenheit" and ck1 == "Kelvin":
                con = (ck,"To",ck1)
                summ = int(num) - int(32) * int(5/9) + int(273)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kelvin" and ck1 == "Celsius":
                con = (ck,"To",ck1)
                summ = int(num) - int(273)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kelvin" and ck1 == "Kelvin":
                con = (ck,"To",ck1)
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kelvin" and ck1 == "Fahrenheit":
                con = (ck,"To",ck1)
                summ = int(num) - int(273) * int(9/5) + int(32)
                tt = (num,con,summ)
                ans.config(text=tt)
            else:
                messagebox.showinfo("Error", "Please enter a number: ")
        except:
            messagebox.showinfo("Error", "Please enter a number: ")
            bck_temp()
            temp()


    label = Label(min_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(min_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(temp_space[0])
    opt = OptionMenu(sec_frame,clicked ,*temp_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(sec_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(temp_space[0])
    opt_to = OptionMenu(sec_frame, clicked2, *temp_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(min_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)
#
def power():
    conv_frame.destroy()
    global power_frame
    power_frame = Frame(page, bg="grey")
    power_frame.pack(padx=10, pady=10)
    Button(power_frame, text=" < Back ", font="bold", command=bck_power, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    sec_frame = Frame(power_frame)
    sec_frame.pack(padx=10, pady=10)
    min_frame = Frame(power_frame)
    min_frame.pack(padx=10, pady=10)
    ans_frame = LabelFrame(power_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
        ck = clicked.get()
        ck1 = clicked2.get()
        try:
            num = int(frm_ent.get())
            if ck == "Joule/second" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Joule/second" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) / int(735.49876)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Joule/second" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) / int(4184.1004184)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Joule/second" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Joule/second" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) / int(745.69987)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Joule/second" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) / int(1.355818)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Joule/second" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Joule/second" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Metric_horsepower" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(735.49876)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Metric_horsepower" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Metric_horsepower" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) / int(5.687933)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Metric_horsepower" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(735.49876)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Metric_horsepower" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) / int(1.0138696)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Metric_horsepower" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) * int(542.47605)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Metric_horsepower" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(735.49876)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Metric_horsepower" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) * int(1.3596216)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Kilocaloric/second" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(4184.10042)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Kilocaloric/second" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) * int(5.68879)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilocaloric/second" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilocaloric/second" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(4184.10042)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilocaloric/second" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) * int(5.61097)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilocaloric/second" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) * int(3086.034096)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilocaloric/second" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(4184.10042)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilocaloric/second" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) * int(4.18410042)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Watt" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Watt" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) / int(735.49875936069271)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Watt" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) / int(4184.100418410041841)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Watt" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Watt" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) / int(745.699865796395153)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Watt" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) / int(1.355817949024906)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Watt" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Watt" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Imperial_horsepower" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(745.69987)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Imperial_horsepower" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) * int(1.0138694)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Imperial_horsepower" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) / int(5.6109711297071129707056861)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Imperial_horsepower" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(745.69987)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Imperial_horsepower" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Imperial_horsepower" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) * int(550)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Imperial_horsepower" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(74569987)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Imperial_horsepower" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) / int(1.3410221)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Foot_pound/second" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(1.3558)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Foot_pound/second" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) / int(542.476045467356505380164519)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Foot_pound/second" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) / int(3086.0340958158995815868721249)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Foot_pound/second" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(1.3558)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Foot_pound/second" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) / int(549.9999954512308189202242817)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Foot_pound/second" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Foot_pound/second" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(1.3558)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Foot_pound/second" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) / int(737.5621489)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Newton_meter/second" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Newton_meter/second" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) / int(735.49875936069271)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Newton_meter/second" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) / int(4184.100418410041841)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Newton_meter/second" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Newton_meter/second" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) / int(745.699865796395153)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Newton_meter/second" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) / int(1.355817949024906)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Newton_meter/second" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Newton_meter/second" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Kilowatt" and ck1 == "Joule/second":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Kilowatt" and ck1 == "Metric_horsepower":
                con = ("=")
                summ = int(num) * int(1.36)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilowatt" and ck1 == "Kilocaloric/second":
                con = ("=")
                summ = int(num) / int(4.184100418410041841)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilowatt" and ck1 == "Watt":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilowatt" and ck1 == "Imperial_horsepower":
                con = ("=")
                summ = int(num) * int(1.341)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilowatt" and ck1 == "Foot_pound/second":
                con = ("=")
                summ = int(num) * int(737.56)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilowatt" and ck1 == "Newton_meter/second":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilowatt" and ck1 == "Kilowatt":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            else:
                messagebox.showinfo("Error", "Please enter a number: ")
        except:
            messagebox.showinfo("Error", "Please enter a number: ")
            bck_power()
            power()

    label = Label(min_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(min_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(power_space[0])
    opt = OptionMenu(sec_frame,clicked , *power_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(sec_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(power_space[0])
    opt_to = OptionMenu(sec_frame, clicked2, *power_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(min_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)
#  
def pressure():
    conv_frame.destroy()
    global pressure_frame
    pressure_frame = Frame(page, bg="grey")
    pressure_frame.pack(padx=10, pady=10)
    Button(pressure_frame, text=" < Back ", font="bold", command=bck_pressure, bg="grey").pack(anchor=NW ,padx=10, pady=10)
    sec_frame = Frame(pressure_frame)
    sec_frame.pack(padx=10, pady=10)
    min_frame = Frame(pressure_frame)
    min_frame.pack(padx=10, pady=10)
    ans_frame = LabelFrame(pressure_frame, text="Answer")
    ans_frame.pack(padx=10, pady=10)
    def wrk():
        ck = clicked.get()
        ck1 = clicked2.get()
        try:
            num = int(frm_ent.get())
            if ck == "Pounds/square_foot" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Pounds/square_foot" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) / int(144)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) / int(2.78449561149)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Bar":
                con = ("=")
                summ = int(num) / int(2089)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) / int(70.726)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) / int(2.088543512)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(2.088543512)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(2116.21728544)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) / int(20.88543512)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_foot" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(20885.43512)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Pounds/square_inch" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(144)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Pounds/square_inch" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(51.7149)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Bar":
                con = ("=")
                summ = int(num) / int(14.503774)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) * int(2.036)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(68.948)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(68.948)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(14.695952977)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) * int(6.8948)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Pounds/square_inch" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(145.03774)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Millimeter_of_mercury" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(2.784496)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Millimeter_of_mercury" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) / int(51.71493295)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Bar":
                con = ("=")
                summ = int(num) / int(750.0617)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) / int(25.39998984)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(1.3332237)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(1.3332237)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(760)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) / int(7.500617)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millimeter_of_mercury" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(7500.617)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Bar" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(2088.54)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Bar" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) * int(14.5038)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(750.0617)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Bar":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) * int(29.53)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(1.0132502738)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) * int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Bar" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Inch_of_mercury" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(70.726)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Inch_of_mercury" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) / int(2.036021)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(25.3999898)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Bar":
                con = ("=")
                summ = int(num) / int(29.53)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(33.863867)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(33.863867)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(29.921280586)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) * int(3.3863867)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Inch_of_mercury" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(295.3)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Millibar" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(2.08854)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Millibar" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) / int(68.94757185)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(1.33322365)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Bar":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) / int(33.86386725)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(1013.25027)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Millibar" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Hectopascal" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(2.08854)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Hectopascal" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) / int(68.94757185)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(1.33322365)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Bar":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) / int(33.86386725)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(1013.25027)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) / int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Hectopascal" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Standard_atmosphere" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(2116.217285)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Standard_atmosphere" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) * int(14.69595)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(760)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Bar":
                con = ("=")
                summ = int(num) * int(1.01325)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) * int(29.92128)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(1013.25)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(1013.25)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) * int(101.325)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Standard_atmosphere" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(9.86923)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Kilopascal" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(20.88543512)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Kilopascal" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) / int(6.8947571853)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(7.500617)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Bar":
                con = ("=")
                summ = int(num) / int(100)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) / int(3.386386725)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) / int(101.32502732)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Kilopascal" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) / int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
    #
            elif ck == "Megapascal" and ck1 == "Pounds/square_foot":
                con = ("=")
                summ = int(num) * int(20885.43512)
                tt = (num,con,summ)
                ans.config(text=tt) 
            elif ck == "Megapascal" and ck1 == "Pounds/square_inch":
                con = ("=")
                summ = int(num) * int(145.03774)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Millimeter_of_mercury":
                con = ("=")
                summ = int(num) * int(7500.617)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Bar":
                con = ("=")
                summ = int(num) * int(10)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Inch_of_mercury":
                con = ("=")
                summ = int(num) * int(295.3)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Millibar":
                con = ("=")
                summ = int(num) * int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Hectopascal":
                con = ("=")
                summ = int(num) * int(10000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Standard_atmosphere":
                con = ("=")
                summ = int(num) * int(9.86923)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Kilopascal":
                con = ("=")
                summ = int(num) * int(1000)
                tt = (num,con,summ)
                ans.config(text=tt)
            elif ck == "Megapascal" and ck1 == "Megapascal":
                con = ("=")
                summ = int(num) * int(1)
                tt = (num,con,summ)
                ans.config(text=tt)
            else:
                messagebox.showinfo("Error", "Please enter a number: ")
        except:
            messagebox.showinfo("Error", "Please enter a number: ")
            bck_pressure()
            pressure()

    label = Label(min_frame, text="Number to be converted: ", font="bold")
    label.pack(padx=10, pady=10)
    ent1 = int()
    frm_ent = Entry(min_frame, textvariable=ent1, width=20)
    frm_ent.pack(padx=10, pady=10)
    clicked = StringVar()
    clicked.set(pressure_space[0])
    opt = OptionMenu(sec_frame,clicked , *pressure_space)
    opt.grid(row=0, column=0, padx=10, pady=10)
    lb = Label(sec_frame, text=" TO ", font="bold")
    lb.grid(row=0, column=1, padx=10, pady=10)
    clicked2 = StringVar()
    clicked2.set(pressure_space[0])
    opt_to = OptionMenu(sec_frame, clicked2, *pressure_space)
    opt_to.grid(row=0, column=2, padx=10, pady=10)
    btn = Button(min_frame, text="Convert", command=wrk).pack(padx=10, pady=10)
    txt = "Answer"
    ans = Label(ans_frame, text=txt,  font=("helvetica", 18, "bold"), width=30, height=2, bg="mistyrose")
    ans.pack(padx=10, pady=10)

def conv():
    optn_frame.destroy()
    global conv_frame
    conv_frame = Frame(page, bg="grey")
    conv_frame.pack(padx=10, pady=10)
    Button(conv_frame, text=" < Back ", font="bold", command=bck2, bg="grey").pack(anchor=NW , padx=10, pady=10)
    pg_frame = Frame(conv_frame, bg="grey")
    pg_frame.pack(padx=10, pady=10)
    Button(pg_frame, text="Length conv", font="bold", width=15, height=1,command=leng , bg="grey").pack(padx=10, pady=10)
    Button(pg_frame, text="Area conv", font="bold", width=15, height=1,command=area , bg="grey").pack(padx=10, pady=10)
    Button(pg_frame, text="Volume conv", font="bold", width=15, height=1,command=vol , bg="grey").pack(padx=10, pady=10)
    Button(pg_frame, text="Speed conv", font="bold", width=15, height=1,command=speed , bg="grey").pack(padx=10, pady=10)
    Button(pg_frame, text="Weight conv", font="bold", width=15, height=1,command=weight , bg="grey").pack(padx=10, pady=10)
    Button(pg_frame, text="Temperature conv", font="bold", width=15, height=1,command=temp , bg="grey").pack(padx=10, pady=10)
    Button(pg_frame, text="Power conv", font="bold", width=15, height=1,command=power , bg="grey").pack(padx=10, pady=10)
    Button(pg_frame, text="Pressure conv", font="bold", width=15, height=1,command=pressure , bg="grey").pack(padx=10, pady=10)

def frame1():
    global main_frame
    main_frame = Frame(page)
    main_frame.pack(padx=10, pady=10)
    mn_label = Label(main_frame, text=" * CALCULATOR * ", font=("buffalo",18,"bold"), bg="grey51")
    mn_label.pack(padx=5, pady=10)

    ## Function
    def plus():
        try:
            num1 = int(ent_1.get())
            num2 = int(ent_2.get())
            global sum2
            sum2 = num1 + num2
            text=(num1,"+",num2,"=", sum2)
            txt = text
            ans_lab.config(text=txt)
            def rite():
                file = open("math.txt","a")
                file.write(str(num1))
                file.write(" + ")
                file.write(str(num2))
                file.write(" = ")
                file.write(str(sum2))
                file.write("\n")
                file.close()
            rite()
            def rel():
                ent_1.delete(0, END)
                ent_1.insert(END, sum2)
            def rel_1():
                ent_2.delete(0, END)
                ent_2.insert(END, sum2)    
            Button(btn_frame, text="Ans ent 1", font="bold", width=10, height=1, command=rel, bg="silver").grid(row=1, column=0, padx=10, pady=10)
            Button(btn_frame, text="Ans ent 2", font="bold", width=10, height=1, command=rel_1, bg="silver").grid(row=2, column=0, padx=10, pady=10)
        except:
            messagebox.showinfo("ERROR", "Plz insert Number !")
            ent_1.delete(0, END)
            ent_2.delete(0, END)    
    
    def sub():
        try:
            num1 = int(ent_1.get())
            num2 = int(ent_2.get())
            global dec
            dec = num1 - num2
            text=(num1,"-",num2,"=", dec)
            txt = text 
            ans_lab.config(text=txt)
            def rite():
                file = open("math.txt","a")
                file.write(str(num1))
                file.write(" - ")
                file.write(str(num2))
                file.write(" = ")
                file.write(str(dec))
                file.write("\n")
                file.close()
            rite()

            def rel():
                ent_1.delete(0, END)
                ent_1.insert(END, dec)
            def rel_1():
                ent_2.delete(0, END)
                ent_2.insert(END, dec)
    
            Button(btn_frame, text="Ans ent 1", font="bold", width=10, height=1, command=rel, bg="silver").grid(row=1, column=1, padx=10, pady=10)
            Button(btn_frame, text="Ans ent 2", font="bold", width=10, height=1, command=rel_1, bg="silver").grid(row=2, column=1, padx=10, pady=10)
        except:
            messagebox.showinfo("ERROR", "Plz insert Number !")
            ent_1.delete(0, END)
            ent_2.delete(0, END)  

    def div():
        try:
            num1 = int(ent_1.get())
            num2 = int(ent_2.get())
            global divi
            divi = num1 / num2
            text=(num1,"÷",num2,"=", divi)
            txt = text
            ans_lab.config(text=txt)
            def rite():
                file = open("math.txt","a")
                file.write(str(num1))
                file.write(" ÷ ")
                file.write(str(num2))
                file.write(" = ")
                file.write(str(divi))
                file.write("\n")
                file.close()
            rite()

            def rel():
                ent_1.delete(0, END)
                ent_1.insert(END, divi)
            def rel_1():
                ent_2.delete(0, END)
                ent_2.insert(END, divi)
    
            Button(btn_frame, text="Ans ent 1", font="bold", width=10, height=1, command=rel, bg="silver").grid(row=1, column=2, padx=10, pady=10)
            Button(btn_frame, text="Ans ent 2", font="bold", width=10, height=1, command=rel_1, bg="silver").grid(row=2, column=2, padx=10, pady=10)
        except:
            messagebox.showinfo("ERROR", "Plz insert Number !")
            ent_1.delete(0, END)
            ent_2.delete(0, END)

    def multi():
        try:
            num1 = int(ent_1.get())
            num2 = int(ent_2.get())
            global mult
            mult = num1 * num2
            text=(num1,"x",num2,"=", mult)
            txt = text
            ans_lab.config(text=txt)
            def rite():
                file = open("math.txt","a")
                file.write(str(num1))
                file.write(" x ")
                file.write(str(num2))
                file.write(" = ")
                file.write(str(mult))
                file.write("\n")
                file.close()
            rite()

            def rel():
                ent_1.delete(0, END)
                ent_1.insert(END, mult)
            def rel_1():
                ent_2.delete(0, END)
                ent_2.insert(END, mult)
    
            Button(btn_frame, text="Ans ent 1", font="bold", width=10, height=1, command=rel, bg="silver").grid(row=1, column=3, padx=10, pady=10)
            Button(btn_frame, text="Ans ent 2", font="bold", width=10, height=1, command=rel_1, bg="silver").grid(row=2, column=3, padx=10, pady=10)
        except:
            messagebox.showinfo("ERROR", "Plz insert Number !")
            ent_1.delete(0, END)
            ent_2.delete(0, END)    
    
    def clear():
        ent_1.delete(0, END)
        ent_2.delete(0, END)
    
    def close():
        page.destroy()
    

    ## Placement

    pg_fme = Frame(main_frame)
    pg_fme.pack(padx=10, pady=10)

    main_fme = Frame(pg_fme)
    main_fme.pack()

    btn_frame = Frame(main_frame)
    btn_frame.pack(padx=10, pady=10)

    ans_fme = LabelFrame(main_frame, text="Answer", font=("buffalo",12, "bold"))
    ans_fme.pack(padx=10, pady=10)
    txt = "Answer"
    ans_lab = Label(ans_fme, text=txt, font=("helvetica", 18, "bold"), width=30, height=2, bg="darkorange2")
    ans_lab.pack(padx=10, pady=10)

    ent_1_label = Label(main_fme, text="Enter first number :", font="bold")
    ent_1_label.grid(row=0, column=0, padx=10, pady=10)
    ent_1 = Entry(main_fme, width=30)
    ent_1.grid(row=0, column=1, padx=10, pady=10)

    ent_2_label = Label(main_fme, text="Enter second number :", font="bold")
    ent_2_label.grid(row=1, column=0, padx=10, pady=10)
    ent_2 = Entry(main_fme, width=30)
    ent_2.grid(row=1, column=1, padx=10, pady=10)
    
    ##  Button
    Button(btn_frame, text=" + ", font=("helvetica", 11, "bold"), width=10, height=1, command=plus, bg="gold").grid(row=0, column=0, padx=10, pady=10)
    Button(btn_frame, text=" ÷ ", font=("helvetica", 11, "bold"), width=10, height=1, command=div, bg="gold").grid(row=0, column=2, padx=10, pady=10)
    Button(btn_frame, text=" - ", font=("helvetica", 11, "bold"), width=10, height=1, command=sub, bg="gold").grid(row=0, column=1, padx=10, pady=10)
    Button(btn_frame, text=" x ", font=("helvetica", 11, "bold"), width=10, height=1, command=multi, bg="gold").grid(row=0, column=3, padx=10, pady=10)
    Button(btn_frame, text="CLEAR", font=("helvetica", 11, "bold"),width=10, height=1, command=clear, bg="red").grid(row=3, column=1, padx=10, pady=10)
    Button(btn_frame, text="CLOSE", font=("helvetica", 11, "bold"),width=10, height=1, command=close, bg="red").grid(row=3, column=2, padx=10, pady=10)
    Button(btn_frame, text="History", font=("helvetica", 11, "bold"), width=10, height=1,command=hist_pg, bg="purple").grid(row=3, column=0,padx=10, pady=10)    
    Button(btn_frame, text="Options", font=("helvetica", 11, "bold"), width=10, height=1, command=options, bg="purple").grid(row=3, column=3, padx=10, pady=10)
    
def frame2():
    global optn_frame
    optn_frame = Frame(page, bg="grey")
    optn_frame.pack(padx=10, pady=10)
    Button(optn_frame, text=" < Back", font=("bold"),bg="grey" , command=bck).pack(anchor=NW ,padx=10, pady=10)
    fit_frame = Frame(optn_frame, bg="grey")
    fit_frame.pack(padx=10, pady=10)
    btn_frame = Frame(fit_frame, bg="grey")
    btn_frame.pack(padx=10, pady=10)
    Button(btn_frame, text="Conversion", width=30, height=1, font=("helvetica", 11, "bold"), bg="silver", command=conv).pack(padx=10, pady=10)

def frame3():
    global hist_frame
    hist_frame = Frame(page)
    hist_frame.pack(padx=10, pady=10)
    hist_frame.config(bg="grey")
    Button(hist_frame, text=" < Back", font="bold", bg="grey", command=bck1).pack(anchor=NW, padx=10,pady=10)
    staff_fme = Frame(hist_frame)
    staff_fme.config(bg="grey")
    staff_fme.pack(padx=10, pady=10)
    def rite():
        file = open("math.txt","w")
        file.write(file_text.get(1.0, END))
        file.close()

    
    Label(staff_fme, text="CALCULATOR HISTORY", font=("buffalo", 15 , "bold"),bg="silver").pack(anchor=CENTER, padx=10, pady=10)
    file_text = Text(staff_fme, width=40, height=10, font=("Helvetica",16,"bold"))
    file_text.pack(padx=10, pady=10)
    file_mod = open("math.txt", "r")
    read = file_mod.read()
    file_text.insert(END, read)
    file_mod.close()
    Button(staff_fme, text="Save", font=("helvetica", 11, "bold"), width=10, height=1, command=rite, bg="silver").pack(padx=10, pady=10)

def options():
    main_frame.destroy()
    frame2()

def hist_pg():
    main_frame.destroy()
    frame3()

def bck():
    optn_frame.destroy()
    frame1()

def bck1():
    hist_frame.destroy()
    frame1()

def bck2():
    conv_frame.destroy()
    options()

def bck_leng():
    len_frame.destroy()
    conv()

def bck_area():
    area_frame.destroy()
    conv()

def bck_vol():
    vol_frame.destroy()
    conv()

def bck_speed():
    speed_frame.destroy()
    conv()

def bck_weight():
    weight_frame.destroy()
    conv()

def bck_temp():
    temp_frame.destroy()
    conv()

def bck_power():
    power_frame.destroy()
    conv()

def bck_pressure():
    pressure_frame.destroy()
    conv()

frame1()

page.mainloop()