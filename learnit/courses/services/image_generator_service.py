from io import BytesIO 
from typing import Protocol

from PIL import Image, ImageDraw, ImageFont

from django.core.files import File


class ImageCreate(Protocol):
    def create(self) -> Image:
        raise NotImplementedError


class CategoryImage:
    def __init__(
    self, 
    title: str, 
    height: int = 660, 
    width: int = 400,
    title_color: str = 'blue', 
    bgcolor: str = 'white',
    watemark_color: str = 'grey',
    watemark: str | None = None,
    title_font_size: int | None = None,
    watemark_font_size: int = 35,
    ) -> None:
        self.title = title
        self.watemark = watemark
        self.height = height
        self.width = width
        self.title_color = title_color
        self.bgcolor = bgcolor
        self.watemark_color = watemark_color
        self.title_font_size = title_font_size
        self.watemark_font_size = watemark_font_size

    def create(self) -> Image:
        category_image = Image.new('RGB', (self.height, self.width), self.bgcolor)    
        idraw = ImageDraw.Draw(category_image)
        w, h = category_image.size
        if self.title_font_size is None:
            letters_count = len(self.title)
            self.title_font_size = self._responsive_font_size(letters_count, w) 
            

        font = ImageFont.truetype("arialbd.ttf", size=self.title_font_size)
        if not self.watemark is None: # Watemark write
            watemark_font = ImageFont.truetype("arial.ttf", size=self.watemark_font_size)
            watemark_FW, watemark_FH = watemark_font.getsize(self.watemark)
            idraw.text(
                (
                    (w - watemark_FW) / 2, # Image center x coordinates
                    (h - watemark_FH) - 20 # Image bottom - 20 px y coordinates 
                ), 
                self.watemark, 
                font=watemark_font, 
                fill=self.watemark_color
                )
        # Title write
        fw, fh = font.getsize(self.title)
        idraw.text(
            (
                (w - fw) / 2, # Image center x coordinates
                (h - fh) / 2  # Image center y coordinates
            ), 
            self.title, 
            font=font, 
            fill=self.title_color, 
            align='center'
            )
        
        return category_image
    
    def _responsive_font_size(self, letters_count: int, width: int) -> int:
        font_size = 0
        match letters_count:
            case 1 | 2 | 3:
                font_size = width // 3
                
            case 4 | 5 | 6:
                font_size = width // 4

            case 7 | 8 | 9:
                font_size = width // 6

            case 10 | 11 | 12:
                font_size = width // 8

            case  14 | 15 | 16:
                font_size = width // 10

            case 17 | 18 | 19:
                font_size = width // 12

            case 20 | 21 | 22:
                font_size = width // 14
                
            case _:
                font_size = width // 16
            
        return font_size
                


def _pillow_to_djfile_format(pillow_img: Image, title) -> File:
    thumb_io = BytesIO() 
    pillow_img.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=f'{title}.jpg') 
    
    return thumbnail

def _create_image(
    title: str, 
    watemark: str, 
    creator: ImageCreate, 
    bg_color: str, 
    title_color: str, 
    watemark_color: str
    ) -> File:
    image_creator = creator (
        title, 
        watemark=watemark, 
        bgcolor=bg_color, 
        title_color=title_color, 
        watemark_color=watemark_color
    )
    pimage = image_creator.create()
    img = _pillow_to_djfile_format(pimage, title)

    return img
    
def execute(
    title: str, 
    watemark: str,
    bg_color: str, 
    title_color: str, 
    watemark_color: str) -> File:
    return _create_image(
        title,
        watemark, 
        CategoryImage, 
        bg_color, 
        title_color, 
        watemark_color,
        )