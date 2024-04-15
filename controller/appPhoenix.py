from db.database import *

class appPhoenix:

    @classmethod
    def call_recordatorios(self,mysql,email):
        data=Exe.sentencia_all(mysql,"call sp_recordatorios('{0}');".format(email))
        return data

    @classmethod
    def call_cuentas(self,mysql,email):
        data=Exe.sentencia_all(mysql,"call sp_mostrar_cuentas('{0}');".format(email))
        return data

    @classmethod
    def call_beneficiarios(self,mysql):
        data=Exe.sentencia_all(mysql,"call sp_mostrar_beneficiarios();")
        return data

    @classmethod
    def call_movimientos(self,mysql,email):
        data=Exe.sentencia_all(mysql,"call sp_movimientos('{0}');".format(email))
        return data

    @classmethod
    def call_transferencias(self,mysql,email):
        data=Exe.sentencia_all(mysql,"call sp_mostrar_trans('{0}');".format(email))
        return data

    @classmethod
    def call_saldo_total(self,mysql,email):
        data=Exe.sentencia_one(mysql,"call sp_saldo_total('{0}');".format(email))
        return data

    @classmethod
    def call_usuario(self,mysql,email):
        data=Exe.sentencia_one(mysql,"call sp_call_user('{0}');".format(email))
        return data

    @classmethod
    def val_duplicar_usuario(self,mysql,name,pat,mat,phone,email):
        data=Exe.sentencia_one(mysql,"call sp_duplicar_signup('{0}','{1}','{2}','{3}','{4}');".format(name,pat,mat,phone,email))
        return data

    @classmethod
    def val_login(self,mysql,email,password):
        data=Exe.sentencia_one(mysql,"call sp_valid_login('{0}','{1}');".format(email,password))    
        return data

    @classmethod
    def val_duplicar_cuenta(self,mysql,tar):
        data=Exe.sentencia_one(mysql,"call sp_duplicar_cuenta('{0}');".format(tar))   
        return data