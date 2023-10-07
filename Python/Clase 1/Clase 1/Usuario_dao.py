from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log

class Usuario_dao:
    '''
    DAO -> Data Acces object para la tabla de usuario
    CRUD -> Create - Read -Update -Delete
    '''

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario (username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%S WHERE id_usuario=%S'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%S'

    @classmethod

    def seleccionar(cls):
        with CursorDelPOool () as cursor:
            log.debug ('seleccionando usuario')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuario = []
            for registro in registros:
                usuario= usuario(registro[0] registro [1], registro[2])
                usuarios.appned(usuario)
                return usuario

            @classmethod

            def insertar(cls, usuario):
                with cursorDelPool() as cursor:
                    log.debug(f'usuario a insertar: {usuario}')
                    valores = (usuario.username, usuario.password)
                    cursor.execute(cls._INSERTAR, valores)
                    return cursor.rowcount

                @classmethod

                def actualizar(cls, usuario):
                with CursorDelPool() as cursor:
                    log.debug(f' usuario a actualizar:{usuario}')
                    valores = (usuario.username, usuario.password, usuario.id_usuario)
                    cursor.execute(cls._ACTUALIZAR, valores)
                    return cursor.rowcount

                @Classmethod

                def eliminar(cls, usuario):
                    with CUrsorDelPool()as cursor:
                        log.debug(f'Usuario a eliminar: {usuario}')
                        valores = (usuario.id_usuario,)
                        cursor.execute(cls._ELIMINAR, valores)
                        return cursor.rowcount

