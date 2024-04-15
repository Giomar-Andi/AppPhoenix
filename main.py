from asyncio.windows_events import NULL
import decimal
import re
from flask import Flask, flash, redirect, render_template, request, session, url_for,session
from flask_mysqldb import MySQL
from db.database import *
from controller.appPhoenix import*
from model.appUser import *

app=Flask(__name__)

mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name=request.form['txtname']
        pat=request.form['txtpat']
        mat=request.form['txtmat']
        phone=request.form['txtphone']
        email=request.form['txtmail']
        pswd=request.form['txtpass']
        #validar usuario duplicado#
        data=appPhoenix.val_duplicar_usuario(mysql,name,pat,mat,phone,email)
        if data:
            flash("El usuario que acaba de crear no esta disponible o ya existe.",'error')
            return redirect(url_for('client'))
        else:  
            #registrar usuario#  
            appUser.registrar_usuario(mysql,name,pat,mat,phone,email,pswd)
            session['mail']=email
            flash(""+name+", Su cuenta a sido registrada exitosamente.",'success')
            print(session)
            return redirect(url_for("dashboard"))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['pswd']
        #validar login#
        data=appPhoenix.val_login(mysql,email,password)
        if data: 
            session['mail']=email
            flash(""+email+", ¿Que lo trae por aca esta vez?.",'success')
            print(session)
            return redirect(url_for("dashboard"))
        else:
            flash("Usted ingresó un correo o contraseña invalida.",'error')  
            return redirect(url_for("client"))
    else: 
        if 'mail' in session: 
            return redirect(url_for("dashboard"))
        return redirect(url_for("client"))   

@app.route('/logout')
def logout():
    print(session)
    session.clear()
    flash("Su sesion se ha cerrado correctamente, vuelva pronto.",'info')
    print(session)
    return redirect(url_for("login"))

@app.route('/dashboard')
def dashboard():
    if 'mail' in session:
        email=session['mail']
        #mostrar recordatorios#
        data=appPhoenix.call_recordatorios(mysql,email)
        #mostrar cuentas#
        data2=appPhoenix.call_cuentas(mysql,email)
        #mostrar saldo total#
        data3=appPhoenix.call_saldo_total(mysql,email)
        print(email)
        return render_template('dashboard.html',data=data,data2=data2,data3=data3,email=email)
    return redirect(url_for('client'))

@app.route('/client')
def client():
    if 'mail' in session:
        return redirect(url_for('dashboard'))
    return render_template('client.html')

@app.route('/operaciones')
def operaciones():
      if 'mail' in session:
          email=session['mail']
          #mostrar movimientos#
          data=appPhoenix.call_movimientos(mysql,email)
          #mostrar cuentas#
          data2=appPhoenix.call_cuentas(mysql,email)
          #mostrar beneficiarios#
          data3=appPhoenix.call_beneficiarios(mysql)
          print(email)
          return render_template('operaciones.html',data=data,data2=data2,data3=data3,email=email)
      return redirect(url_for('client'))

@app.route('/transferencias')
def transferencias():
    if 'mail' in session:
        email=session['mail']
        #mostrar cuentas#
        data=appPhoenix.call_cuentas(mysql, email)
        #mostrar transferencias#
        data2=appPhoenix.call_transferencias(mysql, email)
        print(email)
        return render_template('transferencias.html',email=email,data=data,data2=data2)
    return redirect(url_for('client'))

@app.route('/insert_trans',methods=['POST'])
def insert_trans():
    if request.method =='POST':
        orig=request.form['origen']
        dest=request.form['destino']
        desc=request.form['descripcion']
        monto=request.form['monto']
        mon=request.form['moneda']
        if mon=='2':
            print(monto)
            monto=float(monto)*3.71
            print(monto)
        else:
            monto=monto
        fech=request.form['fecha']
        #transferencia de dinero#
        appUser.transferir_dinero(mysql,orig,monto)
        #registrar transferencia#
        appUser.registrar_transferencia(mysql,orig,dest,desc,monto,mon,fech)
        flash("Transferencia realizada de manera exitosa.",'success')
        return redirect(url_for('transferencias'))

@app.route('/delete_transferencias/<int:id>')
def delete_transferencias(id):
    #eliminar registro de transferencia#
    appUser.eliminar_transferencia(mysql,id)
    return redirect(url_for('transferencias'))

@app.route('/insert_gasto',methods=['GET','POST'])
def insert_gasto():
    if request.method == 'POST': 
        cat=request.form['categoria']
        fec=request.form['fecha']
        ben=request.form['beneficiario']
        cue=request.form['cuenta']
        nom=request.form['nombre']
        mont=request.form['monto'] 
        mon=request.form['moneda']
        if mon=='2':
            print(mont)
            mont=float(mont)*3.71
            print(mont)
        else:
            mont=mont
        ope=request.form['operacion']
        if ope=='2':
            #restar saldo en tarjeta#  
            appUser.restar_saldo(mysql,cue,mont)
        else:
            #sumar saldo en tarjeta#
            appUser.sumar_saldo(mysql,cue,mont)
        #registrar operacion#
        appUser.registrar_gasto(mysql,ope,cue,cat,ben,mont,mon,nom,fec)
        flash("Operacion realizada exitosamente.","success")
        print(ope,cat,fec,ben,mont,mon,nom,cue)
        return redirect(url_for('operaciones'))              
        
