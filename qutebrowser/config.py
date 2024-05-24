import os

config.load_autoconfig(False)

config.source("colors/default.py")

c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.contrast = 0
c.colors.webpage.darkmode.policy.images = "smart"
c.colors.webpage.darkmode.policy.page = "smart"

c.content.user_stylesheets = [
    "stylesheets/default.css",
    "stylesheets/full.css",
]

c.fileselect.handler = "external"
c.fileselect.single_file.command = ["picker", "{}"]
c.fileselect.multiple_files.command = ["picker", "{}"]
c.fileselect.folder.command = ["picker", "{}"]

c.editor.command = ["foot", "-e", "nvim", "{file}"]

c.backend = "webengine"
c.window.hide_decoration = True

c.auto_save.session = True

c.session.lazy_restore = False
c.session.default_name = "base"

c.history_gap_interval = 5

c.zoom.default = "120%"
c.zoom.levels = [
    "10%",
    "20%",
    "30%",
    "40%",
    "50%",
    "60%",
    "70%",
    "80%",
    "90%",
    "100%",
    "110%",
    "120%",
    "130%",
    "140%",
    "150%",
    "160%",
    "170%",
    "180%",
    "190%",
    "200%",
]

c.scrolling.smooth = True
c.scrolling.bar = "overlay"

c.qt.highdpi = False

c.window.title_format = "Qutebrowser {id}: {current_title}{private}"

c.scrolling.bar = "when-searching"
c.scrolling.smooth = True

c.tabs.select_on_remove = "last-used"
c.tabs.mousewheel_switching = True
c.tabs.wrap = False
c.tabs.tooltips = False

c.tabs.title.format = "{current_title}{audio}{private}"
c.tabs.title.format_pinned = ""
c.tabs.title.alignment = "center"
c.tabs.focus_stack_size = 1000
c.tabs.undo_stack_size = 1000
c.tabs.last_close = "blank"
c.tabs.new_position.related = "last"
c.tabs.new_position.unrelated = "last"
c.tabs.new_position.stacking = False
c.tabs.indicator.padding = {"bottom": 0, "left": 0, "right": 5, "top": 0}
c.tabs.indicator.width = 5
c.tabs.padding = {"bottom": 1, "left": 1, "right": 1, "top": 1}
c.tabs.pinned.frozen = True
c.tabs.background = False
c.tabs.close_mouse_button = "right"
c.tabs.close_mouse_button_on_bar = "ignore"

c.statusbar.widgets = ["url"]
c.statusbar.position = "bottom"
c.statusbar.show = "always"

c.input.forward_unbound_keys = "auto"
c.input.insert_mode.auto_enter = True
c.input.insert_mode.auto_leave = True
c.input.insert_mode.auto_load = False
c.input.insert_mode.leave_on_load = False
c.input.insert_mode.plugins = False
c.input.links_included_in_focus_chain = True
c.input.spatial_navigation = False
c.input.partial_timeout = 0
c.input.mouse.rocker_gestures = False

c.keyhint.delay = 300
c.keyhint.radius = 0

c.messages.timeout = 2000

c.new_instance_open_target = "tab-silent"
c.new_instance_open_target_window = "first-opened"

c.prompt.filebrowser = False
c.prompt.radius = 0

c.hints.uppercase = True
c.hints.chars = "djfhskeialwo"
c.hints.leave_on_load = False
c.hints.hide_unmatched_rapid_hints = True

c.completion.open_categories = ["searchengines", "history"]
c.completion.height = "30%"
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 0
c.completion.shrink = True
c.completion.use_best_match = True

c.downloads.location.prompt = False
c.downloads.location.directory = os.environ["HOME"] + "/Downloads"
c.downloads.location.suggestion = "filename"
c.downloads.position = "top"
c.downloads.remove_finished = 5000

c.content.prefers_reduced_motion = True
c.content.default_encoding = "utf-8"
c.content.pdfjs = False
c.content.print_element_backgrounds = False

c.content.blocking.enabled = True

c.content.blocking.method = "both"
c.content.blocking.adblock.lists = [
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badlists.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/thirdparties/easylist-downloads.adblockplus.org/easyprivacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/thirdparties/pgl.yoyo.org/as/serverlist",
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts",
    "https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt",
    "https://fanboy.co.nz/fanboy-problematic-sites.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
    "https://easylist.to/easylist/easylist.txt",
    "https://raw.githubusercontent.com/bogachenko/fuckfuckadblock/master/fuckfuckadblock.txt",
]

c.content.geolocation = "ask"
c.content.desktop_capture = "ask"
c.content.media.audio_capture = "ask"
c.content.media.video_capture = "ask"
c.content.media.audio_video_capture = "ask"
c.content.mouse_lock = False
c.content.cookies.accept = "no-3rdparty"
c.content.cookies.store = True
c.content.persistent_storage = "ask"
c.content.javascript.alert = False
c.content.notifications.enabled = True
c.content.javascript.clipboard = "access"

