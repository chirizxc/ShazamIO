from typing import List, Optional

from pydantic import BaseModel, Field


class AttributeName(BaseModel):
    title: str


class ArtistAttribute(BaseModel):
    genre_names: List[str] = Field([], alias="genreNames")
    name: str
    url: str
    artist_bio: Optional[str] = Field(None, alias="artistBio")
