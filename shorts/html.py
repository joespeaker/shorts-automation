from html2image import Html2Image
from PIL import Image
import os
hti = Html2Image(custom_flags=['--virtual-time-budget=10000', '--hide-scrollbars'])



data =  {"""
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <script src="https://kit.fontawesome.com/f7b26bdd81.js" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  </head>
  <body style="background-color: transparent;">
    <div class="position-absolute top-50 start-50 translate-middle">
        <div class="card bg-dark rounded-4" style="width: 400px; color: #FEFEFE; border: #333 2px solid;">
            <div class="card-body">
                <div class="row">
                    <div class="col-2 text-center margin">
                        <i class="fa-brands fa-reddit fa-3x" style="color: #FF5700;"></i>
                    </div>
                    <div class="col-10">
                        <h5 class="card-title">r/MaliciousCompliance</h5>
                        <h6 class="card-subtitle mb-2 text-muted">u/anonymous</h6>
                    </div>
                </div>
                <hr>
                <strong><h5 class="card-text">Charge me a fee to pay online, enjoy your trip to the bank</h5></strong>
                <br>
                <span class="text-muted">
                <i class="fa-regular fa-thumbs-up pe-2"></i>
                <i class="fa-regular fa-message pe-2"></i>
                <i class="fa-regular fa-share-from-square pe-2"></i>
                <i class="fa-regular fa-bookmark pe-2"></i>
                </span>
            </div>
          </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
  </body>
</html>
         """ }

hti.screenshot(html_str=data, save_as='reddit.png')
def convertImage():
    img = Image.open("reddit.png")
    img = img.convert("RGBA")
  
    datas = img.getdata()
  
    newData = []
  
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)
    box = (760, 430, 1160, 650)
    img2 = img.crop(box)
    img2.save("reddit.png", "PNG")
    # img.crop((0, 0, 1080, 1920)).save("reddit.png", "PNG")
    print("Successful")

    
  
convertImage()