with config.pattern("*://mail.google.com/*") as p:
    p.content.register_protocol_handler = True

with config.pattern("*://calendar.google.com/*") as p:
    p.content.register_protocol_handler = True


web_size = 16

c.fonts.default_family = ["Fira Mono Medium"]
c.fonts.default_size = "18px"

c.fonts.web.size.default = web_size
c.fonts.web.size.default_fixed = web_size
c.fonts.web.size.minimum = web_size
c.fonts.web.size.minimum_logical = web_size


c.url.default_page = "about:blank"
c.url.start_pages = "about:blank"
c.url.open_base_url = True
c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}&pws=0&gl=us&gws_rd=cr",
    "G": "https://www.google.com/search?q={}&pws=0&gl=us&gws_rd=cr",
    "I": "https://www.google.com/search?q={}&pws=0&gl=us&gws_rd=cr&tbm=isch",
    "JOB": "https://www.google.com/search?q=site%3Alinkedin.com%2Fjobs+%28%22Switzerland%22+AND+%22Easy+Apply%22+AND+%22{}%22%29&pws=0&gl=us&gws_rd=cr",
    "M": "https://www.openstreetmap.org/search?query={}",
    "GM": "https://www.google.com/maps/search/{}",
    "CF": "https://conjugueur.reverso.net/conjugaison-francais-verbe-{}.html",
    "W": "https://en.wikipedia.org/w/index.php?search={}",
    "WF": "https://fr.wikipedia.org/w/index.php?search={}",
    "WP": "https://pt.wikipedia.org/w/index.php?search={}",
    "WK": "https://en.wiktionary.org/wiki/{}",
    "WKF": "https://fr.wiktionary.org/wiki/{}",
    "A": "https://wiki.archlinux.org/index.php?search={}",
    "PY": "https://docs.python.org/3/search.html?q={}&check_keywords=yes&area=default",
    "Y": "https://www.youtube.com/results?search_query={}",
    "GIT": "https://github.com/search?q={}",
    "ETF": "https://www.justetf.com/en/etf-profile.html?isin={}",
    "LI": "https://www.linkedin.com/jobs/search/?keywords={}&location=Switzerland",
    "B": "https://libgen.is/index.php?req={}",
    "AX": "https://arxiv.org/search/?query={}&searchtype=all",
    "AR": "http://libgen.is/scimag/?q={}",
    "REF": "https://search.crossref.org/?q={}",
    "TP": "https://thepiratebay.org/search.php?q={}",
    "T": "https://1337x.to/search/{}/1/",
    "TA": "https://nyaa.si/?f=0&c=0_0&q={}&s=seeders&o=desc",
    "TOP": "https://www.toppreise.ch/browse?q={}",
    "RIC": "https://www.ricardo.ch/fr/s/{}/",
    "DGT": "https://www.digitec.ch/en/search?q={}",
    "GLX": "https://www.galaxus.ch/search?q={}",
    "TM": "https://www.techmania.ch/fr/Search/DoSearch?suche={}",
    "AE": "https://www.aliexpress.com/wholesale?SearchText={}",
    "AMZ": "https://www.amazon.de/s?k={}",
    "IKEA": "https://www.ikea.com/ch/en/search/products/?q={}",
    "DECA": "https://www.decathlon.ch/fr/search?Ntt={}",
    "DEAL": "https://isthereanydeal.com/search/?q={}",
    "CDK": "https://www.cdkeys.com/catalogsearch/result/?q={}",
    "STM": "https://store.steampowered.com/search/?term={}",
    "BGG": "https://boardgamegeek.com/geeksearch.php?action=search&objecttype=boardgame&q={}",
    "ID": "https://infinitediscs.com/Search-Results?search_text={}",
    "FD": "https://search.f-droid.org/?q={}&lang=en",
    "AM": "https://www.apkmirror.com/?searchtype=apk&s={}",
    "LY": "https://genius.com/search?q={}",
    "DOI": "https://www.doi.org/{}",
    "ISBN": "https://isbnsearch.org/search?s={}",
    "SUP": "https://examine.com/supplements/{}/",
    "GE": "https://www.deepl.com/en/translator#de/en/{}",
    "FE": "https://www.deepl.com/en/translator#fr/en/{}",
    "EF": "https://www.deepl.com/en/translator#en/fr/{}",
}

c.bindings.key_mappings = {}
config.unbind("M")
config.unbind("V")
config.unbind("U")
config.unbind("<Ctrl-h>")
config.unbind("<Ctrl-v>")


Up = "k"
Down = "j"
Left = "h"
Right = "l"

Prev = ","
Next = "."

TabList = "<Space>"

Hint = "f"
RapidHint = "F"

