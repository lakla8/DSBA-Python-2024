# DSBA-Python-2024

## Description

> [!NOTE] Disclaimer  
> As part of our course, workshops suggest developing a project based on business tasks and their implementation through libraries
>
> The main goal is to develope a **music recommendation application**.

**User story:**
> As music fan, I want to find song, so I can listen it.

First of all, we should choose a **dataset** of songs of various artist in the world from Kaggle: [Spotify and Youtube](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube)  

## App initialization and wrapping as CLI

**Job story:**
> When the application is run, I want to know a summary info about primary dataset  
> (such as quantity of songs or artists, date range etc.) so I can create a search query more accurately.

### Part 1 requirements

> [!IMPORTANT]
> We should use only built-in python functions as we can before import more complex and convenient libraries (such as pandas, file).

1) Read dataset and store it in a appropriate data structure;
2) Write a function to get shape of dataset;
3) Write a function which returns minimum and maximum values from a column if column type is double or integer;
4) Write a function which returns top-n artists with the highest songs count in dataset (with count itself);
5) Using **argparse** tool to implement an application console call with positional and optional arguments.

**Topics:**
> `File reading`, `Argparse`, `Type Annotation`

## Pre-built playlist

**Job story:**
> When I run the function,
> I want to obtain a playlist with n-songs,
> so I can choose a playlist by type (artist or genre or years range or track's audio features) to listen.

### Part 2 requirements

1) Write a function which returns top-n songs by artist;
2) Write a function which returns top-n songs for a genre;
3) Write a function which returns top-n songs by period;
4) Write a function which returns the most top-n similar songs by sound to current (by link);

**Topics:**
> `Sorting`, `Euclidean Distance`, `Cosine Similarity`
