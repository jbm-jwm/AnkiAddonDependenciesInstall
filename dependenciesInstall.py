from aqt import mw
from aqt.addons import download_addons
config = mw.addonManager.getConfig(__name__)

try:
    from aqt import gui_hooks
except ImportError:  # For some older versions of Anki
    gui_hooks = None

def on_done(info)-> None:
    print(info)

# download only AnkiConnect, should be use with a configuration (to add more dependencies, multiple dependencies configurations to do)   

def dependenciesAddonsInstall():    
    for id in config['addons']:
        if(id not in mw.addonManager.allAddons()):
            download_addons(mw, mw.addonManager, [id], on_done)
            
def dependenciesAddonsConfig():
# configuration for Anki Connect
    configAnkiConnect = mw.addonManager.getConfig("2055492159")
    if "https://mezase.herokuapp.com" not in configAnkiConnect['webCorsOriginList']
        configAnkiConnect['webCorsOriginList'] += ["https://mezase.herokuapp.com"]
        mw.addonManager.writeConfig("2055492159",configAnkiConnect)

# Attach function to window did init hook (if GUI hooks are available)
if gui_hooks:
    gui_hooks.main_window_did_init.append(dependenciesAddonsInstall)