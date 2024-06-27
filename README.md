# Pitch Coordinate From ⚽ SN-GS24

This dataset consist of the pitch coordinate of the [sn-gamestate-24](https://github.com/SoccerNet/sn-gamestate) dataset.

## Download SN data
1. Install the required package
```
pip install SoccerNet
```
2. Use the following code or download_data.py to download the data (replace the path)
```
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="data/SoccerNetGS")
mySoccerNetDownloader.downloadDataTask(task="gamestate-2024",
                                       split=["train", "valid", "test", "challenge"])
```

## Folder Structure
```
pitch_coord_gs24/
├── train/
│ ├── clip_id.txt/
├── test/
│ ├── clip_id.txt/
├── test/
│ ├── clip_id.txt/
```

## clip_id.txt Example

```csv
track_id,image_id,role,jersey_number,team,bbox_x,bbox_y,bbox_w,bbox_h,pitch_x_bottom_left,pitch_y_bottom_left,pitch_x_bottom_right,pitch_y_bottom_right,pitch_x_bottom_middle,pitch_y_bottom_middle
1,000001,player,17,left,1406,748,101,167,-16.22103119216188,10.87012730965439,-15.529639130748913,10.266759625111394,-15.874354120475461,10.567585230814622
1,000002,player,17,left,1417,745,101,168,-16.206564498603694,10.865532791300861,-15.516164919893262,10.26271761602362,-15.860385557142575,10.563268170315675
1,000003,player,17,left,1429,743,101,169,-16.178189728766025,10.856188482637888,-15.489741948847326,10.254474846050728,-15.832990437192162,10.554477047582091
1,000004,player,17,left,1440,741,101,171,-16.136988970923937,10.841745902752724,-15.45138424233195,10.241674455473902,-15.793216757598833,10.540859208736808
1,000005,player,17,left,1452,739,101,172,-16.084565951972145,10.821567603224878,-15.402593665401316,10.223662197955681,-15.742617211228062,10.521768813619058

```

## Feature Descriptions

### track_id
- **Description**: A unique identifier for each track or sequence of images. This is used to link multiple frames that belong to the same tracking sequence.

### image_id
- **Description**: A unique identifier for each image. This is used to reference individual frames within the dataset img1 folder.

### role
- **Description**: The role of the person or object in the image. For example, this could be "player" to indicate a player on the field.

### jersey_number
- **Description**: The jersey number of the player. This is typically a numeric value worn by players to identify them.

### team
- **Description**: The team to which the player belongs. This can indicate which side the player is on, such as "left" or "right".

### bbox_x
- **Description**: The x-coordinate of the top-left corner of the bounding box that surrounds the player or object in the image.

### bbox_y
- **Description**: The y-coordinate of the top-left corner of the bounding box that surrounds the player or object in the image.

### bbox_w
- **Description**: The width of the bounding box that surrounds the player or object in the image.

### bbox_h
- **Description**: The height of the bounding box that surrounds the player or object in the image.

### pitch_x_bottom_left
- **Description**: Projecting the bbox bottom left image x-coordinate into pitch x-coordinate.

### pitch_y_bottom_left
- **Description**: Projecting the bbox bottom left image y-coordinate into pitch y-coordinate.

### pitch_x_bottom_right
- **Description**: Projecting the bbox bottom right image x-coordinate into pitch x-coordinate.

### pitch_y_bottom_right
- **Description**: Projecting the bbox bottom right image y-coordinate into pitch y-coordinate.

### pitch_x_bottom_middle
- **Description**: Projecting the bbox bottom right image x-coordinate into pitch x-coordinate.

### pitch_y_bottom_middle
- **Description**: Projecting the bbox bottom middle image y-coordinate into pitch y-coordinate.
