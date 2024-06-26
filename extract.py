import os
import json
import pandas as pd
from tqdm import tqdm
import pdb


dataset_path="path/to/your/directory/" #path to the directory where the dataset was downloaded
out_path="save_path" #path to save the pitch coordinates

#get all the folders in the dataset path and remove gamestate-2024
dataset = [f for f in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, f)) and f != "gamestate-2024" and f != "challenge"]

for set in dataset:
    #get all the folders in the dataset path
    set_path = os.path.join(dataset_path, set)
    out_set_path = os.path.join(out_path, set)
    os.makedirs(out_set_path, exist_ok=True)
    games = [f for f in os.listdir(set_path) if os.path.isdir(os.path.join(set_path, f))]
    for game in tqdm(games):
        #read the Labels-GameState.json file in the game folder
        game_path = os.path.join(set_path, game)
        json_file = os.path.join(game_path, "Labels-GameState.json")
        with open(json_file) as f:
            data = json.load(f)
            data = data['annotations']
        #get the pitch coordinates
        out_data = []
        for item in data:
            if item['supercategory']=='object':
                track_id=item.get('track_id')
                image_id=item.get('image_id')
                if image_id is not None:
                    image_id = image_id[-6:]
                role=item.get('attributes',{}).get('role')
                jersey_number=item.get('attributes',{}).get('jersey')
                team=item.get('attributes',{}).get('team')
                bbox_x=item.get('bbox_image',{}).get('x')
                bbox_y=item.get('bbox_image',{}).get('y')
                bbox_w=item.get('bbox_image',{}).get('w')
                bbox_h=item.get('bbox_image',{}).get('h')
                try:
                    pitch_x_bottom_left=item.get('bbox_pitch',{}).get('x_bottom_left')
                    pitch_y_bottom_left=item.get('bbox_pitch',{}).get('y_bottom_left')
                    pitch_x_bottom_right=item.get('bbox_pitch',{}).get('x_bottom_right')
                    pitch_y_bottom_right=item.get('bbox_pitch',{}).get('y_bottom_right')
                    pitch_x_bottom_middle=item.get('bbox_pitch',{}).get('x_bottom_middle')
                    pitch_y_bottom_middle=item.get('bbox_pitch',{}).get('y_bottom_middle')
                except:
                    pitch_x_bottom_left=None
                    pitch_y_bottom_left=None
                    pitch_x_bottom_right=None
                    pitch_y_bottom_right=None
                    pitch_x_bottom_middle=None
                    pitch_y_bottom_middle=None
            
                out_data.append([track_id, image_id, role, jersey_number, team, bbox_x, bbox_y, bbox_w, bbox_h, pitch_x_bottom_left, pitch_y_bottom_left, pitch_x_bottom_right, pitch_y_bottom_right, pitch_x_bottom_middle, pitch_y_bottom_middle])
        #save the pitch coordinates in a csv file
        out_df = pd.DataFrame(out_data, columns=['track_id', 'image_id', 'role', 'jersey_number', 'team', 'bbox_x', 'bbox_y', 'bbox_w', 'bbox_h', 'pitch_x_bottom_left', 'pitch_y_bottom_left', 'pitch_x_bottom_right', 'pitch_y_bottom_right', 'pitch_x_bottom_middle', 'pitch_y_bottom_middle'])
        #order the row with the track_id and image_id
        out_df = out_df.sort_values(by=['track_id', 'image_id'])
        out_df.to_csv(os.path.join(out_set_path, f"{game}.txt"), index=False)

        

        # pdb.set_trace()
