from fastapi import FastAPI
import httpx
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup

app = FastAPI()
url = "https://news.ycombinator.com/"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/titles")
async def titles():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the title links
    titles = soup.find_all("td", class_="title")
    all_titles = [title.get_text(strip=True) for i, title in enumerate(titles) if i % 2 != 0]

    return {"titles": all_titles}

@app.get("/links")
async def links(): 
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    # Hacker News uses <span> tags instead of <a> tags for links
    links = soup.find_all("a", class_="span.titleline > a")

    return {"links": [link.get_text(strip=True) for link in links]}
    