@app.route('/delete_movimiento/<int:id>')
def delete_movimiento(id):
    #eliminar registro de operacion#
    appUser.eliminar_operacion(mysql,id)
    return redirect(url_for('operaciones'))

@app.route('/recordatorios')
def recordatorios():
    if 'mail' in session:
        email=session['mail']
        #mostrar recordatorios#
        data=appPhoenix.call_recordatorios(mysql, email)
        #mostrar cuentas#
        data2=appPhoenix.call_cuentas(mysql,email)
        #mostrar beneficiarios#
        data3=appPhoenix.call_beneficiarios(mysql)
        print(email)
        return render_template('recordatorios.html',data=data,data2=data2,data3=data3,email=email)
    return redirect(url_for('client'))    

@app.route('/insert_recordatorio',methods=['GET','POST'])
def insert_recordatorio():
    if request.method == 'POST':
        cuen=request.form['cuenta']
        bene=request.form['beneficiario']
        cate=request.form['categoria']
        desc=request.form['descripcion']
        oper=request.form['operacion']
        mont=request.form['monto']
        mone=request.form['moneda']
        if mone=='2':
            print(mont)
            mont=float(mont)*3.71
            print(mont)
        else:
            mont=mont
        pago=request.form['pago']
        frec=request.form['frecuencia']
        noti=request.form['notificacion']
        fech=request.form['fecha']
        #registrar recordatorio#
        appUser.registrar_recordatorio(mysql,cuen,oper,cate,mont,mone,pago,bene,frec,fech,noti,desc)
        flash('Recordatorio insertado exitosamente.','success')
        print(cuen,bene,cate,desc,oper,mone,pago,mont,frec,noti,fech,)
        return redirect(url_for('recordatorios'))

@app.route('/delete_recordatorio/<int:id>')
def delete_recordatorio(id):
    #eliminar registro de recordatorio#
    appUser.eliminar_recordatorio(mysql,id)
    return redirect(url_for('recordatorios'))

@app.route('/cuentas')
def cuentas():
    if 'mail' in session:
        email = session['mail']
        #mostrar cuentas#
        data=appPhoenix.call_cuentas(mysql,email)
        #mostrar usuario#
        data2=appPhoenix.call_usuario(mysql,email)
        print(email)
        return render_template('cuentas.html',data=data,data2=data2,email=email)
    return redirect(url_for('client'))    

@app.route('/insert_cuenta',methods=['GET','POST'])
def insert_cuenta():
    if request.method == 'POST':
        user=request.form['user']
        prop=request.form['propietario']
        tar=request.form['tarjeta']
        mes=request.form['mes']
        year=request.form['año']
        cvv=request.form['cvv']
        ban=request.form['banco']
        mont=request.form['monto']
        #validar cuenta duplicada#
        data=appPhoenix.val_duplicar_cuenta(mysql,tar)
        if data:
            flash('Cuenta con numero de tarjeta existente.','error') 
            return redirect(url_for('cuentas'))
        else: 
            #registrar cuenta#
            appUser.registrar_cuenta(mysql,user,prop,ban,tar,mes,year,cvv,mont)
            flash("Su cuenta a sido afiliada exitosamente.",'success')
            return redirect(url_for('cuentas'))
    
@app.route('/delete_cuenta',methods=['POST'])
def delete_cuenta():
    if request.method == 'POST':
        id=request.form['id']
        #eliminar cuenta#
        appUser.eliminar_cuenta(mysql,id)
        return redirect(url_for('cuentas'))

@app.route('/ajustes')
def ajustes():
    if 'mail' in session:
        email = session['mail']
        #mostrar usuario#
        data=appPhoenix.call_usuario(mysql,email)
        print(email)
        return render_template('ajustes.html',email=email,data=data)
    return redirect(url_for('client'))

@app.route('/update_user',methods=['GET','POST'])
def update_user():
    if request.method == 'POST':
        id=request.form['id']
        name=request.form['name']
        apat=request.form['apepat']
        amat=request.form['apemat']
        phone=request.form['phone']
        mail=request.form['mail']
        pswd=request.form['pswd']
        #actualizar datos de usuario#
        appUser.actualizar_usuario(mysql,id,name,apat,amat,phone,mail,pswd)
        flash("Su cuenta de usuario a sido actualizada de manera exitosa.",'success')
        return redirect(url_for('ajustes'))

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run(port=3000)    