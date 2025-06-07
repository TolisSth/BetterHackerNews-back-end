from fastapi import FastAPI
import httpx
from bs4 import BeautifulSoup

app = FastAPI()
url = "https://news.ycombinator.com/"

@app.get("/titles")
async def titles():
    url = "https://news.ycombinator.com/"  # Make sure 'url' is defined
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the title links
    titles = soup.find_all("td", class_="title")
    all_titles = [title.get_text(strip=True) for i, title in enumerate(titles) if i % 2 != 0]

    return {"odd_titles": all_titles}

@app.get("/links")
async def links(): 
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    # Hacker News uses <span> tags instead of <a> tags for links
    links = soup.find_all("span", class_="sitestr")

    return {"links": [link.get_text(strip=True) for link in links]}
    
