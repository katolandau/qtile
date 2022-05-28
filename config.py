

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile

import os

mod = "mod4"
terminal = "kitty" #guess_terminal()

# Colores y variables
color_barra="#282828"  #"#353138" # "#211226"
tamano_barra= 25
tamano_iconos= 20
fuente_predeterminada= "Monoid Nerd Font"
tamano_fuente= 12
color_activo="#ffffff" #"#e2c1f5" #color de iconos activos
color_inactivo="#212121" #"#91a5b5"
color_sombra="#000000" #"#9600fa"
color_fg="#ffffff" # "#592878"
color_bg="#83a598" #"#1f182b"
color_claro="#793be3"
#color_claro2="#f0ec0e"
color_urgent="#052ba8"
#color_urgente="#00d0f0"
color_texto="#9300a3"
color_grupo1="#0b9624"

# COLORES KATO

colors=[["#00000000", "#00000000", "#00000000"], #color 0
        ["#2e3440", "#2e3440", "#2e3440"], #color 1
        ["#211226", "#211226", "#211226"]]


# Creacion de nuevas funciones
def fc_separador():
    return widget.Sep(
        linewidth=0,
        padding=5,
        background=color_barra,
        foreground=colors[0]
    )

def fc_separador2():
    return widget.Sep(
        linewidht=0,
        padding=50,
        backgroun=color_barra,
        foreground=color_barra
    )

#funcion para crear curvas del rectangulo
def fc_rectangulo(vColor,tipo):
    if tipo == 0:
        icono=""
    else:
        icono=""
    return widget.TextBox(
        text=icono,
        fontsize=tamano_barra,
        foreground=vColor,
        background=color_barra,
        padding=-1

    )

def fc_rectangulo2(vColor,tipo):
    if tipo == 0:
        icono=""
    else:
        icono=""
    return widget.TextBox(
        text=icono,
        fontsize=tamano_barra,
        foreground=vColor,
        background=color_barra,
        padding=3

    )

#funcion para crear texto u icono
def fc_icono(icono, color_grupo):
    return widget.TextBox(
        text=icono,
        fontsize=25,
        foreground="#212121",
        background=color_grupo

    )


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="kitty"),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="",
        #dmenu_font="sans",
        #dmenu_fontsize=30,
        background="#222222",
        selected_background="#6c2ea3",
        foreground="#6c2ea3",
        selected_foreground="#ab5df0"
    )),
        desc="Spawn a command using a prompt widget"),
]

# lista de iconos
#

groups = [Group(i) for i in [
    " 一 ", " 二 ", " 三 ", " 四 ", " 五 ", " 六 ", " 七 ", " 八 ", " 九 ",
]]

for i, group in enumerate(groups):
    numeroEscritorio=str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], numeroEscritorio, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], numeroEscritorio, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_width=4,
        border_focus="#cc241d",
        border_normal="#fb4934",
        margin=10,
        change_size=10,

    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    #layout.Zoomy(
    #    columnwidth=100,
    #    margin=10,
    #    property_big='0.5',
    #    property_small='0.5',
    #    property_name="kato"
    #),
      layout.Floating(
        border_width=5,
        border_focus=color_barra,
        border_normal=color_bg,
        margin=6,

      ),
]

### PROMPT ####
#prompt= "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

### MOUSE CALLBACKS ###

def open_neofetch():
    qtile.cmd_spawn(terminal + "-e neofetch")


### WIDGETS ###

