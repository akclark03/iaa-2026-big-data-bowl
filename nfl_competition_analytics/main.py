import visualize

import data as nfl_data

if __name__ == "__main__":
    dfs = nfl_data.load_data(data_dir="data/train")

    df = nfl_data.get_play_data(dfs, week="w01", game_id=2023090700, play_id=1741)

    visualize.visualize_nfl_play(df)
