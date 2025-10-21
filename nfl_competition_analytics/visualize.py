import matplotlib.pyplot as plt


def visualize_nfl_play(play_df, frames=14):
    game_id = play_df["game_id"].iloc[0]
    play_id = play_df["play_id"].iloc[0]

    fig, ax = plt.subplots(figsize=(12, 8))
    for player, group in play_df.groupby("player_name"):
        ax.plot(group["x"], group["y"], label=player)
        ax.text(group["x"].iloc[0], group["y"].iloc[0], player, fontsize=8)
    ax.scatter(
        play_df["ball_land_x"].iloc[-1], play_df["ball_land_y"].iloc[-1], color="red"
    )
    ax.set_xlabel("X (Yards)")
    ax.set_ylabel("Y (Yards)")
    ax.set_title(f"Play {play_id} from Game {game_id}")
    ax.set_ylim(0, 53.3)
    ax.legend()
    plt.savefig(f"figures/play_{play_id}_game_{game_id}.png")
