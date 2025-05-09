<img src = "https://raw.githubusercontent.com/Faris4166/Simple-Checklist-Application-in-Python/refs/heads/main/BG.jpg">


# 🧮 เครื่องคิดเลข GUI ด้วย Python Tkinter

โปรเจกต์นี้เป็นเครื่องคิดเลขแบบกราฟิก (GUI) ที่สร้างด้วยไลบรารี Tkinter ของ Python 🐍 ทำให้ผู้ใช้สามารถทำการคำนวณพื้นฐานได้อย่างง่ายดายบนหน้าต่างเดสก์ท็อป 💻

## ✨ คุณสมบัติหลัก

* ➕ **การบวก:** สามารถบวกตัวเลขสองจำนวนเข้าด้วยกัน
* ➖ **การลบ:** สามารถลบตัวเลขหนึ่งออกจากอีกจำนวนหนึ่ง
* ✖️ **การคูณ:** สามารถคูณตัวเลขสองจำนวนเข้าด้วยกัน
* ➗ **การหาร:** สามารถหารตัวเลขหนึ่งด้วยอีกจำนวนหนึ่ง (มีการจัดการข้อผิดพลาดเมื่อหารด้วยศูนย์ 🚫)
* ^ **ยกกำลัง:** สามารถยกกำลังตัวเลขด้วยตัวเลขอื่น
* ² **ยกกำลังสอง:** คำนวณผลลัพธ์ของการยกกำลังสองของตัวเลข
* ¹/ₓ **ส่วนกลับ:** คำนวณส่วนกลับของตัวเลข (1 หารด้วยตัวเลขนั้น)
* +/- **เปลี่ยนเครื่องหมาย:** เปลี่ยนเครื่องหมายของตัวเลขที่แสดงอยู่ (จากบวกเป็นลบ หรือจากลบเป็นบวก)
* .** ทศนิยม:** อนุญาตให้ป้อนตัวเลขทศนิยม
* **C ล้าง:** ล้างตัวเลขและผลลัพธ์ที่แสดงบนหน้าจอ
* **Quit ออก:** ปิดแอปพลิเคชันเครื่องคิดเลข

## ⚙️ โครงสร้างโค้ด

โค้ดนี้ถูกสร้างขึ้นโดยใช้ไลบรารี Tkinter ซึ่งเป็นเครื่องมือมาตรฐานสำหรับสร้าง GUI ใน Python มาดูรายละเอียดของแต่ละส่วนกันครับ:

1.  **การนำเข้าไลบรารี:**
    ```python
    from tkinter import *
    ```
    บรรทัดนี้จะนำเข้าทุกสิ่งทุกอย่างจากโมดูล `tkinter` ซึ่งจำเป็นสำหรับการสร้าง GUI

2.  **การสร้างหน้าต่างหลัก:**
    ```python
    root = Tk()
    root.title("Calculator")
    root.iconbitmap("icon/calculator.ico")
    root.geometry("310x530")
    root.resizable(0, 0)
    ```
    * `root = Tk()`: สร้างอินสแตนซ์ของหน้าต่างหลักของแอปพลิเคชัน
    * `root.title("Calculator")`: กำหนดชื่อที่แสดงบนแถบชื่อของหน้าต่างเป็น "Calculator"
    * `root.iconbitmap("icon/calculator.ico")`: กำหนดไอคอนสำหรับหน้าต่าง (หากมีไฟล์ `calculator.ico` ในโฟลเดอร์ `icon`)
    * `root.geometry("310x530")`: กำหนดขนาดเริ่มต้นของหน้าต่างเป็น 310 พิกเซล (กว้าง) x 530 พิกเซล (สูง)
    * `root.resizable(0, 0)`: ปิดการปรับขนาดหน้าต่างทั้งในแนวนอนและแนวตั้ง

