from fastapi import FastAPI
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
async def scrape():
    url = "https://news.ycombinator.com/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("td", class_="title")

    return {"titles": [title.get_text(strip=True) for title in titles]}

