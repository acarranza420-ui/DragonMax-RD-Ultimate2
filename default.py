import sys, urllib.parse
import xbmcgui, xbmcplugin, xbmcaddon
ADDON=xbmcaddon.Addon(); HANDLE=int(sys.argv[1]); BASE=sys.argv[0]
def url(action): return BASE+'?'+urllib.parse.urlencode({'action':action})
def item(label, action, desc=''):
    li=xbmcgui.ListItem(label); li.setInfo('video', {'title': label, 'plot': desc})
    xbmcplugin.addDirectoryItem(HANDLE, url(action), li, True)
def page(title, rows):
    xbmcplugin.setPluginCategory(HANDLE, title); xbmcplugin.setContent(HANDLE, 'files')
    for label, action, desc in rows: item(label, action, desc)
    xbmcplugin.endOfDirectory(HANDLE)
def simple(title, body): xbmcgui.Dialog().textviewer(title, body); root()
def root():
    page('DragonMax RD Wizard v6.0', [
        ('🐉 Install / Update DragonMax OS', 'builds', 'Fresh install, standard install, update existing build.'),
        ('🎬 Concierge + Netflix Layout', 'concierge', 'Hero spotlight, rows, smart dashboard, dynamic banners.'),
        ('🏰 Living Realms', 'realms', 'Dragon, Wizard, Vampire, Martial Arts, Anime, Fitness, Documentary realms.'),
        ('📱 Dragon Portal + QR Upload', 'portal', 'Phone dashboard concept, upload images/videos, manage themes.'),
        ('🔐 Quick Connect Services', 'connect', 'One-screen account authorization guide for RD, Trakt, Plex, Jellyfin, Emby, YouTube, subtitles.'),
        ('🏢 Office Panel', 'office', 'Internet, Google Docs, CompanyCam, email, work shortcuts.'),
        ('🔊 Audio & Theater Center', 'audio', '11.2 AVR guidance, passthrough, test media, theater profiles.'),
        ('🧰 Maintenance + Recovery', 'maintenance', 'Cache clean, package clean, auto updates, repair build, backup/restore.'),
        ('🎙 Voice + Chime Center', 'voice', 'Voice packs, context voices, 5-hour chime, time/date/temp.'),
        ('🔒 Private Vault', 'vault', 'PIN 1234, hidden section, local/authorized media only.'),
        ('ℹ GitHub / Kodi Help', 'help', 'Upload dist to GitHub Pages and install from Kodi.'),
    ])
def builds():
    page('Install / Update DragonMax OS', [
        ('Fresh Install - DragonMax RD v6', 'fresh', 'Use for a clean setup on Fire Stick 4K Max.'),
        ('Standard Install - Keep User Settings', 'standard', 'Use when updating without wiping custom preferences.'),
        ('Update Existing Build', 'update', 'Refresh wizard/theme/docs from GitHub source.'),
        ('Build Payload Notes', 'payload', 'Explains where to place theme/settings payload ZIPs.'),
    ])
PAGES={
'fresh':('Fresh Install', 'Recommended flow:\n1. Backup Kodi userdata.\n2. Install legal add-ons from official/authorized sources.\n3. Apply DragonMax theme/settings payload.\n4. Connect services with Quick Connect.\n5. Reboot Kodi.\n\nThis wizard starter does not include unauthorized streaming add-ons.'),
'standard':('Standard Install', 'Keeps existing user data. Apply only theme, menu, artwork, docs, and wizard updates.'),
'update':('Update Existing Build', 'Use GitHub Pages as the update source. Upload the contents of dist to your repo root, then refresh the repository in Kodi.'),
'payload':('Build Payload Notes', 'Place legal theme/settings packages in /builds and list them in resources/builds/builds.json. Do not bundle piracy add-ons, credentials, or copyrighted assets you do not own.'),
'concierge':('Concierge + Netflix Layout', 'Home: DragonMax Concierge, Hero Spotlight, Continue Watching, Favorites, Anime Universe, Movies, TV Shows, Martial Arts, Fitness, Learning Center, Recently Added.\n\nAdds smart banners, dynamic hero rotation, profile status, weather, storage, service status, and fewer top-level menus.'),
'realms':('Living Realms', 'Realm Travel System:\n- Dragon Realm\n- Dark Wizard Realm\n- Vampire Queen Realm\n- Anime Warrior Realm\n- Martial Arts Realm\n- Fitness Arena\n- Documentary Realm\n- Music Realm\n\nEach realm can swap wallpaper sets, sounds, voice personality, companion look, widgets, and icon accents.'),
'portal':('Dragon Portal + QR Upload', 'Phone dashboard concept for uploading wallpapers/videos, changing theme/voice, viewing storage, scheduling maintenance, and managing profile preferences. Use QR code to open your own local server, NAS, SMB, Google Drive, or cloud upload page.'),
'connect':('Quick Connect Services', 'Single onboarding screen for accounts:\nReal-Debrid cloud, Trakt, Plex, Jellyfin, Emby, YouTube, OpenSubtitles, Weather.\n\nUse QR/device-code sign-in where the service supports it. Never store passwords in this build.'),
'office':('Office Panel', 'Work shortcuts only; Fire TV/Kodi is not a full office workstation. Recommended launch targets:\n- Silk Browser / Internet\n- Google Docs web shortcut\n- Gmail or webmail shortcut\n- CompanyCam web/app shortcut if available on device\n- Google Drive shortcut\n\nDo not store work credentials in Kodi files.'),
'audio':('Audio & Theater Center', 'For 11.2-capable AVR/processors, Kodi typically sends bitstream/passthrough and the AVR expands channels. Suggested options:\nChannels: 7.1 where applicable\nPassthrough: ON\nDolby Digital Plus/TrueHD/DTS/DTS-HD: ON if your receiver supports them.\n\nAdd theater profiles: Movie Night, Anime Theater, Concert Hall, Late Night, Reference Audio.'),
'maintenance':('Maintenance + Recovery', 'Maintenance Center:\n- Quick Clean\n- Deep Clean\n- Clear Cache\n- Clean Packages\n- Update Add-ons\n- Backup Build\n- Restore Build\n- Repair Build\n- Reset Theme\n- Fix Widgets\n\nBack up before major updates.'),
'voice':('Voice + Chime Center', 'Voices: Ancient Dragon, Dragon Queen, Dark Wizard, Arcane Wizardess, Vampire Queen, Martial Arts Master, AI Assistant.\n\nContext switching: Realm determines voice.\n5-hour chime announces time/date/temp if weather is configured. Quiet hours recommended.'),
'vault':('Private Vault', 'Private Vault PIN: 1234\nHidden from home and search. Use only for your own local, cloud, Plex, Jellyfin, Emby, or authorized content.'),
'help':('GitHub / Kodi Help', 'Upload everything inside dist to your GitHub repo root. Enable GitHub Pages from main/root. Add this source in Kodi:\nhttps://acarranza420-ui.github.io/DragonMax-RD-Ultimate/\nInstall repository.dragonmax-1.6.0.zip, then install DragonMax RD Wizard from the repo.')
}
def route():
    q=urllib.parse.parse_qs(urllib.parse.urlparse(sys.argv[2]).query); action=q.get('action',['root'])[0]
    if action=='root': return root()
    if action=='builds': return builds()
    if action in PAGES: return simple(*PAGES[action])
    root()
route()
