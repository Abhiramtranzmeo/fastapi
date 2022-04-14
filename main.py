from fastapi.openapi.models import Response
from starlette import status

from pigtracking import app

pig = {
    'pidsinfoId': 1,
    'channelId': 2,
    'mid_position': 8765,
    'pig_width': 867
}

@app.post('/pigtracking', status_code=status.HTTP_200_OK)
def pig_details():
    return pig