3.  **ฟังก์ชันการทำงาน:**
    * `negate()`:
        ```python
        def negate():
            result=float(display.get()) *-1
            display.delete(0,END)
            display.insert(0,result)
        ```
        ฟังก์ชันนี้จะอ่านค่าจากช่องแสดงผล (`display`) แปลงเป็น float แล้วคูณด้วย -1 เพื่อเปลี่ยนเครื่องหมาย จากนั้นจะล้างค่าเดิมและแสดงผลลัพธ์ใหม่

    * `square()`:
        ```python
        def square():
            result=float(display.get()) ** 2
            display.delete(0,END)
            display.insert(0,result)
        ```
        ฟังก์ชันนี้จะอ่านค่าจากช่องแสดงผล ยกกำลังสอง และแสดงผลลัพธ์

    * `inverse()`:
        ```python
        def inverse():
            if display.get()=="0":
                result = "ERROR"
            else:
                result = 1 / float(display.get())
            display.delete(0,END)
            display.insert(0,result)
        ```
        ฟังก์ชันนี้จะคำนวณส่วนกลับของตัวเลข หากตัวเลขเป็น 0 จะแสดงข้อผิดพลาด "ERROR"

    * `clearDisplay()`:
        ```python
        def clearDisplay():
            display.delete(0,END)
            enableOperator()
        ```
        ฟังก์ชันนี้จะล้างข้อความทั้งหมดในช่องแสดงผล และเรียกใช้ฟังก์ชัน `enableOperator()` เพื่อเปิดใช้งานปุ่มตัวดำเนินการอีกครั้ง

    * `showNumber(number)`:
        ```python
        def showNumber(number):
            display.insert(END,number)
            if "." in display.get():
                btnDecimal.config(state=DISABLED)
        ```
        ฟังก์ชันนี้จะเพิ่มตัวเลขที่ระบุลงในช่องแสดงผล และหากมีจุดทศนิยมอยู่แล้ว จะปิดใช้งานปุ่มทศนิยมเพื่อป้องกันการป้อนจุดทศนิยมซ้ำ

    * `equal()`:
        ```python
        def equal():
            if operator=="add":
                result = float(firstNumber) + float(display.get())
            elif operator=="subtract":
                result = float(firstNumber) - float(display.get())
            elif operator=="multiply":
                result = float(firstNumber) * float(display.get())
            elif operator=="divide":
                if display.get()=="0":
                    result="ERROR"
                else:
                    result = float(firstNumber) / float(display.get())
            elif operator=="exponent":
                result = float(firstNumber) ** float(display.get())

            display.delete(0,END)
            display.insert(0,result)
            enableOperator()
        ```
        ฟังก์ชันนี้จะทำการคำนวณตามตัวดำเนินการ (`operator`) ที่ถูกเลือกไว้ก่อนหน้า โดยใช้ค่า `firstNumber` และค่าปัจจุบันในช่องแสดงผล จากนั้นจะแสดงผลลัพธ์และเปิดใช้งานปุ่มตัวดำเนินการ

    * `operation(value)`:
        ```python
        def operation(value):
            global firstNumber
            global operator
            operator = value
            firstNumber = display.get()
            btnDecimal.config(state=NORMAL)
            display.delete(0,END)

            btnAdd.config(state=DISABLED)
            btnSubtract.config(state=DISABLED)
            btnMultiply.config(state=DISABLED)
            btnDivide.config(state=DISABLED)
            btnExponent.config(state=DISABLED)
            btnInverse.config(state=DISABLED)
            btnSquare.config(state=DISABLED)
        ```
        ฟังก์ชันนี้จะถูกเรียกเมื่อมีการคลิกปุ่มตัวดำเนินการ (+, -, x, / , ^) มันจะเก็บค่าแรก (`firstNumber`) และตัวดำเนินการ (`operator`) ที่เลือกไว้ จากนั้นจะล้างช่องแสดงผลและปิดใช้งานปุ่มตัวดำเนินการชั่วคราว

    * `enableOperator()`:
        ```python
        def enableOperator():
            btnAdd.config(state=NORMAL)
            btnSubtract.config(state=NORMAL)
            btnMultiply.config(state=NORMAL)
            btnDivide.config(state=NORMAL)
            btnExponent.config(state=NORMAL)
            btnInverse.config(state=NORMAL)
            btnSquare.config(state=NORMAL)
            btnDecimal.config(state=NORMAL)
        ```
        ฟังก์ชันนี้จะเปิดใช้งานปุ่มตัวดำเนินการทั้งหมด รวมถึงปุ่มทศนิยม

4.  **การกำหนดสีและฟอนต์:**
    ```python
    color = "#F79B72"
    displayFont = ("Kanit", 35)
    btnFont = ("Kanit", 19)
    ```
    ส่วนนี้กำหนดสีพื้นหลังสำหรับปุ่มตัวดำเนินการ และฟอนต์สำหรับข้อความในช่องแสดงผลและบนปุ่ม (ใช้ฟอนต์ "Kanit" ขนาด 35 และ 19 ตามลำดับ)

5.  **การสร้างเฟรม:**
    ```python
    displayFrame = LabelFrame(root)
    buttonFrame = LabelFrame(root)
    displayFrame.pack(padx=2, pady=5)
    buttonFrame.pack(padx=2)
    ```
    มีการสร้างสองเฟรมหลัก: `displayFrame` สำหรับช่องแสดงผล และ `buttonFrame` สำหรับปุ่มต่างๆ จากนั้นจึงจัดวางเฟรมเหล่านี้ในหน้าต่างหลัก

