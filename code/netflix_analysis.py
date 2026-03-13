import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("images", exist_ok=True)
df = pd.read_csv("data/netflix_titles.csv")
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns)
df["country"] = df["country"].fillna("Unknown")
type_count = df["type"].value_counts()

type_count.plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("images/movies_vs_tvshows.png")
plt.close()

year_data = df["release_year"].value_counts().sort_index()

year_data.plot()
plt.title("Netflix Content Release Trend")
plt.xlabel("Year")
plt.ylabel("Number of Shows")

plt.savefig("images/release_trend.png")
plt.close()

top_countries = df["country"].value_counts().head(10)

top_countries.plot(kind="bar")
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Shows")

plt.savefig("images/top_countries.png")
plt.close()
top_ratings = df["rating"].value_counts().head(10)

top_ratings.plot(kind="bar")
plt.title("Most Common Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("images/top_ratings.png")
plt.close()
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

year_added = df["year_added"].value_counts().sort_index()

year_added.plot()
plt.title("Content Added to Netflix Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Shows")

plt.savefig("images/content_added_per_year.png")
plt.close()

print("Analysis completed. Charts saved in images folder.")