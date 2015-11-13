# PowerShift

A plugin for quickly switching views in Sublime Text 3.

If you have trouble with keeping track of your open tabs, you came to the right place. PowerShift brings speed and order to your environment.
By using PowerShift, you won't have to search for that one tab you had open five minutes ago, only to find it in the wrong pane.

![Power Switch](https://cloud.githubusercontent.com/assets/8056203/11155699/73a22836-8a47-11e5-83b5-5a39df440926.gif)

## Installation

### Manual installation

You can install PowerShift manually using git by running the following command within sublime packages directory (Preferences > Browse Packages):

```
$ git clone git@github:ice9js/power-shift-sublime.git PowerShift/
```

Or you can just copy the contents of this repository into ```Packages\PowerShift```.

## Usage

Use the following key shortcut to trigger the list of all currently open files.

- ```Ctrl/Super + Shift + o```

After selecting a file, it'll be moved into focus. If the file was open in a different pane, it'll be moved to the one that's currently active.

## Customization

### Key bindings

Go to ```Preferences > Package Settings > PowerShift > Key Bindings - User``` and override the following command:

```
power_shift
```
