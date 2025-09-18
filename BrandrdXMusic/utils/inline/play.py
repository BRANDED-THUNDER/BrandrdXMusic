import math

from pyrogram.types import InlineKeyboardButton

from BrandrdXMusic.utils.formatters import time_to_seconds


# Make sure you have this helper function somewhere
def time_to_seconds(time_str: str) -> int:
    """Convert HH:MM:SS or MM:SS to total seconds."""
    parts = list(map(int, time_str.split(":")))
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h, m, s = 0, parts[0], parts[1]
    else:
        h, m, s = 0, 0, parts[0]
    return h * 3600 + m * 60 + s


def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur) or 1  # avoid ZeroDivisionError
    percentage = (played_sec / duration_sec) * 100
    tgn = math.floor(percentage)

    if 0 <= tgn <= 10:
        bar = "❥—————————"
    elif 10 < tgn <= 20:
        bar = "—❥————————"
    elif 20 < tgn <= 30:
        bar = "——❥———————"
    elif 30 < tgn <= 40:
        bar = "———❥——————"
    elif 40 < tgn <= 50:
        bar = "————❥—————"
    elif 50 < tgn <= 60:
        bar = "—————❥————"
    elif 60 < tgn <= 70:
        bar = "——————❥———"
    elif 70 < tgn <= 80:
        bar = "———————❥——"
    elif 80 < tgn <= 95:
        bar = "————————❥—"
    else:
        bar = "—————————❥"

    return [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url="https://t.me/BRANDEDKING8"),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/BRANDED_WORLD"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]


def stream_markup(_, chat_id):
    return [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url="https://t.me/BRANDEDKING8"),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/BRANDED_WORLD"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    safe_query = query.replace("|", "")[:20]  # sanitize to avoid callback issues
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{safe_query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{safe_query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]

