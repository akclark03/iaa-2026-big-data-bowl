from pathlib import Path

import pandas as pd


def load_data(data_dir: str) -> dict[str, pd.DataFrame]:
    """Load all CSV files from the specified directory into a dictionary of DataFrames.

    Args:
        data_dir (Path): The directory containing the CSV files.
    """
    data = {}
    for file_path in Path(data_dir).glob("*.csv"):
        key = file_path.stem
        data[key] = pd.read_csv(file_path)
    return data


def get_play_data(dfs, week, game_id, play_id, output=False):
    input_key = f"input_2023_{week}"
    output_key = f"output_2023_{week}"
    input_df = dfs[input_key]
    output_df = dfs[output_key]

    # Get play data
    in_play_df = input_df[
        (input_df["game_id"] == game_id) & (input_df["play_id"] == play_id)
    ]

    if not output:
        return in_play_df

    out_play_df = output_df[
        (output_df["game_id"] == game_id) & (output_df["play_id"] == play_id)
    ]

    # Columns to carry over (store once, no duplicates)
    cat_cols = [
        "game_id",
        "play_id",
        "nfl_id",
        "player_name",
        "player_role",
        "player_position",
        "player_side",
        "player_height",
        "player_weight",
        "player_birth_date",
        "player_to_predict",
        "play_direction",
        "absolute_yardline_number",
        "ball_land_x",
        "ball_land_y",
    ]

    # Unique categorical info by key
    cat_info = in_play_df[cat_cols].drop_duplicates()

    # Merge categorical info, using clear suffix for new columns
    out_play_df = out_play_df.merge(
        cat_info,
        on=["game_id", "play_id", "nfl_id"],
        how="left",
        suffixes=("", "_from_cat"),
    )

    # Fill in missing merge columns from cat info, drop temporary columns
    for col in cat_cols:
        if col not in ["game_id", "play_id", "nfl_id"]:
            cat_col = f"{col}_from_cat"
            if cat_col in out_play_df:
                out_play_df[col] = out_play_df[col].combine_first(out_play_df[cat_col])
                out_play_df = out_play_df.drop(columns=[cat_col])

    # Make frame_id continuous after input's max frame
    max_frame = (
        in_play_df.groupby(["game_id", "play_id", "nfl_id"])["frame_id"]
        .max()
        .rename("max_input_frame")
    )
    out_play_df = out_play_df.merge(
        max_frame, on=["game_id", "play_id", "nfl_id"], how="left"
    )
    out_play_df["frame_id"] += out_play_df["max_input_frame"]
    out_play_df = out_play_df.drop(columns=["max_input_frame"])

    # Concatenate clean input/output play data
    play_df = pd.concat([in_play_df, out_play_df], ignore_index=True)
    return play_df


if __name__ == "__main__":
    dfs = load_data(data_dir="data/train")

    df = get_play_data(
        dfs,
        week="w01",
        game_id=2023090700,
        play_id=1741,
        output=True,
    )
