# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['KingTheFool.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/images/backgrounds/bg/background.png', 'assets/images/backgrounds/bg/dark_forest.png', 'assets/images/backgrounds/bg/dark_forest.jpeg', 'assets/images/backgrounds/bg/dark_forest2.jpeg', 'assets/images/backgrounds/bg/forest_background.png', 'assets/images/backgrounds/bg/market.png', 'assets/images/backgrounds/bg/pupet_wizard_background.png', 'assets/images/backgrounds/bg/room_zish.png' ),
        ('assets/images/backgrounds/менюшки/choice.png', 'assets/images/backgrounds/менюшки/choice2.png', 'assets/images/backgrounds/менюшки/comming soon.png', 'assets/images/backgrounds/менюшки/management_bg.png', 'assets/images/backgrounds/менюшки/menu.jpg', 'assets/images/backgrounds/менюшки/menu.png'),
        ('assets/images/backgrounds/Утренний рассвет/в небе голубом облака плывут как корабли.jpeg', 'assets/images/backgrounds/Утренний рассвет'),
        ('assets/images/icons/*', 'assets/images/icons'),
        ('assets/images/Акустический альбом/*', 'assets/images/Акустический альбом'),
        ('assets/images/Будь как дома путник/*', 'assets/images/Будь как дома путник'),
        ('assets/images/Как в старой сказке/*', 'assets/images/Как в старой сказке'),
        ('assets/images/камнем по голове/*', 'assets/images/камнем по голове'),
        ('assets/images/кнопки/*', 'assets/images/кнопки'),
        ('assets/images/компоненты локации/*', 'assets/images/компоненты локации'),
        ('assets/images/обложки альбомов/*', 'assets/images/обложки альбомов'),
        ('assets/images/персонажи/*', 'assets/images/персонажи'),
        ('assets/sounds/*', 'assets/sounds')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='KingTheFoolsGame',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
