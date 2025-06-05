from fastapi import APIRouter, HTTPException, Response, Depends, Request
from app.schemas.story_schema import StoryCreate, FrontChatRequest
from app.services.story_service import create_story, save_user_message
from app.core.jwt import verify_access_token

router = APIRouter()

@router.post("/create")
async def create_story_router(story: StoryCreate, request: Request):
    # 쿠키에서 토큰 가져오기
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="토큰이 누락되었습니다.")

    # Bearer 제거
    if token.startswith("Bearer "):
        token = token[7:]
    
    # 토큰 검증
    try:
        payload = verify_access_token(token)
        user_id = payload.get("sub")
    except Exception as e:
        raise HTTPException(status_code=403, detail="토큰이 유효하지 않습니다.")

    # 제목과 장르 저장 (예시)
    # 실제로는 DB에 저장해야 함
    try:
        book_id = create_story(story, payload)
        return {
            "book_id": book_id,
            "message": "소설 생성 완료"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="서버와 연결되지 않았습니다.")

@router.post("/chat/send")
async def chat_send(req: FrontChatRequest, request: Request):
    # 1. 사용자 인증 (토큰 검증)
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="토큰이 누락되었습니다.")

    if token.startswith("Bearer "):
        token = token[7:]

    try:
        payload = verify_access_token(token)
        user_id = payload.get("sub")
    except Exception:
        raise HTTPException(status_code=403, detail="토큰이 유효하지 않습니다.")

    # 2. 사용자 메시지 DB에 저장
    try:
        chat_id = save_user_message(user_id, req)
    except Exception:
        raise HTTPException(status_code=500, detail="메시지 저장 실패")

    # 3. 바로 응답
    return {
        "chat_id": chat_id,
        "message": "채팅 메시지가 정상적으로 저장되었습니다."
    }