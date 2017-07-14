def register_blueprints(app):
    # Prevents circular imports
    from apps.views import admin
    from apps.views import home
    app.register_blueprint(admin.mod,url_prefix='/admin')
    app.register_blueprint(home.mod)