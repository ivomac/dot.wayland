
c = get_config()

c.PasswordIdentityProvider.password_required = True
c.PasswordIdentityProvider.allow_password_change = False

c.LabApp.open_browser = False

c.LabServerApp.open_browser = False

c.ServerApp.autoreload = True

c.ServerApp.ip = "localhost"
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.webbrowser_open_new = 2

c.ServerApp.allow_root = False
c.ServerApp.allow_remote_access = False
c.ServerApp.allow_unauthenticated_access = False

c.ServerApp.terminals_enabled = False
