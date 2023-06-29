from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄 ايقاف 🙄",
            description=f"لايقاف التشغيل المؤقت.",
            thumb_url="https://graph.org/file/e240c5120f91ed0a9f13f.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 استئناف 😋",
            description=f"لاستئناف التشغيل في المكالمه.",
            thumb_url="https://graph.org/file/f088f33226badc5154285.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂 تخطي 🙂",
            description=f"لتخطي الاغنيه وتشغيل اغنيه اخرى في قائمة التشغيل.",
            thumb_url="https://graph.org/file/8f87bc4932cd94b1c785b.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 انهاء 🥺",
            description="لانهاء التشغيل.",
            thumb_url="https://graph.org/file/7c2298a2ef86d29ab8589.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥴 دمج 🥴",
            description="لخلط الاغاني في قائمة التشغيل.",
            thumb_url="https://graph.org/file/7c2298a2ef86d29ab8589.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🥱 تكرار 🥱",
            description="لتكرار الاغنيه.",
            thumb_url="https://graph.org/file/30719d27eb72c2dc29411.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
