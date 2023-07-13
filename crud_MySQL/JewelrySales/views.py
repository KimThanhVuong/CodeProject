from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.apps import apps
import pymysql
from datetime import date

from JewelrySales.forms import CarForm

# Create your views here.
def home(request):
    return render(request, 'HomePage.html')

def dangky(request):
    return render(request, 'dangky.html')
def quenmatkhau(request):
    return render(request, 'quenmatkhau.html')

def admin(request):
    return render(request, 'admin.html')

def muasp(request):
    return render(request, 'muasp.html')
def shopingcart(request):
    return render(request, 'shopingcart.html')
def hoadon(request):
    return render(request, 'hoadon.html')

def huongdandosize(request):
    return render(request, 'huongdandosize.html')
def khuyenmai(request):
    return render(request,'khuyenmai.html')
def trangsuc(request):
    return render(request, 'trangsuc.html')
def dichvu(request):
    return render(request, 'dichvu.html')
def gioithieuvalienhe(request):
    return render(request, 'gioithieuvalienhe.html')

def connection():
    s = '127.0.0.1'
    d = 'carsales'
    u = 'root'
    p = ''
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

def carslist(request):
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TblCars")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    return render(request, 'carslist.html', {'cars':cars})

def addcar(request):
    if request.method == 'GET':
        return render(request, 'addcar.html')
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            name = form.cleaned_data.get("name")
            year = form.cleaned_data.get("year")
            price = form.cleaned_data.get("price")
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblCars (id, name, year, price) VALUES (%s, %s, %s, %s)", (id, name, year, price))
        conn.commit()
        conn.close()
        return redirect('carslist')
        return render(request, 'addcar.html', {'car':{}})
        
def updatecar(request, id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM TblCars WHERE id = %s", (id))
        for row in cursor.fetchall():

            cr.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
        conn.close()
        return render(request, 'addcar.html', {'car':cr[0]})
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data.get("name"))
            year = int(form.cleaned_data.get("year"))
            price = float(form.cleaned_data.get("price"))
            cursor.execute("UPDATE TblCars SET name = %s, year = %s, price = %s WHERE id = %s", (name, year, price, id))
            conn.commit()
        conn.close()
        return redirect('carslist')

def deletecar(request, id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TblCars WHERE id = %s", (id))
    conn.commit()
    conn.close()
    return redirect('carslist') 