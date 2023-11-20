from fastapi import Request

async def get_current_user(request: Request) -> None:
	uid = request.headers.get('uid')
	return None if uid is None else {'uid': uid, 'name': 'zzy'}