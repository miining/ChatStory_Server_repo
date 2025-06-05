from pydantic import BaseModel, Field
from typing import List, Optional

# 사용자가 보낸 채팅 메시지
class ChatMessageRequest(BaseModel):
    user_id: str = Field(..., example="user1234")
    book_id: str = Field(..., example="book1")
    category: str = Field(..., example="무협")
    prompt: str = Field(..., example="그는 문을 열었다.")


# AI가 생성한 소설 텍스트 응답
class ChatMessageResponse(BaseModel):
    response: str = Field(..., example="문 너머에는 생각지도 못한 인물이 서 있었다.")