6.  **การสร้างและจัดวางวิดเจ็ต (Widgets):**
    * **ช่องแสดงผล:**
        ```python
        display = Entry(displayFrame, width=30, font=displayFont, bg="#2A4759", fg="#EEEEEE", border=5, justify=RIGHT)
        display.pack(padx=5, pady=5)
        ```
        สร้างช่องสำหรับแสดงตัวเลขและผลลัพธ์ โดยมีการกำหนดคุณสมบัติเช่น ความกว้าง ฟอนต์ สีพื้นหลัง สีตัวอักษร ขอบ และการจัดวางข้อความ

    * **ปุ่ม Clear และ Quit:**
        ```python
        btnClear = Button(buttonFrame, text="Clear", font=btnFont, command=clearDisplay)
        btnQuit = Button(buttonFrame, text="Quit", font=btnFont, command=root.destroy)
        btnClear.grid(row=0, column=0, columnspan=2, ipadx=30, sticky="WE")
        btnQuit.grid(row=0, column=2, columnspan=2, ipadx=30, sticky="WE")
        ```
        สร้างปุ่ม "Clear" และ "Quit" พร้อมกำหนดฟอนต์และคำสั่งเมื่อคลิก (`clearDisplay` และ `root.destroy`) จากนั้นจัดวางโดยใช้ `grid` layout manager

    * **ปุ่มตัวดำเนินการและฟังก์ชันพิเศษ:**
        ```python
        btnInverse  = Button(buttonFrame, text="1/x", font=btnFont, bg=color, command=inverse)
        btnSquare   = Button(buttonFrame, text="x^2", font=btnFont, bg=color, command=square)
        btnExponent = Button(buttonFrame, text="x^n", font=btnFont, bg=color, command=lambda: operation("exponent"))
        btnDivide   = Button(buttonFrame, text="/", font=btnFont, bg=color, command=lambda: operation("divide"))
        btnMultiply = Button(buttonFrame, text="x", font=btnFont, bg=color, command=lambda: operation("multiply"))
        btnSubtract = Button(buttonFrame, text="-", font=btnFont, bg=color, command=lambda: operation("subtract"))
        btnAdd      = Button(buttonFrame, text="+", font=btnFont, bg=color, command=lambda: operation("add"))
        btnEqual    = Button(buttonFrame, text="=", font=btnFont, bg=color, command=equal)
        btnDecimal  = Button(buttonFrame, text=".", font=btnFont, bg=color, command=lambda: showNumber("."))
        btnNegate   = Button(buttonFrame, text="+/-", font=btnFont, bg=color, command=negate)
        ```
        สร้างปุ่มสำหรับตัวดำเนินการต่างๆ และฟังก์ชันพิเศษ พร้อมกำหนดฟอนต์ สีพื้นหลัง และคำสั่งเมื่อคลิก

    * **ปุ่มตัวเลข:**
        ```python
        btn9 = Button(buttonFrame, text="9", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(9))
        # ... ปุ่มอื่นๆ สำหรับตัวเลข 8 ถึง 0 ก็มีลักษณะคล้ายกัน
        ```
        สร้างปุ่มสำหรับตัวเลข 9 ถึง 0 พร้อมกำหนดฟอนต์ สีพื้นหลัง สีตัวอักษร และคำสั่งเมื่อคลิก (`showNumber()`)

    * **การจัดวางปุ่มด้วย `grid`:**
        ส่วนนี้ใช้ `grid` layout manager เพื่อจัดวางปุ่มต่างๆ ใน `buttonFrame` โดยกำหนดแถว (`row`) และคอลัมน์ (`column`) รวมถึงการกำหนดการขยายตัว (`sticky`) และระยะห่าง (`padx`, `pady`, `ipadx`)

7.  **การรันแอปพลิเคชัน:**
    ```python
    root.mainloop()
    ```
    บรรทัดสุดท้ายนี้จะเริ่ม event loop ของ Tkinter ซึ่งทำให้แอปพลิเคชัน GUI ทำงานและตอบสนองต่อการกระทำของผู้ใช้

## 🚀 วิธีการใช้งาน

1.  **ติดตั้ง Python:** หากยังไม่มี Python ในเครื่อง โปรดติดตั้งจาก [เว็บไซต์ Python อย่างเป็นทางการ](https://www.python.org/downloads/)
2.  **บันทึกโค้ด:** คัดลอกโค้ดด้านบนและบันทึกลงในไฟล์ชื่อ `calculator.py`
3.  **(Optional) สร้างโฟลเดอร์ `icon`:** หากต้องการให้มีไอคอนปรากฏบนหน้าต่าง ให้สร้างโฟลเดอร์ชื่อ `icon` ในไดเรกทอรีเดียวกับไฟล์ `calculator.py` และนำไฟล์ไอคอน (เช่น `calculator.ico`) มาใส่ไว้
4.  **รันแอปพลิเคชัน:** เปิดเทอร์มินัลหรือ command prompt ไปที่ไดเรกทอรีที่บันทึกไฟล์ `calculator.py` แล้วรันคำสั่ง `python calculator.py`
5.  **ใช้งานเครื่องคิดเลข:** หน้าต่างเครื่องคิดเลขจะปรากฏขึ้น คุณสามารถคลิกปุ่มต่างๆ เพื่อทำการคำนวณได้เลย! 🎉

## 🙏 ขอบคุณครับ

หวังว่าคำอธิบายนี้จะเป็นประโยชน์นะครับ! หากมีคำถามเพิ่มเติม สามารถสอบถามได้เลย 😊

---

<div align="center">
  <img src = "https://i.pinimg.com/originals/a6/a7/b2/a6a7b22f0204e0bd47ac1be00698395f.gif">
</div>
