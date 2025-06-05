# app/ai/client.py
import httpx
from app.AI.schemas import ChatMessageRequest, ChatMessageResponse
from app.core.config import settings  # .env에서 AI_SERVER_URL 불러올 예정

# 비동기 함수로 정의
async def send_message_to_ai_server(data: ChatMessageRequest) -> ChatMessageResponse:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                # url=f"{settings.AI_SERVER_URL}/generate",  # 예시 endpoint
                url=f"/{settings.AI_SERVER_URL}",  # 예시 endpoint                
                json=data.dict()
            )
            response.raise_for_status()
            result = response.json()
            return ChatMessageResponse(**result)
        except httpx.HTTPError as e:
            # 에러 핸들링 (로그 출력 or 예외 전파)
            raise RuntimeError(f"AI 서버 통신 실패: {str(e)}")
