# astroid-plugin-identicon

Simple [plugin][astroid-plugins] to generate offline avatars for [astroid][].


## Motivation

Why should one prefer this plugin over the default (Gravatar usage) or the [other plugin][astroid-plugin-avatar]?

- Offline usage
- No potential meta data leakage
- Dunno tbh ¯\\\_(ツ)\_/¯


## Installation

First, make sure [pydenticon][] is installed for Python 3.

```sh
mkdir -p ~/.config/astroid/plugins/
cd ~/.config/astroid/plugins/
git clone https://github.com/oxzi/astroid-plugin-identicon
```


## License

This plugin is released under the [GPL-3.0-or-later][gpl3].


[astroid-plugin-avatar]: https://github.com/astroidmail/astroid-plugin-avatar
[astroid-plugins]: https://github.com/astroidmail/astroid-plugins
[astroid]: https://github.com/astroidmail/astroid
[gpl3]: LICENSES/GPL-3.0-or-later.txt
[pydenticon]: https://github.com/azaghal/pydenticon
