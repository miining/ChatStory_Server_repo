from pydantic import BaseModel, Field
from typing import Literal, List, Optional

class StoryCreate(BaseModel): # 소설 새로 생성 시 
    title: str = Field(..., min_length=1, max_length=100)
    genre: Literal["동화", "연애", "액션", "판타지", "무협", "스릴러", "추리"]
    flag: bool = Field(..., description="새로 생성된 소설인지 여부 (True: 새 소설, False: 생성하던 소설)")

class FrontChatRequest(BaseModel): # 프론트에서 전달 받을 message
    book_id: str          # 소설의 ID (예: "book001")
    message: str          # 사용자가 입력한 메시지
    chapter_id: Optional[str] = None # 챕터 id는 있어도 되고 없어도 됨, 하지만 웬만하면 챕터 새로 시작할 때는 넣는걸로

class ChatSendRequest(BaseModel): # 채팅 요청 함수
    user_id: str
    book_id: str
    prompt: str

class ChatSendResponse(BaseModel): # AI로부터 응답받는 함수
    message: str
    prompt: str