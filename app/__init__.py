from flask import Flask



# importar blueprints
from app.rutas.referenciales.productos.productos_routes import bp_productos

from app.rutas.operaciones.ventas.ventas_routes import bp_ventas

from app.rutas.auth.auth_routes import bp_auth






def crear_app():
    app = Flask(__name__)
    app.secret_key = "punto_frio"

    # registrar blueprints
    app.register_blueprint(bp_productos)

    app.register_blueprint(bp_ventas)

    app.register_blueprint(bp_auth)


    from flask import session

    @app.context_processor
    def inyectar_usuario():
        return {"usuario_logueado": session.get("usuario")}

    return app
