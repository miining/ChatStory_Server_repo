from pymongo import MongoClient
from datetime import datetime
# from app.AI.schemas import StorySaveRequest
import os

mongo_url = os.getenv("MONGO_URL")
client = MongoClient(mongo_url)
db = client[os.getenv("DB_NAME", "chatstory")]

def create_story(story, token):
    user_id = token["sub"]
    # 소설 생성
    result = db.stories.insert_one({ # flag 추가할 것 (새로 생성된 소설인지 아닌지)
        "is_new_story": story.flag, # 이 함수에서는 flag = 1, 기존에서 이어쓰는 함수에서는 flag = 0
        "title": story.title,
        "genre": story.genre,
        "author": user_id,
        "created_at": datetime.now()
    })
    return str(result.inserted_id)

def save_user_message(user_id, req):
    """
    사용자가 보낸 채팅 메시지를 DB에 저장
    """
    chat_doc = {
        "user_id": user_id,
        "book_id": req.book_id,
        "message": req.message,
    }
    result = db.chat_messages.insert_one(chat_doc)
    return str(result.inserted_id)