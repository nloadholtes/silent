try:
    import weechat
except ImportError:
    print("This script must be run from inside weechat")
    exit -1

weechat.register("silent_python", "Silent", "1.0", "MIT", "Make a user silent", "", "")
weechat.prnt("", "Silent Python started?")

