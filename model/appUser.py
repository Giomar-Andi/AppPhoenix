from db.database import *

class appUser:

    @classmethod
    def registrar_usuario(self,mysql,name,pat,mat,phone,email,pswd):
        Exe.sentencia_commit(mysql,"call sp_signup('{0}','{1}','{2}','{3}','{4}','{5}');".format(name,pat,mat,phone,email,pswd))

    @classmethod
    def transferir_dinero(self,mysql,orig,monto):
        Exe.sentencia_commit(mysql,"call sp_update_cuenta({0},{1});".format(orig,monto))

    @classmethod
    def registrar_transferencia(self,mysql,orig,dest,desc,monto,mon,fech):
        Exe.sentencia_commit(mysql,"call sp_insert_trans({0},'{1}','{2}',{3},{4},'{5}');".format(orig, dest, desc, monto, mon,fech))    

    @classmethod
    def eliminar_transferencia(self,mysql,id):
        Exe.sentencia_commit(mysql,"call sp_delete_transferencias({0});".format(id))

    @classmethod
    def restar_saldo(self,mysql,cue,mont):
        Exe.sentencia_commit(mysql,"call sp_resta_saldo({0},{1});".format(cue,mont))    

    @classmethod
    def sumar_saldo(self,mysql,cue,mont):
        Exe.sentencia_commit(mysql,"call sp_suma_saldo({0},{1});".format(cue,mont))     

    @classmethod
    def registrar_gasto(self,mysql,ope,cue,cat,ben,mont,mon,nom,fec):
        Exe.sentencia_commit(mysql,"call sp_ingreso_gasto({0},{1},{2},{3},{4},{5},'{6}','{7}');".format(ope,cue,cat,ben,mont,mon,nom,fec))

    @classmethod
    def eliminar_operacion(self,mysql,id):
        Exe.sentencia_commit(mysql,"call sp_delete_movimiento({0});".format(id))    

    @classmethod
    def registrar_recordatorio(self,mysql,cuen,oper,cate,mont,mone,pago,bene,frec,fech,noti,desc):
        Exe.sentencia_commit(mysql,"call sp_ingreso_recordatorio({0},{1},{2},{3},{4},{5},{6},{7},'{8}',{9},'{10}');".format(cuen,oper,cate,mont,mone,pago,bene,frec,fech,noti,desc))   

    @classmethod
    def eliminar_recordatorio(self,mysql,id):
        Exe.sentencia_commit(mysql,"call sp_delete_recordatorio({0});".format(id))    

    @classmethod
    def registrar_cuenta(self,mysql,user,prop,ban,tar,mes,year,cvv,mont):
        Exe.sentencia_commit(mysql,"call sp_ingreso_cuenta({0},'{1}',{2},'{3}','{4}','{5}','{6}',{7});".format(user,prop,ban,tar,mes,year,cvv,mont)) 

    @classmethod
    def eliminar_cuenta(self,mysql,id):
        Exe.sentencia_commit(mysql,"call sp_delete_cuenta({0});".format(id))        

    @classmethod
    def actualizar_usuario(self,mysql,id,name,apat,amat,phone,mail,pswd):
        Exe.sentencia_commit(mysql,"call sp_update_user({0},'{1}','{2}','{3}','{4}','{5}','{6}');".format(id,name,apat,amat,phone,mail,pswd))    