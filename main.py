from fastapi import FastAPI
import httpx
from bs4 import BeautifulSoup

app = FastAPI()
url = "https://news.ycombinator.com/"

@app.get("/titles")
async def titles():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("td", class_="title")

    return {"titles": [title.get_text(strip=True) for title in titles]}

@app.get("/links")
async def links(): 
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("span", class_="sitestr")

    return {"links": [link.get_text(strip=True) for link in links]}
    


