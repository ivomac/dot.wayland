# Configuration file for lab.

c = get_config()  # noqa

c.LabServerApp.open_browser = False

c.LabApp.open_browser = False

c.ServerApp.allow_password_change = True

c.ServerApp.allow_remote_access = False

c.ServerApp.allow_root = False

c.ServerApp.allow_unauthenticated_access = True

c.ServerApp.autoreload = True

c.ServerApp.ip = "localhost"

c.ServerApp.open_browser = False

c.ServerApp.password = ""

c.ServerApp.password_required = True

c.ServerApp.port = "8888"

c.ServerApp.root_dir = "~"

c.ServerApp.terminals_enabled = False

c.ServerApp.token = ""

c.ServerApp.webbrowser_open_new = 2
