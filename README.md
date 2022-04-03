# LeftWM RPMs
This repository makes it easy to build Rocky-8.5 RPMs for leftwm and some handy tools for a full configuration

## Packages
 * [LeftWM](#leftwm)
 * [Dunst](#dunst)
 * [Feh](#feh)
 * [Picom](#picom)
 * [Polybar](#polybar)
 * [Slock](#slock)
 * [Scrot](#scrot)

### [LeftWM](https://github.com/leftwm/leftwm)
The actual window manager

## Build Dependencies
* cargo-1.56+ via rustup

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.bashr
```

### [Dunst](https://dunst-project.org/)
dunst - A customizable and lightweight notification-daemon


### [Feh](https://feh.finalrewind.org/)

#### Build Dependencies

* `wget`
* `libXinerama-devel`
* `imlib2-devel`
* `libXt-devel`

```sh
sudo dnf install wget libXinerama-devel imlib2-devel libXt-devel
```

```sh
sudo /usr/bin/pip3 install sphinx
```

### [Picom](https://github.com/yshui/picom)
A lightweight compositor for X11

#### Build Dependencies

* `dbus-devel`
* `libconfig-devel`
* `libdrm-devel`
* `libev-devel`
* `libX11-devel`
* `libX11-xcb`
* `libXext-devel`
* `libxcb-devel`
* `mesa-libGL-devel`
* `meson`
* `pcre-devel`
* `pixman-devel`
* `uthash-devel`
* `xcb-util-image-devel`
* `xcb-util-renderutil-devel`
* `xorg-x11-proto-devel`

```sh
sudo dnf install dbus-devel libconfig-devel libdrm-devel libev-devel libX11-devel libX11-xcb libXext-devel libxcb-devel mesa-libGL-devel meson pcre-devel pixman-devel uthash-devel xcb-util-image-devel xcb-util-renderutil-devel xorg-x11-proto-devel
```

### [Polybar](https://polybar.github.io/)
A fast and easy to use tool for creating status bars

#### Build Dependencies
* `powertools`
* `epel`
* `cmake`
* `xcb-util-devel`
* `xcb-util-image-devel`
* `xcb-util-wm-devel`
* `cairo-devel`
* `libuv-devel`
* `alsa-lib-devel`
* `pulseaudio-libs-devel`
* `libcurl-devel`
* `libnl3-devel`
* `sphinx`

```sh
sudo dnf install epel-release
dnf config-manager --set-enabled powertools
sudo dnf install -y cairo-devel libuv xcb-util-devel libxcb-devel xcb-proto xcb-util-image-devel xcb-util-wm-devel
sudo dnf install cmake cairo-devel libuv-devel alsa-lib-devel pulseaudio-libs-devel jsoncpp-devel libnl3-devel
```

```sh
sudo /usr/bin/pip3 install sphinx
```

### [Slock](https://tools.suckless.org/slock/)
Simple X display locker. This is the simplest X screen locker we are aware of. It is stable and quite a lot of people in our community are using it every day when they are out with friends or fetching some food from the local pub.

### [Scrot](https://github.com/resurrecting-open-source-projects/scrot/)
scrot is a simple command line screen capture utility, it uses imlib2 to grab and save images.
