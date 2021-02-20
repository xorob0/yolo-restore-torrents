# YOLO restore torrent
I once deleted my download folder but I still had the files I wanted to seed on my system. The only problem was they where renamed and I did not know which belonged where. I wrote this script to create hard link between the renamed files their corresponding path in the `.torrent`'s structure.

You probably do not need this script. If you do that means you yeeted your download away and your not afraid to fix things in a dirty way.

There is no pretty way to link a file to it's `.torrent`'s file if renamed it. This script is named yolo for a reason: it will use the size to try and guess which file belongs to which torrent.

To use it you just need to:
```
python3 yolo-restore /path/to/renamed/files/ /path/to/torrent/files/ /output/path/
```
A really big thanks to [Bittornado](https://github.com/effigies/BitTornado)