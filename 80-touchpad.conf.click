# softlink this file into:
# /usr/share/X11/xorg.conf.d
 
# and prevent the settings app from overwriting our settings:
# gsettings set org.gnome.settings-daemon.plugins.mouse active false
 
 
Section "InputClass"
    Identifier "nathan touchpad catchall"
    MatchIsTouchpad "on"
    MatchDevicePath "/dev/input/event*"
    Driver "synaptics"
 
    # No Drag Lock
    Option "LockedDrags" "0"

    # No Tapping
    Option "TapButton1" "0"
    Option "TapButton2" "0"
    Option "TapButton3" "0"

    # Enable the clickpad
    Option "ClickPad" "1"
    Option "ClickFinger1" "1"
    Option "ClickFinger2" "3"
    Option "ClickFinger3" "2"

    # Easy to touch, no pressure to register letting go
    Option "FingerLow" "10"
    Option "FingerHigh" "20"
 
    # prevents too many intentional clicks
    Option "PalmDetect" "0"
 
    # "natural" vertical and horizontal scrolling
    Option "VertTwoFingerScroll" "1"
    Option "VertScrollDelta" "75"
    Option "HorizTwoFingerScroll" "1"
    Option "HorizScrollDelta" "75"
    Option "CoastingFriction" "100"
    Option "PressureMotionMaxFactor" "3"

    # Reduce Noise
    Option "HorizHysteresis" "25"
    Option "VertHysteresis" "25"
 
    Option "MinSpeed" "0.5"
    Option "MaxSpeed" "1.8"
    Option "AccelerationProfile" "0.015"
    Option "ConstantDeceleration" "4"

    # Clean up settings not needed
    Option "MaxTapMove" "0"
    Option "MaxTapTime" "0"
    Option "MaxDoubleTapTime" "0"
    Option "MaxSingleTapTime" "0"
    Option "SingleTapTimeout" "0"
    Option "MaxTapMove" "0"
    Option "MaxTapMove" "0"
    Option "SoftButtonAreas"  "0 0 0 0 0 0 0 0"
EndSection
