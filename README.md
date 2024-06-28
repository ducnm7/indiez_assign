# **PIXEL ART** - User Experience Analysis

## Introduction
This project aims to analyze the improvement level of update 1.6.0 compared to the previous update 1.5.2. And from there, make suggestions for new improvements for the next updates.

## Data Description
- **Source:** The data was sourced from **Pixel Art** game from **INDIEZ** released in the Russian market.
- **Variables:**
  | Column Name  | Defination |
  | ------------- | ------------- |
  | user  | identifies each user  |
  | day_diff  | = day_time - day0  |
  | day0  | Records the time when the user first opened the game.  |
  | mode_game  | Describes the mode of the game (e.g., session start or user engagement)  |
  | win  | Records whether the user won (1) or lost (0) in the game_end event.|
  | reason_to_die  | records the reason why the user lost in the game_end event.  |
  | quantity  | records properties of event_names (e.g., time duration in seconds, steps completed in the tutorial)  |
  | version  | represents the version of the app that the user is using  |
  
- The **event_name** value:
  | Value  | Defination |
  | ------------- | ------------- |
  | tutorial  | guides the user on how to play, with each step recorded in the `quantity` column. (-2): Acknowledges that the user has completed the entire tutorial successfully. (-1): Records the user starting the tutorial. 1, 2, 3, 4, etc. represent individual steps in the tutorial. The exact number depends on the design of the tutorial; there may be more or fewer steps. 0: indicates that the user has chosen to skip the tutorial. The tutorial event provides a detailed breakdown of the user's progress through the instructional levels, with each step and completion status being recorded in the quantity column. This information can be valuable for analyzing how users engage with and complete the tutorial within the gaming app  |
  | game_start  |  Marks when the user starts a certain level.  |
  | game_end  | Marks when the user finishes a level, indicating a win or loss. Loss reasons are recorded in the reason_to_die column, and the playing time is in the quantity column.  |
  | user_engagement  | Recorded continuously while the user plays, with two types: ss for session start, and ue for user engagement. The time the user is active is recorded in the quantity column.  |