widget_defaults = dict(
    font= fuente_predeterminada,
    fontsize=tamano_fuente,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    background=color_barra,
                    padding=3,
                    linewidth=0,

                ),
                fc_rectangulo(color_bg, 0),

                widget.Sep(
                    background=color_bg,
                    padding=3,
                    linewidth=0,

                ),

                widget.Image(
                    filename="~/.config/qtile/icons/archlinux.png",
                    background=color_bg,
                    scale=True,
                    margin=0,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e import -window root test.png')}
                ),
                #inicio de curva
                #fc_rectangulo(color_bg, 0),
                widget.Sep(
                    background=color_barra,
                    padding=2,
                    linewidth=0,

                ),

                widget.GroupBox(
                    active=color_activo,
                    background=color_bg,
                    border_width=1,
                    disable_drag= True,
                    fontsize=tamano_iconos,
                    fontshadow=color_sombra, # "#4c2069",
                    foreground=color_fg,
                    highlight_method = 'block',
                    inactive=color_inactivo,
                    margin_x=0,
                    margin_y=3,
                    padding_x=0,
                    padding_y=10,
                    rounded= True,
                    this_current_screen_border="#458588",
                    this_screen_border="#d79921",
                    urgent_alert_method='line',
                    urgent_border="#d79921",
                ),
                fc_rectangulo(color_bg, 1),
                #fin de curva


               # widget.Image(
               #     filename="~/.config/qtile/icons/hentai.png",
               #     background=color_bg,
               # ),
                widget.Sep(
                    background=color_barra,
                    padding=20,
                    linewidth=0,

                ),
                #inicio de curva
                #fc_rectangulo(color_bg, 0),
                #widget.Image(
                #    filename="~/.config/qtile/icons/calendario.png",
                #    background=color_bg,
                #),
                #widget.Clock(format='%d %b %a',
                #    background=color_bg,

                #    font='Monoid NF Bold',
                #    fontsize=15
                #),
                #fc_rectangulo(color_bg, 1),
                #fin de curva
                fc_separador2(),
                fc_rectangulo("#fb4934", 0),
                widget.CurrentLayout(
                    background="#fb4934",
                    foreground="#212121",
                    font='Iosevka Term Heavy Oblique',
                    fontsize=20
                ),
                fc_rectangulo("#fb4934", 1),
                fc_separador(),
                widget.CurrentLayoutIcon(
                    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    padding = 0,
                    scale = 0.7,
                    background = color_barra,
                    foreground = "#96d5ff"
                ),
                fc_separador2(),
                fc_separador2(),

                widget.Prompt(
                    background=color_barra,
                    foreground=color_fg,

                ),
                widget.WindowName(
                    background=color_barra,
                    foreground="#d79921",
                    fontshadow="#d79921",
                    fontsize=15,
                    padding=0,
                    font='Iosevka Term Heavy Oblique'
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                fc_separador(),
                widget.Systray(),

                fc_separador(),

                widget.OpenWeather(

                        location='Santa Cruz de la Sierra, BO',
                        foreground="#09ffff",
                        fontsize=14
                    
                ),

                fc_separador(),
                
                widget.CPUGraph(
                    type='line'
            
                ),
                

                fc_separador(),

                #widget.CapsNumLockIndicator(
                #        background = "#ed371f",
                #    foreground = "#000000",
                #    fontsize=14
                #
                #),

                fc_separador(),

                #inicio de curva
                fc_rectangulo("#a89984", 0),
               # widget.Image(
               #     filename="~/.config/qtile/icons/termometro.png",
               #     background=color_grupo1
               # ),
               # fc_icono("", color_grupo1), #thermometer
               # widget.ThermalSensor(
               #     foreground = "#f5f5f5",
               #     background = color_grupo1,
               #     threshold = 50,
               #     tag_sensor = "Core_0",
               #     fmt= 'T1:{}',
               #     padding=6,
               #     fontsize=14
               #
               # ),




                widget.Image(
                    filename="~/.config/qtile/icons/ram4.png",
                    background="#a89984",
                    scale=True,
                    margin=2

                ),
                fc_icono("", "#a89984"), #hard disk
                widget.Memory(
                    foreground = "#212121",
                    background = "#a89984",
                    fontsize = 20,
                    font = 'Iosevka Term Heavy Oblique'


                ),
                fc_rectangulo("#a89984", 1),
                #fin de curva
                fc_separador(),
                #inicio de curva
                fc_rectangulo("#a89984" , 0),
                #fc_icono(" ", "#d79921"),
                widget.Image(
                    filename="~/.config/qtile/icons/wifi.png",
                    background="#a89984",
                    scale=True,
                    margin=2
                 ),


                widget.Net(
                    background="#a89984",
                    foreground="#212121",
                    fontsize=20,
                    format='{down}{up}',
                    interface=None,
                    padding=1,
                    font='Iosevka Term Heavy Oblique',
                    #fontsize=
                ),
                fc_rectangulo("#a89984" , 1),
                #inicio de curva
                fc_separador(),
                fc_rectangulo("#a89984", 0),
                widget.Image(
                    filename="~/.config/qtile/icons/reloj3.png",
                    background="#a89984",
                    scale= True,
                    margin=3
                ),
                widget.Clock(format='%I:%M %p',
                    background="#a89984",
                    foreground="#212121",
                    font='Iosevka Term Heavy Oblique',
                    fontsize=20
                ),
                fc_rectangulo("#a89984", 1),
                #fin de curva
                fc_separador(),
                #widget.AGroupBox(),
                #widget.QuickExit(
                #    default_text= '',
                #    fontsize=tamano_iconos,
                #    background=color_barra,
                #    foreground="#00ffff",
                #    fontshadow="#9900ff", #"#3ed6d6",
                #    padding=15,
                #),

            ],
            tamano_barra,
            background=color_barra,
            #border_color="#000000",
            #border_width=0,
            #opacity=1,
            margin=[0,10,0,10]
        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

inicio= [
    "feh --bg-fill /home/kato/Downloads/makima.jpg",
    "xrandr --output VGA-0 --auto --primary --mode 1920x1080 --rate 60  --pos 0x0 --rotate normal",
    "picom --no-vsync &",
]

for x in inicio:
    os.system(x)


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