Open = "o"
Close = "d"

Window = "w"
PrivateWindow = "W"
Tab = "s"

StyleToggle = "a"
BackgroundToggle = "A"

Yank = "y"

Quickmark = "m"
SaveQuickmark = "M"

Edit = "e"
EditField = "E"

Video = "V"

Userscript = "U"

Mute = "-"

ConfigSource = "c"
Source = "C"
Inspect = "I"
Pdf = "P"

Title = "t"
Domain = "d"
Selection = "s"

Cancel = "c"
Retry = "r"
Clear = "x"

myaliases = {
    "scroll-up": "scroll-page 0 -0.4",
    "scroll-down": "scroll-page 0 +0.4",
    "d": "session-delete",
    "e": "session-load",
    "w": "session-save --only-active-window",
    "wa": "session-save",
}

c.aliases = {**c.aliases, **myaliases}

config.bind(
    StyleToggle,
    'config-cycle -t content.user_stylesheets "[]" "['
    + ", ".join(c.content.user_stylesheets)
    + ']"',
)

config.bind(
    BackgroundToggle,
    "config-cycle -t colors.webpage.bg #cccccc " + c.colors.webpage.bg,
)

config.bind("<Shift-Return>", "command-accept -r", "command")
config.bind(f"<Control-{Down}>", "completion-item-focus --history next", "command")
config.bind(f"<Control-{Up}>", "completion-item-focus --history prev", "command")

config.bind(Up, "scroll-up")
config.bind(Down, "scroll-down")

config.bind(Left, "tab-prev")
config.bind(Right, "tab-next")

config.bind("<Control-" + Left + ">", "tab-move -")
config.bind("<Control-" + Right + ">", "tab-move +")

config.bind(Next, "forward")
config.bind(Tab + Next, "forward -t")
config.bind(Window + Next, "forward -w")

config.bind(Prev, "back")
config.bind(Tab + Prev, "back -t")
config.bind(Window + Prev, "back -w")

config.bind(TabList, "clear-messages ;; cmd-set-text -s :tab-select")

config.bind("<Ctrl-Shift-^>", "tab-focus last")
config.bind("<Ctrl-Shift-6>", "tab-focus last")
config.bind("<Ctrl-^>", "tab-focus last")
config.bind("<Ctrl-6>", "tab-focus last")

config.bind(Close, "tab-close")
config.bind(Tab + Tab, "tab-clone")
config.bind(Tab + Mute, "tab-mute")

config.bind(Window + Close, "close")
config.bind(Window + Window, "tab-clone -w")

config.bind(RapidHint, "hint -a -r all tab-bg")

config.bind(Hint, "hint -a all current")
config.bind(Tab + Hint, "hint -a all tab-fg")
config.bind(Window + Hint, "hint -a all window")
config.bind(Yank + Hint, "hint -a all yank")

config.bind(Open, "cmd-set-text -s :open")
config.bind(Tab + Open, "cmd-set-text -s :open -t")
config.bind(Window + Open, "cmd-set-text -s :open -w")
config.bind(PrivateWindow + Open, "cmd-set-text -s :open -p")

config.bind(Yank + Yank, "yank url")
config.bind(Yank + Title, "yank title")
config.bind(Yank + Domain, "yank domain")
config.bind(Yank + Selection, "yank selection")

config.bind(Video + Video, "spawn -d mpv {url}")
config.bind(Video + Hint, "hint all spawn -d mpv {hint-url}")

config.bind(Userscript + "d", "spawn --userscript doi-add")
config.bind(Userscript + "x", "spawn --userscript arxiv-add")

config.bind(
    Userscript + "p",
    "spawn --userscript qute-pass -d tofi --password-store ~/.config/password-store",
)
config.bind(
    Userscript + "u",
    "spawn --userscript qute-pass -d tofi --username-only --password-store ~/.config/password-store",
)
config.bind(
    Userscript + "P",
    "spawn --userscript qute-pass -d tofi --password-only --password-store ~/.config/password-store",
)

config.bind(Edit, "edit-url")
config.bind(Tab + Edit, "edit-url -t")
config.bind(Window + Edit, "edit-url -w")
config.bind(PrivateWindow + Edit, "edit-url -p")

config.bind(EditField, "edit-text")

config.bind(SaveQuickmark, "quickmark-save")
config.bind(Quickmark, "cmd-set-text -s :quickmark-load")
config.bind(Tab + Quickmark, "cmd-set-text -s :quickmark-load -t")
config.bind(Window + Quickmark, "cmd-set-text -s :quickmark-load -w")

config.bind(Inspect, "devtools window")

config.bind(Source, "view-source -e")
config.bind(ConfigSource, 'config-source ;; message-info "Config loaded."')
config.bind(Pdf, 'print -f print.pdf ;; message-info "PDF created!"')
